import json, datetime, time, logging
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
from boto import connect_dynamodb as DynoConn
from boto.dynamodb2.exceptions import *
from boto.dynamodb.condition import *

__all__ = ['get_table_or_create', 'store_handle', 'get_handle']

#__all__ = ['query_user_stats', 'query_account_sqor']

worker_schema=[HashKey('handle', data_type=STRING), RangeKey('follower_count')]
worker_throughput {'read':10, 'write': 10}]
#worker_indexes = [AllIndex('EverythingIndex', parts=[HashKey('handle', data_type=NUMBER), ]
worker_indexes = []

def create_table(handle_table, conn):
    if handle_table:
 	Table.create(handle_table, schema=worker_schema,throughput=worker_throughput, indexes=worker_indexes)
    else:
        raise ValueError(str(handle_table)+' cannot be empty string')

def get_table(handle_table, conn):
     
    

def store_handle(file_name, conn):


def get_table_or_create(handle_table):
    


def get_handle():






def bulk_get_handle():






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
    access_id = os.getenv('aws_access_key_id'.upper())
    access_key = os.getenv('aws_secret_access_key'.upper())
    with DynoConn(aws_access_key_id=access_id, aws_secret_access_key=access_key) as conn:
        return conn

def seconds_from_epoch(x):
    x_dt = datetime.datetime.strptime(x, "%Y-%m-%d")  
    return (x_dt - datetime.datetime(1972, 1, 1)).total_seconds()



   
