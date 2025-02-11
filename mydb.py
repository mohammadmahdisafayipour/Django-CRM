# Install Mysql on your computer
# https://dev.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 


import mysql.connector
import pymysql

dataBase = pymysql.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = 'm77b77s77a77'
    
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done")