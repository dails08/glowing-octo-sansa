package org.apache.spark.examples.streaming

import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.SparkContext._
import org.apache.spark.streaming.twitter._
import org.apache.spark.SparkConf
import org.apache.spark.streaming.StreamingContext._
import scala.io.Source

object Twitter {
  def main(args: Array[String]) {
    
    val creds = Source.fromFile("creds.txt").getLines.toArray

    System.setProperty("twitter4j.oauth.consumerKey", creds(0))
    System.setProperty("twitter4j.oauth.consumerSecret", creds(1))
    System.setProperty("twitter4j.oauth.accessToken", creds(2))
    System.setProperty("twitter4j.oauth.accessTokenSecret", creds(3))


    

    val totalSampleTime_minutes = args(0)
    val subSampleTime_minutes = args(1)
    val numTopics = args(2)
    

    val sparkConf = new SparkConf().setAppName("twitterProj").setMaster("spark://spark1:7077")
    val ssc = new StreamingContext(sparkConf, Seconds(5))
    val stream = TwitterUtils.createStream(ssc, None)

    val tweets = stream.map(tweet => {
        val hashtags = tweet.getText().split(" ").filter(word => word.startsWith("#"))
        val username = tweet.getUser.getScreenName()
        val mentions = tweet.getText().split(" ").filter(word => word.startsWith("@"))
        (hashtags, username, mentions)})
        .flatMap(tup => tup._1.map(hashtag => (hashtag, tup._2, tup._3)))

    val popTags = tweets.map(tuple => (tuple._1,1))
        .reduceByKeyAndWindow((a:Int, b:Int) => (a+b), Seconds(subSampleTime_minutes.toInt*60))
        .map(tuple => (tuple._2, tuple._1))
        .transform(tuple => tuple.sortByKey(false))

    val popUsers = tweets.map(tuple => (tuple._2,1))
        .reduceByKeyAndWindow((a:Int, b:Int) => (a+b), Seconds(subSampleTime_minutes.toInt*60))
        .map(tuple => (tuple._2, tuple._1))
        .transform(tuple => tuple.sortByKey(false))
   
    val popMentions = tweets.flatMap(tuple => tuple._3)
        .map(mention => (mention,1))
        .reduceByKeyAndWindow((a:Int, b:Int) => (a+b), Seconds(subSampleTime_minutes.toInt*60))
        .map(tuple => (tuple._2, tuple._1))
        .transform(tuple => tuple.sortByKey(false))

    popTags.foreachRDD(rdd => rdd.take(numTopics.toInt).foreach(tuple => println(tuple._2 + ": " + tuple._1))) 
    popUsers.foreachRDD(rdd => rdd.take(numTopics.toInt).foreach(tuple => println(" "+tuple._2 + ": " + tuple._1))) 
    popMentions.foreachRDD(rdd => rdd.take(numTopics.toInt).foreach(tuple => println("  "+tuple._2 + ": " + tuple._1))) 


    val related = tweets.foreachRDD(rdd => rdd.map(tup => (tup._1, (1, Set(tup._2), tup._3.toSet)))
        .foldByKey(0, Set(), Set())((acc, tup) => (acc._1 + tup._1, acc._2 ++ tup._2, acc._3 ++ tup._3))
        .sortBy(recTup => recTup._2._1, false)
        .take(numTopics.toInt)
        .foreach(recTup => {
            println("Related stuff:")
            println("===================")
            println(recTup._1+": "+recTup._2._1+
            "\n  Authors: "+recTup._2._2.mkString(",")+
            "\n  Mentions: "+recTup._2._3.mkString(","))
            println("===================")})
        )


    ssc.start()
    ssc.awaitTermination()
  }
}
