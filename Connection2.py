import sqlite3
import URLOrganizer

conn = None
try:
    conn = sqlite3.connect('ChatbotWebsiteOrganizer.db')
    cursor = conn.cursor()
    print("Successfully Connected to SQLite.")

    topic1, url1, website_name1 = URLOrganizer.web_name()
    today1 = URLOrganizer.today_date()

    sqlite_insert_query = "INSERT INTO ChatbotWebsiteOrganizer" \
                          "(Topic, URL, Website_Name, Joining_Date)" \
                          "VALUES" \
                          "('"+topic1+"','"+url1+"','"+website_name1+"','"+today1+"');"

    count = cursor.execute(sqlite_insert_query)
    conn.commit()

    print("Record inserted successfully into ChatbotWebsiteOrganizer table.", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table.", error)

finally:
    if conn:
        conn.close()
        print("The SQLite connection is closed.")