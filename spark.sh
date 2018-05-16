cd /home/ubuntu/Insight-demo-project/spark-streaming
spark-submit --class PriceDataStreaming --master spark://ec2-35-160-167-99.us-west-2.compute.amazonaws.com:7077 --jars target/scala-2.11/streamhits-assembly-1.0.jar target/scala-2.11/streamhits-assembly-1.0.jar
