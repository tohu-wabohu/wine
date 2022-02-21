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
