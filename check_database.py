import sqlite3

connection = sqlite3.connect("database/telemetry.db")

cursor = connection.cursor()

tables = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

print("Tables:", tables)

rows = cursor.execute(
    "SELECT * FROM telemetry"
).fetchall()

print("Rows:")

for row in rows:
    print(row)

connection.close()