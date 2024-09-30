import sqlite3
import random
import uuid


if __name__ == '__main__':

    policy_numbers = [i for i in range(90000, 100000, 1)]
    # Step 1: Connect to the SQLite database
    conn = sqlite3.connect('policies.db')
    cursor = conn.cursor()

    # Step 3: Insert fake data into the 'users' table
    for i in range(10000):
        policy_id = policy_numbers[i]
        customer_id = i
        policy_type = "Motor"

        cursor.execute('''
            INSERT INTO policies (policy_id, customer_id, policy_type)
            VALUES (?, ?, ?)
        ''', (policy_id, customer_id, policy_type))

    policy_numbers = [i for i in range(40000, 50000, 1)]

    for i in range(500):
        policy_id = policy_numbers[i]
        customer_id = i
        policy_type = "Pension"

        cursor.execute('''
            INSERT INTO policies (policy_id, customer_id, policy_type)
            VALUES (?, ?, ?)
        ''', (policy_id, customer_id, policy_type))

    # Step 4: Commit the changes
    conn.commit()

    # Step 5: Close the connection
    conn.close()

    print("Fake data inserted successfully.")
