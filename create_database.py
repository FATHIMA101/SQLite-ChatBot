import sqlite3

DB_PATH = "database.db"

# Connect to (or create) the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Drop tables if they already exist (to avoid duplicates)
cursor.execute("DROP TABLE IF EXISTS Employees;")
cursor.execute("DROP TABLE IF EXISTS Departments;")

# Create Employees table
cursor.execute("""
    CREATE TABLE Employees (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date TEXT NOT NULL
    );
""")

# Insert sample data into Employees table
employees_data = [
    (1, "Alice", "Sales", 50000, "2021-01-15"),
    (2, "Bob", "Engineering", 70000, "2020-06-10"),
    (3, "Charlie", "Marketing", 60000, "2022-03-20"),
]

cursor.executemany("INSERT INTO Employees VALUES (?, ?, ?, ?, ?);", employees_data)

# Create Departments table
cursor.execute("""
    CREATE TABLE Departments (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    );
""")

# Insert sample data into Departments table
departments_data = [
    (1, "Sales", "Alice"),
    (2, "Engineering", "Bob"),
    (3, "Marketing", "Charlie"),
]

cursor.executemany("INSERT INTO Departments VALUES (?, ?, ?);", departments_data)

# Commit and close the connection
conn.commit()
conn.close()

print("✅ Database created successfully: database.db")
