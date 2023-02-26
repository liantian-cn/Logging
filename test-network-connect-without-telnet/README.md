[comment]: # (Copyright 2022 github.com/liantian-cn)

[comment]: # (Released under Attribution-NonCommercial-ShareAlike 4.0 International)

[comment]: # (email liantian.me+code@gmail.com)

# 不使用telnet测试网络连通性

## 用/dev/tcp

    cat < /dev/tcp/8.8.8.8/443

## 用ncat

    nc -zv 8.8.8.8 443

## 用curl / wget

    wget http://8.8.8.8:443
    curl -H http://8.8.8.8:443

## Powershell

    tnc <TargetMachine> -port <PortNumber>