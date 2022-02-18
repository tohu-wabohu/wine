# Wine
### I don't know... Just have some wine I guess.
### One man page to rule them all!

# MySQL

```
CREATE DATABASE mydb;
CREATE USER 'foobar'@'127.0.0.0/255.0.0.0' IDENTIFIED BY 'secret';
GRANT ALL PRIVILEGES ON mydb . * TO 'foobar'@'127.0.0.0/255.0.0.0';
FLUSH PRIVILEGES;
```

```
SELECT user, host FROM mysql.user;
```
