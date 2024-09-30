import sqlite3


if __name__ == '__main__':
    # Step 1: Connect to a SQLite database
    # This will create the database file 'example.db' if it doesn't exist
    conn = sqlite3.connect('policies.db')

    # Step 2: Create a cursor object
    cursor = conn.cursor()

    # Step 3: Create a table
    # Here, we create a simple table called 'users'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS policies (
        policy_id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        policy_type TEXT NOT NULL
    )
    ''')

    # Step 4: Commit changes (save changes)
    conn.commit()

    # Step 5: Close the connection
    conn.close()

    print("Database and table created successfully.")
