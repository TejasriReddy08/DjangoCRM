'''
install mysql on ur computer
https:dev.mysql.com/downl;oads/installer/
pip install mysql
pip install mysql-connector
pip install mysql-connector-python
'''

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'teja123'
)

#prepare a cursor object
cursorObject = dataBase.cursor();

#create a database
cursorObject.execute("CREATE DATABASE elderco")


