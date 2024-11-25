import mysql.connector

class Config:
  DEBUG = True
  
class Database:
  def connect_to_database():
      conn = mysql.connector.connect(
          host='127.0.0.1',
          user='root',
          password='',
          database='blog_app'
      )
      return conn
