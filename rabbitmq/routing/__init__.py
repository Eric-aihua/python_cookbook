# -*- coding:utf-8 -*-
import random

from faker.providers import BaseProvider

#
class LogLevelProvider(BaseProvider):
    def log_level(self):
        log_level_list = 'debug,info,warn,error'.split(',')
        return random.choice(log_level_list)