import logging

# Определяем свой фильтр, наследуясь от класса logging.Filter
class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()
        
         
    
# Создаем логгер
logger = logging.getLogger(__name__)

# Создаем обработчик, который будет использовать наш фильтр
stderr_handler = logging.StreamHandler()

stderr_handler = logging.StreamHandler()

# подключаем фильтр к обработчику
stderr_handler.addFilter(ErrorLogFilter())

logger.addHandler(stderr_handler)

logger.warning('Это важное предупреждение!')
logger.error('Важно! Это ошибка!')
logger.critical('Это критическая ошибка!')
logger.info('Это информация!')