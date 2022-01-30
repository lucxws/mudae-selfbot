"""
Ainda irei atualizar esse código, arrumar diversas coisas mas por enquanto vou deixar assim!

... TO-DO:
    - Multiplos rolls (fácil mas não é meu interesse no momento).
    - Configurações personalizadas, sem precisar seguir as do config.txt
    - Verificar se o delay está sendo respeitado (estudando lógicas).
    - PokéRolls automático (já será adicionado).
    - Alguns ifs devem ser melhorados.
    - Compilar o código pra aqueles que não tem o Python instalado. (auto-py-to-exe)
    - Versão premium maybe?
    - Blacklist de servidores.
"""


"""
Adicione seriados e personagens por comandos

... Exemplo:
    >>> !add_serie Naruto
    >>> !add_char Goku
"""


from discord.ext import commands
from discord import Reaction, User
from asyncio import sleep

from mudae import MudaeUtils
from data import MudaeData



bot = commands.Bot(command_prefix="!", self_bot=True, help_command=None)
mudae = MudaeUtils(roll_emoji='insira o emoji do roll aqui')
mudae_data = MudaeData('database.db')

token = 'token de sua conta'
bot.roll = False
bot.kakera = False


@bot.event
async def on_connect():
    print(f'{bot.user} está conectado ao discord ({bot.user.id})')

@bot.event
async def on_reaction_add(reaction: Reaction, user: User):
    
    if mudae.is_roll(reaction.message, user):
        personagem, serie, kakera, likes = mudae.get_all(message=reaction.message)
        
        if personagem in await mudae_data.get_chars():
            if not bot.roll:
                print(f'[CHAR-{personagem}]')
                await reaction.message.add_reaction(reaction.emoji)
                bot.roll = True
                await sleep(3600)
            else:
                pass
        
        if serie in await mudae_data.get_series():
            if not bot.roll:
                print(f'[SÉRIE-{serie}]')
                await reaction.message.add_reaction(reaction.emoji)
                bot.roll =  True
                await sleep(3600)
                bot.roll = False

        elif kakera > 250:
            if not bot.kakera:
                print(f'[KAKERA-{kakera}]')
                await reaction.message.add_reaction(reaction.emoji)
                bot.kakera = True
                await sleep(3600)
                bot.kakera = False
            else: 
                pass

            
        
        elif likes <= 100:
            if not bot.roll:
                print(f'[LIKES-{likes}]')
                await reaction.message.add_reaction(reaction.emoji)
                bot.roll = True
                await sleep(3600)
                bot.roll = False
            else:
                pass
        else:
            pass
        
    
    elif mudae.is_kakera_roll(reaction.message):
        print(f'[KAKERA-{mudae.get_kakera(reaction.message)}-CLAIMED]')
        await reaction.message.add_reaction(reaction.emoji)





@bot.command(name="ac")
async def add_char(ctx, *, name: str = None):
    if name is None:
        await ctx.message.add_reaction('❌')
    
    if name:
        await mudae_data.save_chars(chars=name)
        await ctx.message.add_reaction('✅')
    
@bot.command(name="as")
async def add_serie(ctx, *, name: str = None):
    if name is None:
        await ctx.message.add_reaction('❌')
    
    if name:
        await mudae_data.save_series(series=name)
        await ctx.message.add_reaction('✅')




bot.run(token, bot=False)


