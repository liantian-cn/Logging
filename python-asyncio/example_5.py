# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import time


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