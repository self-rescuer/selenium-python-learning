import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config_manager import ConfigManager
config = ConfigManager()

print('baseurl:',config.base_url)
print('headers:',config.headers)
print('timeout:',config.timeout)
print('Accept:',config.get("headers.Accept"))
print('不存在的键:',config.get("not_exist","默认值"))