# Challange Info

Name : SQL Direct

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/303?category=1&page=1

# Writeup

The challange provides PostgreSQL server details to connect to the server and find the flag.

```bash
psql -h saturn.picoctf.net -p 54709 -U postgres pico
```

\l to list all databases.

```bash
\l
```

`
   Name    |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | Locale | ICU Rules |   Access privileges   
-----------+----------+----------+-----------------+------------+------------+--------+-----------+-----------------------
 pico      | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           |
 postgres  | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           |
 template0 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/postgres          +
           |          |          |                 |            |            |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/postgres          + 
           |          |          |                 |            |            |        |           | postgres=CTc/postgres
`

/dt to list relations

```
\dt
```

`
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | flags | table | postgres
`

```
select * from flags;
```

This will show contents of table which contains the flag.
