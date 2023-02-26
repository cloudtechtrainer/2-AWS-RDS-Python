import mysql.connector

# Connect to the RDS MySQL database
db = mysql.connector.connect(
    host="database-1.cluster-ro-clk1drfaf3ne.ap-northeast-1.rds.amazonaws.com",
    user="admin",
    password="Abcd1234",
    database="boopathi"
)

# Get the input value from user
name = input("Enter the name to search for: ")

# Execute a SELECT query with WHERE clause
cursor = db.cursor()
query = f"SELECT * FROM training_students WHERE name = '{name}'"
cursor.execute(query)

# Write the results to a file
with open('output.txt', 'w') as f:
    for row in cursor:
        f.write(str(row) + '\n')

# Close the database connection
db.close()
