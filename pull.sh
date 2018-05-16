cd /home/ubuntu/Insight-demo-project/
sleep 20s
git checkout master
git stash
git pull
tmux kill-session -t k1
./usr/local/spark/sbin/stop-all.sh
sleep 20s
./usr/local/spark/sbin/start-all.sh
cd /home/ubuntu/Insight-demo-project/spark-streaming
sbt assembly
sleep 2m
