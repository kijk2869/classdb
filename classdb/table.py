class Table:
    def __init__(self):
        pass
    
    @classmethod
    async def create(cls, name):
        raise NotImplementedError

    def __getattr__(self, key):
        """ select if there any key like primary """
        raise NotImplementedError

    async def insert(self, data: dict):
        raise NotImplementedError

    async def delete(self):
        raise NotImplementedError