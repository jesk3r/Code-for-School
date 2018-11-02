import asyncio as ay
from asyncio import *

async def main ():
    while True:
        print("hello")
        await ay.sleep(1)


def ans():
    input()

if __name__ == '__main__':
    ay.run(main())
