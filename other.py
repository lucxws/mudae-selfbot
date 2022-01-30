"""
Adicione aqui, o que você quer que o selfbot pegue.
"""

from data import MudaeData
from asyncio import run

async def main():
    mde = MudaeData('database.db')
    char = 'Goku'
    serie = 'Naruto'
    await mde.save_chars(char)
    await mde.save_series(serie)


run(main())