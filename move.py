# -*- coding:utf-8 -*-
import os

os.system('mv /etc/named.conf /etc/named.conf.bak')
os.system('mv /etc/named.rfc1912.zones /etc/named.rfc1912.zones.bak')
os.system('cp -f named.rfc1912.zones/named.rfc1912.zones /etc/named.rfc1912.zones')
os.system('cp -a -f named/* /var/named')
os.system('cp -f named.conf /etc/named.conf')

os.system('setenforce 0')
os.system("sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config")
os.system('service named start')
