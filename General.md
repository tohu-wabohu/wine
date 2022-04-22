# Zipping, Tarring, archiving, etc...

Tar examples:
```
tar -C /foobar_path/ -cvf foobar.tar foobar/
tar -I lz4 -cvf foobar.tar.lz4 foobar/
lz4 -d foobar.tar.lz4 | tar -xv
```

Rsync:
```
rsync -azP /foobar /destination/
```

SCP example:
```
scp -c aes128-ctr 10.0.0.1:/tmp/foobar.tar.gz .
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

mydumper, myloader examples:
```
mydumper -B foobar --triggers --events --routines --compress --rows=10000 -t 8 --trx-consistency-only \ 
  --outputdir /dump/foobar/
myloader --directory=/dump/foobar/ --queries-per-transaction=10000 --threads=8"
```

# PostgreSQL

General commands:
```
\l        - list databases
\du       - list users

CREATE USER foobar WITH SUPERUSER PASSWORD 'secret';
ALTER USER foobar WITH PASSWORD 'new_secret';
```

Backup & Restore:
```
pg_dump foobar > foobar.sql
sqpl < foobar.sql
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

Update the local list of remote branches:
```
git remote update origin --prune
```

Replace master branch with dev branch:
```
git push -f origin dev:master
```

# GPG

```
gpg -c /tmp/foobar.txt            - Encrypt with a symmetric cipher using a passphrase.
gpg /tmp/foobar.txt.gpg           - Decrypt file.
gpgconf --kill gpg-agent          - Kill GPG agnet. It will start again when it’s needed.
```

# Text Manipulations

Uncomment `deb-src` in /etc/apt/sources.list:
```
sed -i '/deb-src/s/^# //' /etc/apt/sources.list && apt update
```

Add a string after some specific line:
```
sed '/optflags=/ s/$/ --without-capabilities/g'  pure-ftpd-1.0.49/debian/rules
```
