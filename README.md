## Учебный проект с курса "Телеграмм боты на Python" на stepik.org

### Шпаргалки


[Пример бота из курса](https://github.com/kmsint/aiogram_bot_template))

[Шпаргалка по консольным командам Git](https://github.com/cyberspacedk/Git-commands)

git remote - v 

###  Документации

[Документация aiogram](https://docs.aiogram.dev/en/dev-3.x/api/enums/content_type.html#module-aiogram.enums.content_type)


[Документация logging](https://docs.python.org/3/library/logging.html)



### Запросы

https://api.telegram.org/bot8225505028:AAHT0CziN-L1TD4OK97JixJ9OJa4Qnj4h78/getMe

https://api.telegram.org/bot8225505028:AAHT0CziN-L1TD4OK97JixJ9OJa4Qnj4h78/getUpdates

https://api.telegram.org/bot8225505028:AAHT0CziN-L1TD4OK97JixJ9OJa4Qnj4h78/sendMessage?chat_id=149469486&text=Hello%2C%20punk%21

https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=AMAZING!


### Паттерн проектирования
В шаблоне имеет смысл заложить следующие разделы:

Конфигурационные данные
Точка входа (запуск бота)
Middleware
Фильтры
Хэндлеры
Бизнес-логика
Взаимодействие с БД
Взаимодействие с внешними API
Лексикон бота (готовые тексты, которые бот будет использовать при общении с пользователями)
Клавиатуры
Состояния
Тесты
Обработчики ошибок
Утилиты

📁 aiogram_bot_template/
├── 📁 alembic/
│   ├── 📁 versinos/
│   │   ├── 1541bb8a3f26_.py
│   │   └── b20e5643d3bd_.py
│   ├── env.py
│   └── script.py.mako
├── 📁 app/
│   ├── 📁 bot/
│   │   ├── 📁 dialogs/
│   │   │   ├── 📁 flows/
│   │   │   │   ├── 📁 settings/
│   │   │   │   │   ├── dialogs.py
│   │   │   │   │   ├── getters.py
│   │   │   │   │   ├── handlers.py
│   │   │   │   │   ├── keyboards.py
│   │   │   │   │   └── states.py
│   │   │   │   ├── 📁 start/
│   │   │   │   │   ├── dialogs.py
│   │   │   │   │   ├── getters.py
│   │   │   │   │   ├── handlers.py
│   │   │   │   │   └── states.py
│   │   │   │   └── __init__.py
│   │   │   └── 📁 widgets/
│   │   │       └── i18n.py
│   │   ├── 📁 enums/
│   │   │   ├── actions.py
│   │   │   └── roles.py
│   │   ├── 📁 filters/
│   │   │   └── dialog_filters.py
│   │   ├── 📁 handlers/
│   │   │   ├── __init__.py
│   │   │   ├── commands.py
│   │   │   └── errors.py
│   │   ├── 📁 i18n/
│   │   │   └── translator_hub.py
│   │   ├── 📁 keyboards/
│   │   │   ├── links_kb.py
│   │   │   └── menu_button.py
│   │   ├── 📁 middlewares/
│   │   │   ├── database.py
│   │   │   ├── get_user.py
│   │   │   ├── i18n.py
│   │   │   └── shadow_ban.py
│   │   ├── 📁 states/
│   │   │   └── states.py
│   │   ├── __init__.py
│   │   └── bot.py
│   ├── 📁 infrastructure/
│   │   ├── 📁 cache/
│   │   │   └── connect_to_redis.py
│   │   ├── 📁 database/
│   │   │   ├── 📁 connection/
│   │   │   │   ├── base.py
│   │   │   │   ├── connect_to_pg.py
│   │   │   │   └── psycopg_connection.py
│   │   │   ├── 📁 models/
│   │   │   │   └── users.py
│   │   │   ├── 📁 query/
│   │   │   │   └── results.py
│   │   │   ├── 📁 tables/
│   │   │   │   ├── 📁 enums/
│   │   │   │   │   ├── base.py
│   │   │   │   │   └── users.py
│   │   │   │   ├── base.py
│   │   │   │   └── users.py
│   │   │   ├── 📁 views/
│   │   │   │   └── views.py
│   │   │   └── db.py
│   │   └── 📁 storage/
│   │       ├── 📁 storage/
│   │       │   └── nats_storage.py
│   │       └── nats_connect.py
│   └── 📁 services/
│       ├── 📁 delay_service/
│       │   ├── 📁 models/
│       │   │   └── delayed_messages.py
│       │   ├── consumer.py
│       │   ├── publisher.py
│       │   └── start_consumer.py
│       └── 📁 scheduler/
│           ├── taskiq_broker.py
│           └── tasks.py
├── 📁 config/
│   ├── config.py
│   └── settings.toml
├── 📁 locales/
│   ├── 📁 en/
│   │   ├── 📁 LC_MESSAGES/
│   │   │   └── txt.ftl
│   │   └── 📁 static/
│   └── 📁 ru/
│       ├── 📁 LC_MESSAGES/
│       │   └── txt.ftl
│       └── 📁 static/
├── 📁 nats_broker/
│   ├── 📁 config/
│   │   └── server.conf
│   └── 📁 migrations/
│       └── create_stream.py
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.example
├── docker-compose.yml
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock



[aiogram_bot_template by kmsint (обновляемый шаблон, которым пользуюсь я)](https://github.com/kmsint/aiogram_bot_template)

[aiogram_bot_template by Forden](https://github.com/Forden/aiogram-bot-template)

[aiogram_template by bomzheg](https://github.com/bomzheg/aiogram_template)

[Advanced User Telegram Bot by BaggerFast](https://github.com/BaggerFast/AdvancedUserTelegramBot)

[tgbot_template by Tishka17](https://github.com/Tishka17/tgbot_template)

[simple-aiogram-bot by xALEGORx](https://github.com/xALEGORx/simple-aiogram-bot)
