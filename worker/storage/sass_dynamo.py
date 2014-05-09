import api
import json, datetime, time

from api import flask_app

import boto.dynamodb2

from boto.dynamodb2 import exceptions, items 
from boto.dynamodb2.fields import (HashKey, RangeKey,
                                   KeysOnlyIndex, AllIndex, IncludeIndex,
                                   GlobalAllIndex, GlobalKeysOnlyIndex,
                                   GlobalIncludeIndex)

from boto.dynamodb2.table import Table
from boto.dynamodb2.types import (STRING, NUMBER, BINARY,
                                  STRING_SET, NUMBER_SET, BINARY_SET,
                                  QUERY_OPERATORS, FILTER_OPERATORS)
from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.exceptions import *
from boto.dynamodb.condition import *

__all__ = ['query_user_stats', 'query_account_sqor']

AWS_ACCESS_KEY_ID = 'AKIAJ7IOL7OS4357ZABA'
AWS_SECRET_ACCESS_KEY = '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'

def query_user_stats(key_id, start_time, end_time):
    flask_app.logger.info("Query User Status:  key_Id:%s start_time:%s end_time:%s", key_id, start_time, end_time)
    conn = get_connection()
    userstats = conn.get_table('userstats')
    result = userstats.query(hash_key=key_id, range_key_condition=BETWEEN(start_time, end_time))
    flask_app.logger.info("Query User Status:  Items Found: %s", result._count) 
    return json.dumps(dict([(row['date'], row) for row in result]))
   
def query_account_sqor(key_id, start_time, end_time):
    flask_app.logger.info("Query User Status:  key_Id:%s start_time:%s end_time:%s", key_id, start_time, end_time)
    conn = get_connection()
    stat_table = conn.get_table('accountsqor')
    from_time = seconds_from_epoch(start_time)
    to_time = seconds_from_epoch(end_time)
    result = stat_table.query(hash_key=key_id, range_key_condition=BETWEEN(from_time, to_time))
    flask_app.logger.info("Query Account %s Sqor:  Items Found: %s", key_id, result._count) 
    return json.dumps(list([(row['id'], row) for row in result]))


def get_connection():
    return boto.connect_dynamodb(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


def seconds_from_epoch(x):
    x_dt = datetime.datetime.strptime(x, "%Y-%m-%d")  
    return (x_dt - datetime.datetime(1972, 1, 1)).total_seconds()



   
