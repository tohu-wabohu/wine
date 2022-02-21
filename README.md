# Wine
### I don't know... Just have some wine I guess.
### One man page to rule them all!

# URLs
https://www.lisenet.com/  
https://vikyd.github.io/download-chromium-history-version/  


# MySQL

```
CREATE DATABASE my_db;
CREATE USER 'foobar'@'127.0.0.0/255.0.0.0' IDENTIFIED BY 'secret';
GRANT ALL PRIVILEGES ON mydb . * TO 'foobar'@'127.0.0.0/255.0.0.0';
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
