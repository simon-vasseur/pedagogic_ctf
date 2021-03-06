#!/bin/bash

service redis-server restart

rm /entrypoint.sh
rm /requirements.txt

echo "127.0.0.1 $(hostname)" >> /etc/hosts
echo "127.0.0.1 evil.com" >> /etc/hosts
echo "127.0.0.1 my-site.com" >> /etc/hosts

tc qdisc add dev eth0 root tbf rate 10kbps latency 50ms burst 2500

cd /home/selenium
for i in {1..3}
do
    sudo -u selenium nohup python3 worker.py selenium &
done
sudo -u selenium python3 api.py
