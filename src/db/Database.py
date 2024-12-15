import os
from dataclasses import dataclass


@dataclass
class Database(object):
    
    login: str = None
    password: str = None
    
    def drop(self):
        if self.login == 'postgres' and self.password == '1234':
            os.system('./dropdb_script.sh')
            return True
        return False
