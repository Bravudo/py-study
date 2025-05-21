import asyncio
import time


async def download(tamanho, url):
    start = time.time()

    t = await tempo(tamanho)

    print('-----DOWNLOAD-----')
    print(f'Iniciando Download: {url}')
    print(f'Tempo Estimado: {t:.0f}s')

    await asyncio.sleep(t)
    print(f'----------\nDownalod: {url}: Concluido')

async def tempo(c):
    
    a = 1 #tamanho do arquivo
    b = 2 #tempo por tamanho
    d = b * c / a

    return d

async def DownloadFinal():
    
    arquivo1 = 2
    arquivo1name = 'PesadãoGames.png'
    task = asyncio.create_task(download(arquivo1, arquivo1name))
    arquivo2 = 4
    arquivo2name = 'Hack.virus.legal.exe'
    task2 = asyncio.create_task(download(arquivo2, arquivo2name))

    await task
    await task2

asyncio.run(DownloadFinal())