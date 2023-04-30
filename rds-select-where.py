import mysql.connector

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "test/MySql"
    region_name = "ap-northeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    
    # Parse the secret JSON object
    secret_dict = json.loads(secret)
    username = secret_dict['username']
    password = secret_dict['password']
    host = secret_dict['host']
    port = secret_dict['port']
    database = secret_dict['database']

    # Your code goes here.

# Connect to the RDS MySQL database
db = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=database
)

# Read the input value from a file
getsecret()
with open('/path/to/input/file.txt', 'r') as f:
    id = f.read().strip()

# Execute a SELECT query with WHERE clause
cursor = db.cursor()
query = f"SELECT * FROM training_students WHERE id = {id}"
cursor.execute(query)

# Write the results to a file
with open('output.txt', 'w') as f:
    for row in cursor:
        f.write(str(row) + '\n')

# Close the database connection
db.close()
