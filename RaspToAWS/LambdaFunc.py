import boto3
import os
import sys
import logging
import pymysql



def lambda_handler(event, context):
    mybucket = 'rasmusdb'
    s3 = boto3.client('s3')

    # Getting the object:
    print("Getting S3 object...")
    response = s3.get_object(Bucket=mybucket, Key='3.txt')
    print("Done, response body:")
    tempdata = response['Body'].read().decode('utf-8')
    print(tempdata)

    # database connection
    connection = pymysql.connect(host="rasmusdb.cij27wlpxhcn.eu-central-1.rds.amazonaws.com", user="rasmuslewinsson",
                                 passwd="rasmuslewinsson", database="Climate")
    cursor = connection.cursor()

    # queries for inserting values
    insert1 = "INSERT INTO Climate(Temp) VALUES(%f);", (tempdata)

    # executing the quires
    cursor.execute(insert1)

    # commiting the connection then closing it.
    connection.commit()
    connection.close()

    return 'lambda'