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

# HDD/SSD/...

## Wipe SSD disk

Just to be on a safe side, we'll erase data in three different ways:
```
dd if=/dev/urandom of=/dev/nvmeX bs=1M status=progress
dd if=/dev/zero    of=/dev/nvmeX bs=1M status=progress
blkdiscard -s /dev/nvmeX
```

# MySQL

Get size of MySQL databases:
```
SELECT table_schema "mydb",
        ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB"
FROM information_schema.tables
GROUP BY table_schema;
```

## Backuping & restoring MySQL

mysqldump example:
```
mysqldump --quick --master-data --single-transaction foobar | lz4  > /dump/foobar.sql.lz4
```

xtrabackup example:
```
xtrabackup --backup --stream=xbstream --compress --target-dir=./ > /dump/foobar.xbstream
```

# Git

Delete git history:
```
git checkout --orphan tmp
git add -A
git commit -am "init"
git branch -D main
git branch -m main
git push -f origin main
```

Quick add, commit, push:
```
git add -A; git commit -m "up"; git push
git add -A; git commit -m "up"; git push --force-with-lease    # after branch rebase
```

Delete branches:
```
git branch -d localBranchName                    # delete branch locally
git push origin --delete remoteBranchName        # delete branch remotely
```

# IPv6

Disable IPv6:
```
# vi /etc/default/grub
GRUB_CMDLINE_LINUX="ipv6.disable=1"
GRUB_CMDLINE_LINUX_DEFAULT="ipv6.disable=1"

update-grub
```
