import mysql.connector

# Connect to the RDS MySQL database
db = mysql.connector.connect(
    host="*****.ap-northeast-1.rds.amazonaws.com",
    user="*****",
    password="****",
    database="****"
)

# Read the input value from a file
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
