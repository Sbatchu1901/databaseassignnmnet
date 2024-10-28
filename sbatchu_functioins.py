#Developed by : Srujan
import sqlite3
import os

def create_database_file(file_name):
    try:
        conn = sqlite3.connect(file_name)
    except sqlite3.Error as e:
        print(e)
    else:
        print('Created the database file.')
        return conn

def create_rep_table(database_connection, rep_data=None):
    try:
        cursor = database_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rep (
                rep_num CHAR(2) PRIMARY KEY,
                last_name CHAR(15),
                first_name CHAR(15),
                street CHAR(15),
                city CHAR(15),
                state CHAR(2),
                zip CHAR(5),
                commission DECIMAL(7,2),
                rate DECIMAL(3,2)
            )
        ''')
        print("Rep table created successfully.")
        rep_data = [
           ('20','Srujan','Batchu','624 Randall','Grove','FL','33321',20542.50,0.05),
           ('35','Hull','Richard','532 Jackson','Sheldon','FL','33553',39216.00,0.07),
           ('65','Perez','Juan','1626 Taylor','Fillmore','FL','33336',23487.00,0.05)
        ]
        cursor.executemany('''
            INSERT INTO rep (rep_num, last_name, first_name, street, city, state, zip, commission, rate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', rep_data)
        database_connection.commit()
        print("Rep data inserted successfully.")
    except sqlite3.Error as e:
        print("Failed to create rep table:", e)




def create_customer_table(database_connection):
    try:
        cursor = database_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer (
                customer_num CHAR(3) PRIMARY KEY,
                customer_name CHAR(35) NOT NULL,
                street CHAR(15),
                city CHAR(15),
                state CHAR(2),
                zip CHAR(5),
                balance DECIMAL(8,2),
                credit_limit DECIMAL(8,2),
                rep_num CHAR(2),
                FOREIGN KEY (rep_num) REFERENCES rep(rep_num)
            )
        ''')
        print("Customer table created successfully.")
        customer_data = [
            ('148','Al''s Appliance and Sport','2837 Greenway','Fillmore','FL','33336',6550.00,7500.00,'20'),
            ('282','Brookings Direct','3827 Devon','Grove','FL','33321',431.50,10000.00,'35'),
            ('356','Ferguson''s','382  Wildwood','Northfield','FL','33146',5785.00,7500.00,'65'),
            ('408','The Everything Shop','1828 Raven','Crystal','FL','33503',5285.25,5000.00,'35'),
            ('462','Bargains Galore','3829  Central','Grove','FL','33321',3412.00,10000.00,'65'),
            ('524','Kline''s','838 Ridgeland','Fillmore','FL','33336',12762.00,15000.00,'20'),
            ('608','Johnson''s Department Store','372  Oxford','Sheldon','FL','33553',2106.00,10000.00,'65'),
            ('687','Lee''s Sport and Appliance','282 Evergreen','Altonville','FL','32543',2851.00,5000.00,'35'),
            ('725','Deerfield''s Four Seasons','282 Columbia','Sheldon','FL','33553',248.00,7500.00,'35')
        ]
        cursor.executemany('''
            INSERT INTO customer (customer_num, customer_name, street, city, state, zip, balance, credit_limit, rep_num)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', customer_data)
        database_connection.commit()
        print("Customer data inserted successfully.")
    except sqlite3.Error as e:
        print(e)
    pass


def insert_a_customer_record(database_connection):
    rep_num = input("Please enter the rep number: ")
    try:
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM rep WHERE rep_num = ?", (rep_num,))
        record = cursor.fetchone()
        if record:
            print("Rep already exists with the following details:")
            print("Rep Number: ", record[0])
            print("Last Name: ", record[1])
            print("First Name: ", record[2])
            print("Street: ", record[3])
            print("City: ", record[4])
            print("State: ", record[5])
            print("ZIP: ", record[6])
            print("Commission: ", record[7])
            print("Rate: ", record[8])
        else:
            print("No rep found with that number.")


    except sqlite3.Error as e:
        print("An error occurred:", e)
    pass
def query_rep_table(database_connection):
    rep_num = input("Please enter the rep number: ")
    try:
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM rep WHERE rep_num = ?", (rep_num,))
        record = cursor.fetchone()
        if record:
            print("Rep Record Found:")
            print("Rep Number: ", record[0])
            print("Last Name: ", record[1])
            print("First Name: ", record[2])
            print("Street: ", record[3])
            print("City: ", record[4])
            print("State: ", record[5])
            print("ZIP: ", record[6])
            print("Commission: ", record[7])
            print("Rate: ", record[8])
        else:
            print("No rep found with the number", rep_num)

    except sqlite3.Error as e:
        print("An error occurred:", e)
    pass
def update_rep_table(database_connection):
    rep_num = input("Please enter the rep number: ")

    try:
        cursor = database_connection.cursor()
        cursor.execute("""
            SELECT commission
            FROM rep
            WHERE rep_num = ?
        """, (rep_num,))
        result = cursor.fetchone()
        if result:
            current_commission = result[0]
            if 0.0 <= current_commission <= 0.20:
                print(f"Current commission is {current_commission}, which is within the [0.0, 0.20] range.")
                new_commission = float(input("Enter the new commission rate: "))
                cursor.execute("""
                    UPDATE rep
                    SET commission = ?
                    HERE rep_num = ?
                """, (new_commission, rep_num))
                database_connection.commit()
                if cursor.rowcount > 0:
                    print("Commission updated successfully.")
                else:
                    print("Update operation failed, please check the rep number and try again.")
            else:
                print(f"Current commission {current_commission} is not in the range [0.0, 0.20]. No updates made.")
        else:
            print("No rep found with that number.")
    except sqlite3.Error as e:
        print("An error occurred while updating the commission:", e)
    except ValueError:
        print("Please ensure you enter a valid number for the commission.")
    pass
def delete_customer_record(database_connection):
    customer_num = input("Please enter the customer number you want to delete: ")
    try:
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM customer WHERE customer_num = ?", (customer_num,))
        record = cursor.fetchone()

        if record:
            print("Customer record found: ", record)
            user_choice = input("Are you sure you want to delete this customer record? (yes/no): ")

            if user_choice.lower() == 'yes':
                cursor.execute("DELETE FROM customer WHERE customer_num = ?", (customer_num,))
                database_connection.commit()
                if cursor.rowcount > 0:
                    print("Customer record deleted successfully.")
                else:
                    print("No record was deleted, please check the customer number and try again.")
            else:
                print("Deletion cancelled.")
        else:
            print("No customer found with the number", customer_num)

    except sqlite3.Error as e:
        print("An error occurred while deleting the customer record:", e)
    pass
def delete_database(file_name, database_connection):
    if os.path.exists(file_name):
        try:
            database_connection.close()
            print("Database connection closed successfully.")
        except sqlite3.Error as e:
            print("Failed to close the database connection:", e)
            return
        user_choice = input("Are you sure you want to permanently delete the database file? (yes/no): ")
        if user_choice.lower() == "yes":
            try:
                os.remove(file_name)
                print("Database file deleted successfully.")
            except OSError as e:
                print("Error while deleting the database file:", e)
        else:
            print("Deletion cancelled.")
    else:
        print("Database file does not exist.")
    pass