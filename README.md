Scenario:
(every service launches on inside it's own container)
- message - writing app generates messages of 2 types (with white and black tags) and puts those into 2 different queues
- postgres has one db with 2 tables (for every queue) that you will fill with messages data
- rabbitmq obviously stores messages, queues, that we can check through the web interface
- depending on message type, the reader app will populate one of 2 tables in the
postgres database.
- adminer provide web interface for the postgres database


Usage:
- download all files using same folder structure
- docker-compose up (it launches reader, db and rabbitmq as well as web interfaces for db and rabbit)
- launch messages' sender python sender.py
- check web interfaces (db tables and message queues)
