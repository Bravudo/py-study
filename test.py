import asyncio
import time

async def EsperarFila():
    print('inicio da fila')
    await asyncio.sleep(5)
    print('fim da fila')
    return time.time()

async def suaMae():
    print('Esperando o Filho pra ir Embora')
    fim_fila = await EsperarFila()
    print('Agora Vamos de Carro')

    return fim_fila

async def MaquinaDaVida():
    inicio = time.time()

    fimfila = await suaMae()
    fimfila = fimfila - inicio
    print('fim')
    fim = time.time()

    fim = fim - inicio

    inicio = inicio - inicio

    print(f' inicio {inicio:.3f}s, fimFila {fimfila:.4f}s, fimtotal {fim:.4f}s ')

asyncio.run(MaquinaDaVida())

