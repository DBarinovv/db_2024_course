import pymonetdb
connection = pymonetdb.connect(username="monetdb", password="monetdb", hostname="localhost", database="demo")

cursor = connection.cursor()
cursor.execute("EXPLAIN SELECT * FROM products WHERE price > 100;")
print(cursor.fetchall())
