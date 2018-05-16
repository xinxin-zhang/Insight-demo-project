cd /home/ubuntu/Insight-demo-project/
sleep 20s
git checkout master
git stash
git pull
tmux kill-session -t k1
cd /usr/local/spark/sbin/
./stop-all.sh
sleep 20s
cqlsh -e "TRUNCATE hitplayground.hitinfo ;"
cqlsh -e "TRUNCATE hitplayground.groupinfo ;"
./start-all.sh
cd /home/ubuntu/Insight-demo-project/spark-streaming
sbt assembly
sleep 1m
