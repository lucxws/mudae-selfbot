"""
Código sobre a licença MIT.
Ou seja, você pode usar, modificar e redistribuir este código fonte.
"""

import discord
import re
import typing

class MudaeUtils:
    """
    - Classe de utilidades do bot de discord, Mudae.
    --------------------------------------------------
    - Desenvolvido por Lucasbc.\n
    >>> Meu Github: 'https://github.com/Lucasbc187'
    >>> Meu Discord: Lucasbc0047 (752311109226201101)
    >>> Mudae: 'https://top.gg/bot/432610292342587392'


    - Não me responsabilizo por qualquer tipo de dano, punição, banimento, encerramento ou qualquer tipo de problema que possa causar a sua conta ou bot.
        - Tendo em mente disso, use com responsabilidade.
        - Selfbots não são permitidos pelo T.O.S do Discord.\n
            >>> Leia: 'https://support.discord.com/hc/pt-br/articles/115002192352-Contas-de-usu%C3%A1rio-automatizadas-auto-bots'

    --------------------------------------------------
    Caso queira usar em um bot comum, você deve ativar as intenções do bot antes de usar esta classe.

        - Selfbots:\n
            - pip install discord.py==1.4.1
            - bot = commands.Bot(self_bot=True)
            - bot.run(token, bot=False)
        \n
        - Bots:\n
            - intents = discord.Intents.default()
            - intents.members = True
            - intents.reactions = True
            - intents.emojis = True
            - bot = commands.Bot(intents=intents)

    """

    def __init__(self, roll_emoji: typing.Union[discord.Emoji, discord.PartialEmoji]):
        """
        Argumentos:
            ``roll_emoji``: Emoji que será usado para os rolls
                            :class:``discord.Emoji`` ou :class:``discord.PartialEmoji``

        
        - Para ver os emojis do roll:
            - No Discord use o comando da Mudae ``$cr list``

        No momento, :class:``MudaeUtils`` só é compatível com 1 emoji.
        """
        self.roll_emoji = roll_emoji
        

    def is_roll(self, message: discord.Message, user: typing.Optional[discord.User]) -> bool:
        """
        Verifica se a mensagem é um roll.

        Argumentos:
            ``message``: :class:``discord.Message``
            ``user``: :class:``discord.User``
            >>> Utilizado dentro de um evento de on_reaction_add, é opcional.
        
        Retorna:
            ``True``: Se a mensagem é um roll.
            ``False``: Se a mensagem não é um roll.
        """

        if message.embeds:
            if user is not None:
                if user.id == 432610292342587392:
                    if message.author.id == 432610292342587392:
                        if self.roll_emoji == message.reactions[0].emoji:
                            if user is not None:
                                return True
                            else:
                                return False

                    
            if user is None:
                 if message.author.id == 432610292342587392:
                    if self.roll_emoji == message.reactions[0].emoji:
                        if user is not None:
                            return True
                        else:
                            return False
                            
            
    def is_kakera_roll(self, message: discord.Message) -> bool:
        """
        Verifica se o roll possui kakera pra ser resgatado.

        Argumentos:
            ``message``: :class:``discord.Message``
        
        Retorna:
            ``True``: Se o roll possui kakera.
            ``False``: Se o roll não possui kakera.
        """
        if message.embeds:
            if message.author.id == 432610292342587392:
                if message.reactions[0].count > 1:
                    return False
                    
                elif message.reactions[0].count == 1:
                    if message.reactions[0].emoji.startswith('kaker') or message.reactions[0].emoji == 'kakera':
                        return True
                    else:
                        return False

    def get_char(self, message: discord.Message) -> str:
        """
        Retorna o personagem do roll.

        Argumentos:
            ``message``: :class:``discord.Message``
        
        Retorna:
            ``str``: Personagem do roll.
        """
        return message.embeds[0].author.name

    def get_serie(self, message: discord.Message) -> str:
        """
        Retorna a série, jogo ou tema do roll.

        Argumentos:
            ``message``: :class:``discord.Message``
        
        Retorna:
            ``str``: Série do roll.
        """
        
        description = message.embeds[0].description.splitlines()
        if len(description) > 3:
            series = description[0] + description[1]
        else:
            series = description[0]
        return series

    def get_kakera(self, message: discord.Message) -> int:
        """
        Retorna a quantia de kakeras do roll.

        Argumentos:
            ``message``: :class:``discord.Message``
        
        Retorna:
            ``int``: Quantia de kakeras do roll.
        """
      
        description = message.embeds[0].description.splitlines()[-1]
        kakera = re.sub(r'<:kakera:469835869059153940>|\*', '', description)
        return int(kakera)

    def get_likes(self, message: discord.Message) -> int:
        """
        Retorna a quantia de likes do roll.

        Argumentos:
            ``message``: :class:``discord.Message``
        
        Retorna:
            ``int``: Quantia de likes do roll.
        """
        
        description = message.embeds[0].description.splitlines()
        likes = description[-2]
        likes = re.sub(r'#|Likes:|\s', '', likes)
        return int(likes)


    def __repr__(self) -> str:
        """
        Retorna uma string com informações sobre o objeto.

        Retorna:
            ``str``: Informações sobre o objeto.
        """
        return f'MudaeUtils: roll_emoji: {self.roll_emoji}'

    def get_all(self, message: discord.Message) -> typing.Tuple[str, str, int, int]:
        """
        Retorna todos os dados do roll.

        Argumentos:
            ``message``: :class:``discord.Message``
        
        Retorna:
            ``tuple``: Dados do roll.
            >>> (personagem, serie, kakera, likes)
        """
        return self.get_char(message), self.get_serie(message), self.get_kakera(message), self.get_likes(message)