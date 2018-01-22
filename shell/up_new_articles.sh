#!/bin/bash
FileLocation="/root/Desktop"
S1="xx.xx.xx.xx1"
S2="xx.xx.xx.xx2"

#judge old or new
if [ "$1" == "old" ]; then
S="xx.xx.xx.xx1"
elif [ "$1" = "new" ]; then
S="xx.xx.xx.xx2"
fi

# up to old server: S1
# 'today' is the whole file, 'articles' is the whole original articles
scp -i ${FileLocation}/xxxxx.pem ${FileLocation}/today/articles/*.naf root@${S1}:/usr/soft/apache-tomcat-7.0.78/webapps/chaorder_articles

# up to new server: S2
scp -i ${FileLocation}/xxxxx.pem -r ${FileLocation}/today/rdfs root@${S}:/root/boson/ks-files
#remote interaction
expect<<-END
spawn ssh -i /root/Desktop/xxxxx.pem -l root ${S}
expect "~$*"
#interact
send "rm -r /root/boson/ks-files/events\r"
#send "/root/boson/ks-files/exec_multi.sh >> /root/boson/ks-files/populate.log | tail -f /root/boson/ks-files/populate.log\r"
send "/root/boson/ks-files/exec_multi.sh >> /root/boson/ks-files/populate.log\r"
#send "echo -e '\003'"
set timeout -1
send "exit\n"
expect eof
exit
END
#bash ${FileLocation}/t1.sh
scp -i ${FileLocation}/xxxxx.pem root@${S}:/root/boson/ks-files/populate.log ./

echo "execute successfully!"
