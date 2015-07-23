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
    val sortedTags = stream.flatMap(tweet => 
                      tweet.getText().split(" ")
                      .filter(word => word.startsWith("#"))
                      .map(tag => (tag, 1)))
                      .reduceByKey((a, b) => a + b)
                      .map(count => (count._2, count._1))
                      .transform(rdd => rdd.sortByKey(false))
                    //  .take(numTopics.toInt)
                    //  .transform(tup => tup._2)

    val popTags = sortedTags.take(numTopics.toInt)     

//    val tags = stream.flatMap(tweet => tweet.getText().split(" ")).filter(word => word.startsWith("#"))
//    println("Type of tags: " + tags.getClass)

//    val sortedCounts = tags.map(tag => (tag, 1))
//                     .reduceByKey((a, b) => a + b)
//                     .map(count => (count._2, count._1))
//                     .transform(rdd => rdd.sortByKey(false))

//    println("Type of sortedCounts: " + sortedCounts.getClass)
    
    
    popTags.foreach(tag => {
        println("Starting inside popTags")
        println("Length of popTags: "+popTags.count)
        println("Length of rdd: "+rdd.count)
        println("Length of popTags: " + popTags.length)
        println("For tag: " + tag)
        stream.filter(tweet => tweet.getText().split(" ").startsWith("#"))
              .foreach(tweet => println("\t" + tweet.getUser().getName()))
        })

//            stream.map(tweet => 
//            tweet.getText().split(" ")
//            .filter(word => word.startsWith("#"))
//            .filter(word => pops.contains(word))
//            .map(tag => {
//                          println("Keeping "+tweet.getUser().getName() + " and " + tag)
//                          (tweet.getUser().getName(), tag)
//                        }))
                       
            //.filter(tup => pops.contains(tup._2))
//            .foreach(tup => println((tweet.getUser().getName(), tup))))
        //val innerTags = 
        //stream.map(tweet => {
        //        //var userName = tweet.getUser().getName()
        //        tweet.getText().split(" ")
        //        .filter(word => word.startsWith("#"))
        //        .filter(word => pops.contains(word))
        //        .foreach(word => println(word, tweet.getUser().getName()))
        //        })
        //        //.intersection(pops)
        //println("Length of innerTags: "+innerTags.count)               
        //val authorTagTuples = innerTags.map(tag => (tag, tweet.getUser().getName()))
        //println("Length of authorTagTuples: "+authorTagTuples.count)       
        //authorTagTuples.foreach(tup => print(tup))
//    })


    ssc.start()
    ssc.awaitTermination()
  }
}
