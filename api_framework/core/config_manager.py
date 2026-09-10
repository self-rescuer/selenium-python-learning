import json
import os

class ConfigManager:
    def __init__(self,config_file='config.json'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_dir = os.path.join(os.path.dirname(current_dir),'config')
        config_path = os.path.join(config_dir,config_file)

        with open(config_path,'r')as f:
            self.config=json.load(f)


    def get(self,key,default=None):
        keys=key.split('.')
        value=self.config
        for k in keys:
            if isinstance(value,dict) and k in value:
                value=value[k]
            else:
                return default
        return value

    @property
    def base_url(self):
        return self.config['base_url']

    @property
    def timeout(self):
        return self.config.get('timeout',10)

    @property
    def headers(self):
        return self.config.get('headers',{})




