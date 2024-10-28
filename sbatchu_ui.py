import sbatchu_functioins as functions
connection = None
def main():
    connection = None
    while True:
        prompt = """
                B to create the database file
                P to create rep table
                S to create customer table
                I to insert a customer record
                R to query the Rep table
                U to update the rep table
                D to delete a customer record
                X to delete the database
                Q to quit the application
                """
        choice = input("prompt")
        if choice == 'Bb':
            file_name = input('Enter the database file name: ')
            connection = functions.create_database_file(file_name)
        elif choice == 'Pp':
            if connection:
                functions.create_rep_table(connection)
                pass
            else:
                print("Database is not connected.")
        elif choice == 'Ss':
            if connection:
                functions.create_customer_table(connection)
            else:
                print("Database is not connected.")
        elif choice == 'Ii':
            if connection:
                functions.insert_a_customer_record(connection)
                pass
            else:
                print("Database is not connected.")
        elif choice == 'Rr':
            if connection:
                functions.query_rep_table(connection)
                pass
            else:
                print("Database is not connected.")
        elif choice == 'Uu':
            if connection:
                functions.update_rep_table(connection)
                pass
            else:
                print("Database is not connected.")
        elif choice == 'Dd':
            if connection:
                functions.delete_customer_record(connection)
                pass
            else:
                print("Database is not connected.")
        elif choice == 'Xx':
            if connection:
                file_name = input('Enter the database file name to delete: ')
                functions.delete_database(file_name, connection)
                connection = None
                pass
            else:
                print("Database is not connected.")
        elif choice == 'Qq':
            if connection:
                connection.close()
                print("Database connection closed successfully.")
            print("Quitting application...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
