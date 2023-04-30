# 2-RDS-Python
## This program will select the required rows from RDS DB instance and write it to an output file

## pre requisite
1. Should create RDS DB and have endpoint, username & password ready  
2. Create a database, table and insert some records  
3. Should have EC2 instance running with output file directory and this python program  

## shell commands
1. sudo yum update  
2. sudo yum install python3-pip  
3. pip3 install mysql-connector-python  
4. sudo yum install mysql  
5. sudo yum install python3-boto3  
6. pip3 install pymysql  
7. Optionally you can give below mysql command to connect to mysql and run quries (instead of running in sqlelectron)  
mysql -u admin -p -h database-1.cluster-ro-clk1drfaf3ne.ap-northeast-1.rds.amazonaws.com -P 3306

## Execution
Now place the program into EC2 instance and execute the program by giving below command  
python3 rds-select.py

Now validate the output file

## Note
Make sure security group in RDS instance is open to all (0.0.0.0/0)
