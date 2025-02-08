import sqlite3
import re
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Database Path
DB_PATH = "database.db"

# Flask App Setup
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Function to extract table schema (columns) dynamically
def get_table_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    schema = {}
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name})")
        schema[table_name] = [row[1] for row in cursor.fetchall()]  # Extract column names

    conn.close()
    return schema

# Get the schema on startup
TABLE_SCHEMA = get_table_schema()

# Function to generate SQL dynamically
def generate_sql_dynamic(user_query):
    user_query = user_query.lower()

    # Check if the query is about employees
    if "employees" in user_query:
        sql = "SELECT * FROM Employees"

        # Check for department filter
        match = re.search(r"in the (\w+) department", user_query)
        if match:
            department = match.group(1).capitalize()
            sql += f" WHERE Department = '{department}'"

        # Check for hiring date filter
        match = re.search(r"hired after (\d{4}-\d{2}-\d{2})", user_query)
        if match:
            date = match.group(1)
            sql += f" AND Hire_Date > '{date}'" if "WHERE" in sql else f" WHERE Hire_Date > '{date}'"

        return sql

    # Check if the query is about managers
    if "manager" in user_query:
        match = re.search(r"manager of the (\w+) department", user_query)
        if match:
            department = match.group(1).capitalize()
            return f"SELECT Manager FROM Departments WHERE Name = '{department}'"

    # Check for salary expense
    if "salary expense" in user_query:
        match = re.search(r"salary expense for the (\w+) department", user_query)
        if match:
            department = match.group(1).capitalize()
            return f"SELECT SUM(Salary) FROM Employees WHERE Department = '{department}'"

    # Count employees
    if "how many employees" in user_query:
        return "SELECT COUNT(*) FROM Employees"

    # Get all departments
    if "list all departments" in user_query:
        return "SELECT Name FROM Departments"

    return None  # If no match found

# Function to execute SQL queries
def execute_sql(sql):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return results if results else "No results found."

# Flask API Route
@app.route("/query", methods=["POST"])
def chat():
    data = request.get_json()
    user_query = data.get("query", "")

    # Generate SQL dynamically
    sql_query = generate_sql_dynamic(user_query)

    if sql_query:
        result = execute_sql(sql_query)
        return jsonify({"response": result})
    else:
        return jsonify({"response": "Sorry, I didn't understand your query."}), 400

# Serve the UI
@app.route("/")
def index():
    return render_template("index.html")

# Start the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
