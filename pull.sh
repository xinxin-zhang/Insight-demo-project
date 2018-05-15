cd /home/ubuntu/Insight-demo-project/
sleep 20s
git checkout master
git stash
git pull
tmux kill-session -t k1
