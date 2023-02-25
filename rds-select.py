import mysql.connector

# Connect to the RDS MySQL database
db = mysql.connector.connect(
  host="your-database-endpoint.rds.amazonaws.com",
  user="your-username",
  password="your-password",
  database="your-database-name"
)

# Execute a SELECT query
cursor = db.cursor()
query = "SELECT * FROM your-table-name"
cursor.execute(query)

# Write the results to a file
with open('output.txt', 'w') as f:
  for row in cursor:
    f.write(str(row) + '\n')

# Close the database connection
db.close()
