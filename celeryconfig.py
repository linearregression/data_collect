''' Config file for Celery Daemon '''
import sys

sys.path.append('.')
sys.path.append('./tasks')

# default RabbitMQ
VHOST = '/dev.sqor.analytics'
BROKER_URL = 'amqp://sqoradmin:VFNz0n3!@devrabbitmq2.sqor.com:5672'+VHOST


CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_EXCHANGE = 'status.collect.data'
CELERY_TASK_RESULT_EXPIRES = 36000 #10 hrs
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

CELERY_ENABLE_UTC = True

CELERY_QUEUE_HA_POLICY = 'HA'
