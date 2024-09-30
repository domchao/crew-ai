import sqlite3
import random
import faker


if __name__ == '__main__':

    # Step 1: Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Step 2: Generate fake data using the Faker library
    fake = faker.Faker()

    # Step 3: Insert fake data into the 'users' table
    for i in range(10000):
        customer_id = i
        name = fake.name()
        age = random.randint(18, 80)
        email = fake.email()
        # Generate a fake registration date between 1 and 5 years ago
        registration_date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')

        cursor.execute('''
            INSERT INTO users (customer_id, name, age, email, registration_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (customer_id, name, age, email, registration_date))

    # Step 4: Commit the changes
    conn.commit()

    # Step 5: Close the connection
    conn.close()

    print("Fake data inserted successfully.")
