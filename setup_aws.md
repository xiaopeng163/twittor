# setup on AWS

## install docker

https://docs.docker.com/install/linux/docker-ce/ubuntu/


## use docker without sudo

```
sudo usermod -aG docker ubuntu
sudo systemctl restart docker
```

```
ubuntu@ip-172-31-30-137:~$ docker version
Client:
 Version:           18.09.3
 API version:       1.39
 Go version:        go1.10.8
 Git commit:        774a1f4
 Built:             Thu Feb 28 06:53:11 2019
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          18.09.3
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.8
  Git commit:       774a1f4
  Built:            Thu Feb 28 05:59:55 2019
  OS/Arch:          linux/amd64
  Experimental:     false
```

## start mysql

```
docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
```

create database

```
CREATE DATABASE twittor CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
