yum install docker.io
yum install docker-ce
yum install docker
clear
docker
clear
flask
clear
vim
yum install vim
vim hello_world.py
ls
yum update -y
yum -y update
yum upgrade -y
ping 8.8.8.
ping 8.8.8.8
ping google.fr
cat /etc/redhat-release
yum install net-snmp net-snmp-utils -y
systemctl status snmpd
cd /etc
ls
cd snmp/
ls
cat snmpd.conf
cat snmpd.conf.orig 
clear
ls
mv snmpd.conf.orig snmpd.conf
ls
cat snmpd.conf
cat snmpd.conf.orig 
vim snmpd.conf.orig 
snmpwalk -v 1 192.168.56.120 -c public
ping 192.168.56.120
ping 192.168.56.3
ls
cd root
ls
ls -a
sudo rm .git
sudo rm .git -R
sudo rm .gitconf -R
sudo rm .gitconfig -R
clear
ip -a
git init .
ls -a
git remote
git remote -v
git remote add origin git@github.com:Kassim28/projet_snmp.git
bit branch
git branch
git branch -M main
git branch -M master
git add .
git commit -am "first commit"
git config --global user.email "jondeaukassim@gmail.com
"
git config --global user.name "Kassim Jondeau"
git commit -am "First Commit"
git branch
git branch -M main
git push -u origin main
ssh-keygen 
cat ~/.ssh/id_rsa.pub 
git push -u origin main
ip a
dhclient
ip a
sudo poweroff
ls
cd root
ls
ls -a
git add .
git commit -am "commit 1"
git remot
git remote
git push origin main
ls
git branch
git branch --help
git branch test
git status
git branch
git pull
cd .ssh
ls
cat id_rsa
cat id_rsa_pub
cat id_rsa.pub
cd
git add .
ls
git status
git add .
git push origin test
git pull
git --help
 snmpget -v 1 -c public pc1 1.3.6.1.2.1.1.1
ping pc1
snmpwalk -v 1 -c public pc1
snmpwalk --h
snmpwalk -v 1 -c default pc1
snmpwalk -v 1 -c default pc1 MIB;2
snmpwalk -v 1 -c default pc1 MIB:2
snmpwalk -v 1 -c default pc1 
snmpget -v 1 -c default pc1 1.3.6.1.2.1.1.3
snmpwalk -v 1 -c public pc1
snmpget -v 1 -c public pc1 1.3.6.1.2.1.1.3
snmpget -v 1 -c public pc1 1.3.6.1.2.1.1.3 MIB:2
snmpget -v 1 -c public pc1 1.3.6.1.2.1.1.3 
snmpget -v 1 -c public pc1 1.3.6.1.2.1.1.3.1 
snmpget -v 1 -c public pc1 1.3.6.1.2.1.1
snmpget -v 1 -c public pc1 .1.3.6.1.2.1.1
snmpwalk -v 1 -c public pc1
snmpget -v 1 -c public pc1 SNMPv2-MIB::sysName.0
snmpget -v 1 -c public pc1 SNMPv2-MIB::sysName.1
snmpget -v 1 -c public pc1 SNMPv2-MIB::sysName.0
snmpget -v 1 -c public pc1 1.3.6.1.2.1.4.22.1.2.0
snmpget -v 1 -c public pc1 1.3.6.1.2.1.4.22.1.2.1
snmpget -v 1 -c public pc1 1.3.6.1.2.1.4.32.1
snmpget -v 1 -c public pc1 1.3.6.1.2.1.4.32.1.0
snmpget -v 1 -c public pc1 1.3.6.1.2.1.4.32
snmpget -v 1 -c public pc1 1.3.6.1.2.1.4.34.1.2
snmpget -v 1 -c public pc1 1.3.6.1.2.1.4.34.1.2.0
Snmpget -v 1 -c public @IP SNMPv2-MIB::sysName.0
snmpget -v 1 -c public @IP SNMPv2-MIB::sysName.0
snmpget -v 1 -c public pc1 SNMPv2-MIB::sysName.0
snmpget -v 1 -c snmp_kas pc1 SNMPv2-MIB::sysName.0
snmpget -v 1 -c snmp_kas pc1 SNMPv2-MIB::sysName
snmpget -v 1 -c snmp_kas pc1 SNMPv2-MIB::sysName.0
snmpwalk -v 1 -c snmp_kas pc1 
clear
systemctl restart snmpd
snmpwalk -v 1 -c snmpkas 
snmpwalk -v 1 -c snmpkas pc1
snmpwalk -v 1 -c snmp_kas pc1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.34.1.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.34.1.2.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.34.1
ip a
snmpwalk -v 1 -c snmp_kas pc1
snmpwalk -v 1 -c snmp_kas pc1 MIB:2
snmpwalk -v 1 -c snmp_kas pc1 -m MIB:2
snmpwalk -v 1 -c snmp_kas pc1 -m IP
snmpwalk -v 1 -c snmp_kas pc1 
snmpwalk -v 1 -c snmp_kas pc1 -m IP-MIB
ip a
snmpget -v 1 -c snmp_kas SNMPv2-SMI::mib-2.55.1.5.1.8.2 
snmpget -v 1 -c snmp_kas pc1 SNMPv2-SMI::mib-2.55.1.5.1.8.2 
snmpwalk -v 1 -c snmp_kas pc1 -m IP-MIB
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.10
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.10.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.10
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.10.1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.10.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.10.3
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.10.4
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.16.1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.16.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.16.3
ip a
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.16.4
yum install iperf -y
curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.rpm.sh | sudo bash
sudo yum install speedtest
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.16.3
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.16.2
ip a
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.16.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.16.3
clear
yum install rrdtool
rrdtool
git add .
git add . -A
git commit -am "commit 2"
git push origin test
git push origin main
export FLASK_APP=NMS.py
flask run
clear
rrdtool create test.rrd --start 920804400 DS:speed:COUNTER:600:U:U RRA:AVERAGE:0.5:1:24 RRA:AVERAGE:0.5.:6:10
 rrdtool update test.rrd 920804700:12345 920805000:12357 920805300:12363
 rrdtool update test.rrd 920805600:12363 920805900:12363 920806200:12373
 rrdtool update test.rrd 920806500:12383 920806800:12393 920807100:12399
 rrdtool update test.rrd 920807400:12405 920807700:12411 920808000:12415
 rrdtool update test.rrd 920808300:12420 920808600:12422 920808900:12423
 rrdtool fetch test.rrd AVERAGE --start 920804400 --end 920809200
git branch test
git checkout test
git add .
git status
git add . -at
git add . -A
git commit -am "commit 2"
git push origin main
git push origin test
 rrdtool fetch test.rrd AVERAGE --start 920804400 --end 920809200
rrdtool graph speed.png --start 92080400 --end 920808000 DEF:myspeed=test.rrd:speed:AVERAGE LINE2:myspeed#FF0000
rrdtool graph speed.png --start 920804400 --end 920808000 DEF:myspeed=test.rrd:speed:AVERAGE LINE2:myspeed#FF0000
ls
cat speed.png 
clear
xdg-open
display
yum install xdg-open
feh
yum install feh
python3 -m http.server 8080
clear
pip3 install pysnmp
python3 NMS.py 
flask run
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.4.1.2021.11.9.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.4.1.2021.11.52.0
snmpwalk -v 1 -c snmp_kas pc1 
snmpwalk -v 1 -c snmp_kas pc1 -m MIB:2
clear
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.4.1.2021.4.6.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.4.1.2021.4.11.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.4.1.2021.4.5.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.1.3.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.3
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.4
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2.
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2
snmpget -v 1 -c snmp_kas pc1 .1.3.6.1.2.1.2.2.1.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.8
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.8.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.8.1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.8.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.8.3
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.6.1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.6.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.6.3
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.2.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.5
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.5.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.5
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.5
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.34
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.34.0
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.34.1
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.34.2
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.34
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.20
snmpget -v 1 -c snmp_kas pc1 1.3.6.1.2.1.4.20.0
clear
snmpwalk -v 1 -c snmp_kas pc1 1.3.6.1.2.1.2.2.1.2
