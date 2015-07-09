package org.apache.spark.examples.streaming

import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.SparkContext._
import org.apache.spark.streaming.twitter._
import org.apache.spark.SparkConf
import org.apache.spark.streaming.StreamingContext._

object Twitter {
  def main(args: Array[String]) {
    System.setProperty("twitter4j.oauth.consumerKey", "QR4co8GaZu0AmFRgZ7vq7LotG")
    System.setProperty("twitter4j.oauth.consumerSecret", "WcsVKcyVP2b9BlufmYRJks8pFiWZorZZtWG9eDe42zp7eu7OWt")
    System.setProperty("twitter4j.oauth.accessToken", "219923247-EwJrkzHkP9CZ3udl3lpzIMSOAMGYy133WmPl2OPz")
    System.setProperty("twitter4j.oauth.accessTokenSecret", "mV6KOgZAISmXuiO46y21NXJ4NtxHzk6oSmzXEpGLsHLp3")

    val totalSampleTime_minutes = args(0)
    val subSampleTime_minutes = args(1)
    val numTopics = args(2)
    

    val sparkConf = new SparkConf().setAppName("twitterProj").setMaster("spark://spark1:7077")
    val ssc = new StreamingContext(sparkConf, Seconds(5))
    val stream = TwitterUtils.createStream(ssc, None)
    println("Type of stream: " + stream.getClass)
    val tweets = stream.map(tweet => tweet.getText())
    println("Type of tweets: " + tweets.getClass)
    val tags = stream.flatMap(tweet => tweet.getText().split(" ")).filter(word => word.startsWith("#"))
    println("Type of tags: " + tags.getClass)
    val sortedCounts = tags.map(tag => (tag, 1))
                     .reduceByKey((a, b) => a + b)
                     .map(count => (count._2, count._1))
                     .transform(rdd => rdd.sortByKey(false))

    println("Type of sortedCounts: " + sortedCounts.getClass)
    //println("Type of sortedCounts[T]: " + sortedCounts[T])
    //sortedCounts.foreach(rdd => println("\nTop "+numTopics+" tags:\n" + rdd.take(numTopics.toInt).mkString("\n")))
    sortedCounts.foreach(rdd => {
        val pops = rdd.take(numTopics.toInt)
        //authorTagLists = stream.map(tweet => (tweet.getUser().getName(), tweet.getText().split(" ").filter(word => word.startsWith("#"))
        val popAuthors = stream.map(tweet => 
                tweet.getText().split(" "))
               .filter(word => word.startsWith("#"))
               //.intersection(pops)
               .map(tag => (tag, tweet.getUser().getName()))
               .foreach(tup => print(tup))
    })


    ssc.start()
    ssc.awaitTermination()
  }
}
