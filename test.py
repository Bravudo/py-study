import asyncio
import time


async def timer():
    start = time.time()
    print(f'Iniciando: {time.time() - start:.2f}s')

    await asyncio.sleep(3)
    print(f'Se passaram {time.time() - start:.3f}s')

    await asyncio.sleep(4)

    print(f'-------\nTotal: {time.time() - start:.3f}s')

asyncio.run(timer())