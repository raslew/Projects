#!/usr/bin/python
import rds_config
import boto3
import os
import sys
import logging
import pymysql

rds_host  = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")

def lambda_handler(event, context):
    """
    This function inserts content into mysql RDS instance
    """
    mybucket = 'rasmusdb'
    s3 = boto3.client('s3')

    # Getting the object:
    print("Getting S3 object...")
    response = s3.get_object(Bucket=mybucket, Key='3.txt')
    print("Done, response body:")
    tempdata = response['Body'].read().decode('utf-8')
    print(tempdata)

    item_count = 0

    with conn.cursor() as cur:
        cur.execute('insert into Climate (Sensor, Temp) values(tempdata)')
        conn.commit()
        cur.execute("select * from Climate")
        for row in cur:
            item_count += 1
            logger.info(row)

    conn.close()

    return "Added %d items to RDS MySQL table" %(item_count)