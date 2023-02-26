[comment]: # (Copyright 2022 github.com/liantian-cn)

[comment]: # (Released under Attribution-NonCommercial-ShareAlike 4.0 International)

[comment]: # (email liantian.me+code@gmail.com)

# python的atexit永远好使么?

https://docs.python.org/zh-cn/3/library/atexit.html

结论

不管是正常执行，还是raise exception，都会正常执行。

但是

被kill了就不会。

比如

os._exit(0)