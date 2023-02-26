# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


async def main():
    print('hello')
    await  asyncio.sleep(1)
    print('hello')

coro = main()

if __name__ == '__main__':
    print(coro)
    asyncio.run(coro)
