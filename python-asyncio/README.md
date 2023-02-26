# asyncio入门

https://www.bilibili.com/video/BV1oa411b7c9/
https://www.bilibili.com/video/BV1ST4y1m7No/

* asyncio不是多线程


## coroutine object

[example_1.py](example_1.py)

```
async def main():
    print('hello')
    await  asyncio.sleep(1)
    print('hello')

coro = main()

if __name__ == '__main__':
    print(coro)
    asyncio.run(coro)


# 结果

<coroutine object main at 0x0000020E11B7C8C0>
hello
hello


```

协程（英語：coroutine）

async def 是 coroutine function，定义一个coroutine object，返回值是一个coroutine object

## 进入async模式

正常的python代码我们认为是synchronize模式

那么切换到async模式，只用asyncio.run这个函数。

## 如何在async模式下增加task

[example_2.py](example_2.py)

```
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await  say_after(1, 'hello')
    await  say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())

# 返回值

started at 13:04:13
hello
world
finished at 13:04:16

```
## 如何真async起来

这里有个问题，为什么`await say_after(1, 'hello')`和`await  say_after(2, 'world')`没有一起等。

所以..要用`asyncio.create_task`

[example_3.py](example_3.py)

```
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())

# 返回值

started at 13:05:06
hello
world
finished at 13:05:08

```

create_task把coroutine转换为task
await后面是task的时候，会跳过coroutine转换为task的过程。

## 如何拿到返回值.

[example_4.py](example_4.py)

```
async def say_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")

    ret1 = await task1
    ret2 = await task2
    print(ret1)
    print(ret2)

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())

返回值
started at 14:01:18
hello - 1
world - 2
finished at 14:01:20
```

## 减少 await

[example_5.py](example_5.py)
```
async def say_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")

    ret = await asyncio.gather(task1, task2)
    print(ret)

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
    
返回值 
started at 14:03:56
['hello - 1', 'world - 2']
finished at 14:03:58
```

gather会将coroutine转换为task

## 重点

coroutine不变成task不会被执行

