# docker-blp-config
Change Docker's default IP space for Bloomberg L.P.
```
$ yum install -y docker
$ cat /etc/sysconfig/docker-network
# /etc/sysconfig/docker-network
DOCKER_NETWORK_OPTIONS=

$ yum install -y docker-blp-config
$ cat /etc/sysconfig/docker-network
# /etc/sysconfig/docker-network
DOCKER_NETWORK_OPTIONS="--bip=192.168.0.0/15"

$ service docker start
```
