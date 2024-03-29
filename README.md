# Wine
### I don't know... Just have some wine I guess.
### One man page to rule them all!

# URLs
https://www.lisenet.com/  
https://vikyd.github.io/download-chromium-history-version/  

# Linux
```
find foobar/ -maxdepth 1  -type d -empty -exec ls -l {} \;
find foobar/ -maxdepth 1  -type d -not -empty -exec ls -l {} \;
```

```
ls -1                                                  # list one file per line
$(date --date="$(date +%Y-%m-15) -1 month" +'%m')      # get last month number
```

# HDD/SSD/...

### Encrypt with LUKS
```
cryptsetup luksFormat /dev/sdX
cryptsetup open /dev/sdX foobar
mkfs.ext4 /dev/mapper/foobar
cryptsetup close foobar
```

# SSL/VPN/...

## CA, server & client certs with EasyRSA

Download EasyRSA from https://github.com/OpenVPN/easy-rsa/releases

Generate new CA and signed server cert:

```
cp vars.example vars

# vi vars
#. . .
set_var EASYRSA_REQ_COUNTRY    "US"
set_var EASYRSA_REQ_PROVINCE   "NewYork"
set_var EASYRSA_REQ_CITY       "New York City"
set_var EASYRSA_REQ_ORG        "DigitalOcean"
set_var EASYRSA_REQ_EMAIL      "admin@example.com"
set_var EASYRSA_REQ_OU         "Community"
#. . .

./easyrsa init-pki
./easyrsa build-ca nopass

./easyrsa gen-req server nopass
./easyrsa sign-req server server

./easyrsa gen-dh
openvpn --genkey --secret ta.key
```

Generate new signed client cert:

```
./easyrsa gen-req client1 nopass
./easyrsa sign-req client client1
```

# Gluster
Install server
```
add-apt-repository ppa:gluster/glusterfs-10
apt update
apt install glusterfs-server

systemctl start glusterd.service
systemctl enable glusterd.service
systemctl status glusterd.service

gluster peer probe lab02
gluster peer probe lab03
gluster peer status

gluster volume create gluster_vol replica 3 lab01:/gluster01_vol lab02:/gluster01_vol lab03:/gluster01_vol force
gluster volume start gluster_vol

gluster volume add-brick gluster_vol replica 4 lab04:/gluster01_vol force
gluster volume remove-brick gluster_vol replica 3 lab03:/gluster01_vol force
gluster peer detach lab03
```
Install client
```
add-apt-repository ppa:gluster/glusterfs-10
apt update
apt install glusterfs-client
mkdir /gluster01

echo "lab01:gluster01_vol /gluster01 glusterfs defaults,_netdev 0 0" >> /etc/fstab
mount -a
```

# MySQL

```
CREATE DATABASE my_db;
CREATE USER 'foobar'@'127.0.0.0/255.0.0.0' IDENTIFIED BY 'secret';
GRANT ALL PRIVILEGES ON mydb . * TO 'foobar'@'127.0.0.0/255.0.0.0';
FLUSH PRIVILEGES;
```

```
ALTER USER 'foobar'@'localhost' IDENTIFIED BY 'new_secret';
FLUSH PRIVILEGES;
```

```
SELECT user, host FROM mysql.user;
```

### xtrabackup, xbstream examples:
```
# Backup
xtrabackup --backup --stream=xbstream --compress --target-dir=./ > /dump/foobar.xbstream

# Restore
xbstream --decompress -x -C /dump/foobar/ < /dump/foobar.xbstream
xtrabackup --prepare --target-dir=/dump/foobar/      # (2x)
```

### Replication
```
# create user for replication, edit users.sql:
-- Grants for 'repl'@'172.16.0.1'
CREATE USER IF NOT EXISTS 'repl'@'172.16.0.1';
ALTER USER 'repl'@'172.16.0.1' IDENTIFIED BY 'secret';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'repl'@'172.16.0.1';

# Create repl user:
mysql < users.sql

# On slave node enable replication:
CHANGE MASTER to MASTER_USER='repl', MASTER_PASSWORD='secret', MASTER_PORT=3306, MASTER_HOST='10.0.0.100',
MASTER_AUTO_POSITION=1, GET_MASTER_PUBLIC_KEY=1;
START SLAVE;
```

# Ansible
```
ansible-playbook _foobar.yml --tags my_tag
```

# Jinja2
```
{% if foobar is defined %}
    value of foobar: {{ foobar }}
{% else %}
    foobar is not defined
{% endif %}
```

# iptables
```
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

# KVM

Install VM:
```
virt-install --name ubuntu20.04 --memory 2048 --vcpus 2 --disk size=8 \
  --location /home/spirit/install/ubuntu-20.04.4-live-server-amd64.iso,kernel=casper/vmlinuz,initrd=casper/initrd \
  --os-variant ubuntu20.04 --graphics none --extra-args='console=ttyS0,115200n8 serial'
```

```
virsh dumpxml foobar > foobar.xml
virsh define foobar.xml

qemu-img resize mydisk.qcow2 +10G
```

```
osinfo-query os
```

### Bugs
#### Cloned VM acquires the same DHCP IP address  
https://kb.vmware.com/s/article/82229  

Add to netplan config:
```
dhcp-identifier: mac
```

# Docker
### Cheatsheet:
```
docker ps -a --filter volume=VOLUME_NAME_OR_MOUNT_POINT

docker swarm init --advertise-addr 127.0.0.1 --listen-addr 127.0.0.1 --data-path-addr 127.0.0.1
```

# BASH
### Text manipulations
```
sed -i '10d' file.txt             # delete 10th line
```

### Code Examples
```
#!/bin/bash
for i in {1..4}
do
   echo "i: $i"
done
```

# JAVA
### Code Examples
```
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
```
