import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        sqlite_create_table_query = '''CREATE TABLE ChatbotWebsiteOrganizer (
                                        Topic TEXT,
                                        URL TEXT UNIQUE,
                                        Website_Name TEXT,
                                        Joining_Date datetime);'''

        cursor = conn.cursor()
        print("Successfully Connected to SQLite!")
        cursor.execute(sqlite_create_table_query)
        conn.commit()
        print('SQLite table created:')

        cursor.close()

    except Error as e:
        print("Error while creating a SQLite table.", e)

    finally:
        if conn:
            conn.close()
            print("SQLite connection is closed!")


if __name__ == '__main__':
    create_connection("ChatbotWebsiteOrganizer.db")