# Docker上手Day2（smokeping）

## Day2

``` dockerfile
FROM alpine:latest


RUN  sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
&&  apk update \
&&  apk upgrade \ 
&& apk add --no-cache smokeping lighttpd ttf-opensans supervisor bind-tools gawk tcptraceroute  \
&& rm -rf /var/cache/apk/* \
&& rm -rf /var/www/localhost/htdocs/ \
&& ln -s /usr/share/webapps/smokeping /var/www/localhost/htdocs \
&& chmod 777 /var/lib/smokeping/.simg \
&& chmod u+s /usr/sbin/fping \
&& chmod 777 /var/log/lighttpd \
&& rm -f /etc/lighttpd/lighttpd.conf \
&& rm -f /etc/smokeping/config



COPY lighttpd.conf /etc/lighttpd/
COPY supervisord.conf /etc/supervisord.conf
COPY tcpping /usr/bin/
RUN chmod +x /usr/bin/tcpping

CMD ["/usr/bin/supervisord"]



VOLUME /etc/smokeping/config

EXPOSE 32080
```

遇到两个之前没遇到的问题。 1. 如果有两个进程需要启动，怎么办。
用supervisor 2. lighttpd nginx apache怎么选
本来没啥可想的，可试了一圈，搭配传统cgi （perl），还是lighttpd最好用。

生成打包，导入命令如下

    docker build --tag smokeping:2.7.3-r3 .

    docker create -p 32080:32080  -v /DATA/config/smokeping.conf:/etc/smokeping/config --restart always --name SmokePing smokeping:2.7.3-r3
    docker export SmokePing > SmokePing.2.7.3-r3.export.tar
    docker start SmokePing

    docker import SmokePing.2.7.3-r3.export.tar smokeping:2.7.3-r3
    docker create -p 32080:32080  -v /DATA/config/smokeping.conf:/etc/smokeping/config  --restart always --name SmokePing smokeping:2.7.3-r3 /usr/bin/supervisord

配置文件下载 [smokeping.docker](smokeping.docker.zip)
