import boto3
import json
import pymysql

import os
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAV44TXIU47BQNCZON'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

# Specify the AWS region
region = 'ap-northeast-2'

# Create a Secrets Manager client with the specified region
secrets_client = boto3.client('secretsmanager', region_name=region)

# Retrieve the secret value for your RDS database
secret = secrets_client.get_secret_value(SecretId='test/MySqlSecret')

# Parse the secret JSON string and extract the database credentials
secret_dict = json.loads(secret['SecretString'])
db_host = secret_dict['host']
db_port = secret_dict['port']
db_user = secret_dict['username']
db_pass = secret_dict['password']
db_name = secret_dict['dbname']

# Connect to the RDS database using the extracted credentials
conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass,db=db_name)

# Execute a SQL query on the database
cur = conn.cursor()
cur.execute('SELECT * FROM my_table')
results = cur.fetchall()

# Print the query results
for row in results:
    print(row)

# Close the database connection
conn.close()
