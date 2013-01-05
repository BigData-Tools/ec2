#coding=utf-8

from ec2.conf.settings import Settings
from ec2.conf.defaults import redis_settings 

conf = Settings(defaults=redis_settings )
conf.update({
    'default':  redis_settings._Config['node@122'],
    'cache':    redis_settings._Config['node@122'],
    'local':    redis_settings._Config['local'],
    'expiredpool_timeout': 1,
})
