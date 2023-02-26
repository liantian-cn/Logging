[comment]: # (Copyright 2022 github.com/liantian-cn)

[comment]: # (Released under Attribution-NonCommercial-ShareAlike 4.0 International)

[comment]: # (email liantian.me+code@gmail.com)

# Python单元测试

unittest

## 目录结构

- 新建名为`tests`的python module。
- 测试文件以`test_xxxx.py`命名。


这样当执行`python -m unittest`时候，会自动执行


 ## 测试怎么写

- 测试检查程序运行结果是否为正确结果。

- 必须`import unittest`
- 必须`unittest.TestCase`
- `TestCase`推荐以`Test`开头命名
- 每个`TestCase`下的`test method`必须以`test_开头`


## 常用test method

 `self.assertEqual(first, second, msg=None)` 
 
 检查first和second是否相等。
 
 `assertNotEqual(first, second, msg=None)` 
 
 检查不相等
 
 `assertTrue(expr, msg=None)`
 
 `assertFalse(expr, msg=None)`


`assertRaises(exception, callable, *args, **kwds)`

使用方法

```
class TestXXXX(unittest.TestCast):
    def test_xxxx(self):
        a = func(b,c)

        with self.assertRaises(ValueError):
            a = func(d,e)
        # 如果a = func(d,e)返回了ValueError则验证通过

```
  
## setUP和tearDown


setUP和tearDown会在每个method前后执行

```
class TestXXXX(unittest.TestCast):
    def setUP(self):
        pass
    def tearDown(self):
        pass


```


## setUPClass和tearDownClass


setUPClass和tearDownClass会在每个TestCast前后执行
注意必须添加 @classmethod修饰器

```
class TestXXXX(unittest.TestCast):

    @classmethod
    def setUPClass和(cls):
        pass

    @classmethod    
    def tearDownClass(self):
        pass


```


## 一些method的修饰器

`@unittest.skipIf(condition, reason)` : 跳过methods

