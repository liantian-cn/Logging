[comment]: # (Copyright 2022 github.com/liantian-cn)

[comment]: # (Released under Attribution-NonCommercial-ShareAlike 4.0 International)

[comment]: # (email liantian.me+code@gmail.com)

# 使用cython将py文件编译为exe

有时候cython比pyinstaller更方便，比如用来做windows服务啥的。

首先，使用`embed`参数生成文件main.c

    cython main.py --embed -3

然后编译它：

    call "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\VsDevCmd.bat" -arch=x64 -host_arch=x64

    cl main.c /I C:\Python39\include /link C:\Python39\libs\python39.lib

然后检查依赖 ![sshot-1](sshot-1.png)
