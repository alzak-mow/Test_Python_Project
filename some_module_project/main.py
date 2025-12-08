print(dir())
from functions import get_double_number
from data import my_dict
from classes import *
import logging

print ('Это главный модуль main.py')
new_variable: int = 15

if __name__ == '__main__':
    print('Этот код выполняется только если main.py запускается напрямую')
    print(get_double_number(100))
    print(my_dict)
    MyClass()
    print(dir())

logger = logging.getLogger()
print(logger.parent)
print(logger.level)
logger = logging.getLogger(__name__)
print(logger.parent)

logging.basicConfig(
    level=logging.DEBUG,
    format ='[%(asctime)s] #%(levelname)s-8s %(filename)s:'
    '%(lineno)d - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.debug('Debug message')