[comment]: # (Copyright 2022 github.com/liantian-cn)

[comment]: # (Released under Attribution-NonCommercial-ShareAlike 4.0 International)

[comment]: # (email liantian.me+code@gmail.com)

# Docker上手Day1（alpine-bash）


新建一个DockerFile，内容如下

``` bash
FROM alpine:latest

RUN  sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories && \
apk update && \
apk upgrade  && \
apk add --no-cache bash bash-doc bash-completion

CMD ["/bin/bash"]
```

生成这个镜像文件

``` bash
buildah bud -t alpine-bash:latest .
```

执行这个镜像，`--rm`将在退出时删除。

``` bash
podman run --rm -it alpine-bash
```
