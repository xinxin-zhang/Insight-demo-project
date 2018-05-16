cd /home/ubuntu/Insight-demo-project/
sleep 20s
git checkout master
git stash
git pull
tmux kill-session -t k1
cd /usr/local/spark/sbin/
./stop-all.sh
sleep 1m
cqlsh -e "TRUNCATE hitplayground.hitinfo ;"
cqlsh -e "TRUNCATE hitplayground.groupinfo ;"
./start-all.sh
cd /home/ubuntu/Insight-demo-project/spark-streaming
sbt assembly
sleep 2m
spark-submit --class PriceDataStreaming --master spark://ec2-35-160-167-99.us-west-2.compute.amazonaws.com:7077 --jars target/scala-2.11/streamhits-assembly-1.0.jar target/scala-2.11/streamhits-assembly-1.0.jar
sleep 30s
cd /home/ubuntu/Insight-demo-project/producer/
bash spawn_kafka_streams.sh ec2-35-160-167-99.us-west-2.compute.amazonaws.com 4 k1
