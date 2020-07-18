class Database:
    def __init__(self):
        pass
    
    @classmethod
    async def create(cls, name):
        raise NotImplementedError

    async def delete(self):
        raise NotImplementedError

    def __getattr__(self, key):
        """ Get Table """
        raise NotImplementedError