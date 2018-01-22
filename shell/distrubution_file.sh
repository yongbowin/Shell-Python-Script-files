#!/bin/bash
nodes=(
192.168.100.242
192.168.100.245
192.168.100.246
192.168.100.247
)
for host in ${nodes[@]}
do
	rsync -avz /root/Desktop/$1 $host:/root/Desktop/$1
done
ret=$?
if [ $ret -eq 0 ]
	then
	echo "$1 completed!"
else
	echo "$1 failed!"
fi
