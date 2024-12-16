import os
from dataclasses import dataclass


@dataclass
class Database(object):
    
    login: str = None
    password: str = None
    
    def drop(self):
        os.system('./dropdb_script.sh')
    
    def check(self):
        return self.login == 'postgres' and self.password == '1234'
