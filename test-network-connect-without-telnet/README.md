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