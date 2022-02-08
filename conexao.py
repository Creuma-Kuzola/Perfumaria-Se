import psycopg2

def start_connection_db():
  connection = psycopg2.connect(
    host='localhost',
    database='perfumaria',
    user='postgres',
    password='admin'
  )

  cursor = connection.cursor()
  return (cursor,connection)

def close_connection_db(cursor, connection):
  cursor.close()
  connection.close()
    