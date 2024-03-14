import requests
import sqlite3

def main():
    api_url = 'https://gitlab.boon.com.au/api/v4/groups'  
    private_token = 'LWfzVvArNyraXE1s5nJW'
    data = fetch_data_from_api(api_url, private_token) 
    print(data)  
    if data:
        create_database_table()
        insert_data_into_db(data)
        print("Data inserted into database successfully.")
    else:
        print("No data fetched from the API.")

def fetch_data_from_api(api_url, token):
    headers = {'Private-Token': token}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API")
        return None

def create_database_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS api_data 
                      (id INTEGER PRIMARY KEY, key TEXT, value TEXT)''')
    conn.commit()
    conn.close()

def insert_data_into_db(data):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    for item in data:
        
        cursor.execute("SELECT id FROM api_data WHERE id=?", (item['id'],))
        existing_id = cursor.fetchone()
        if existing_id:
            print(f"ID {item['id']} already exists in the database. Skipping insertion.")
        else:
        
            cursor.execute("INSERT INTO api_data (id, name) VALUES (?, ?)", (item['id'], item['name']))
    conn.commit()
    conn.close()
    
def print_data_from_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM api_data")

    rows = cursor.fetchall()

 
    for row in rows:
        print(row)

    conn.close()
print_data_from_db()


if __name__ == "__main__":
    main()


