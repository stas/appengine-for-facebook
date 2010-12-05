import yaml
import os

class Config:
    cfile = None
    data = None
    
    def __init__(self, name):
        if not name:
            name = 'app'
        
        path = os.path.dirname(__file__)
        path = os.path.normpath(path + '/../../')
        self.cfile = os.path.join(path, name + '.yaml')
        self.load()

    def load(self):
        if os.path.isfile(self.cfile):
            self.data = yaml.load(file(self.cfile, 'r'))
    
    def id(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None