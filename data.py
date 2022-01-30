import aiosqlite as sql
import typing as typ


class MudaeData:
    """
    This class is used to store the data from Mudae Cheat.
    """
    def __init__(self, database_file: str):
        """
        Argumentos:
            ``database_file``: Caminho para o arquivo de banco de dados.    
        """
        self.database_file = database_file
        self.tables = {'chars': 'mudae_personagens', 'series': 'mudae_series', 'likes_kakras': 'mudae_filter'}
    
    async def start_connection(self) -> sql.Cursor:
        """
        Inicia a conexão com o banco de dados.
        """
        self.conn = await sql.connect(self.database_file)
        self.cursor = await self.conn.cursor()
        return self.cursor

    async def close_connection(self) -> None:
        """
        Fecha a conexão com o banco de dados.
        """
        await self.conn.close()


    async def save_chars(self, chars: str)-> None:
        """
        Salva os personagens no banco de dados.
        """
        self.cursor = await self.start_connection()
        await self.cursor.execute(f'INSERT INTO {self.tables["chars"]} (name) VALUES (?)', (chars,))
        await self.conn.commit()

    async def save_series(self, series: str) -> None:
        """
        Salva as séries no banco de dados.
        """
        self.cursor = await self.start_connection()
        await self.cursor.execute(f'INSERT INTO {self.tables["series"]} (name) VALUES (?)', (series,))
        await self.conn.commit()

    async def save_filtering(self, priority: str, kakeras: int, likes: int) -> None:
        """
        Salva os filtros no banco de dados.
        """
        self.cursor = await self.start_connection()
        await self.cursor.execute(f'INSERT INTO {self.tables["likes_kakras"]} (priority, kakeras, likes) VALUES (?, ?, ?)', (priority, kakeras, likes))
        await self.conn.commit()
    
    async def get_chars(self) -> typ.List[str]:
        """
        Retorna os personagens do banco de dados.
        """
        self.cursor = await self.start_connection()
        await self.cursor.execute(f'SELECT name FROM {self.tables["chars"]}')
        return [char[0] for char in await self.cursor.fetchall()]
    
    async def get_series(self) -> typ.List[str]:
        """
        Retorna as séries do banco de dados.
        """
        self.cursor = await self.start_connection()
        await self.cursor.execute(f'SELECT name FROM {self.tables["series"]}')
        return [serie[0] for serie in await self.cursor.fetchall()]
    
    async def get_filtering(self) -> typ.List[typ.Tuple[str, int, int]]:
        """
        Retorna os filtros do banco de dados.
        """
        self.cursor = await self.start_connection()
        await self.cursor.execute(f'SELECT priority, kakeras, likes FROM {self.tables["likes_kakras"]} ORDER BY priority ASC')
        return await self.cursor.fetchall()
    
    


    