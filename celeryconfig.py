# config file for Celery Daemon

# default RabbitMQ 
BROKER_URL = 'amqp://sqoradmin:VFNz0n3!@devrabbitmq2.sqor.com:5672'
CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_EXCHANGE = 'status.collect.data'
CELERY_TASK_RESULT_EXPIRES = 36000 #10 hrs
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']

