import sqlite3                          # sqlute db is inbuilt in python.

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos(): 
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    conn.commit()

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time,  video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))   # Here you have to use ',' for makes it tuple and we can make tuple like that(mandatory in sqlite if value count is one.)
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video details")
        print("4. Delete a Youtube video")
        print("5. Exist the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
             name = input("Enter video name: ")
             time = input("Enter video time: ")
             add_video(name, time)
        elif choice == '3':
             video_id = input('Enter a Video Id to update: ')
             name = input("Enter video name: ")
             time = input("Enter video time: ")
             update_video(video_id, name, time)
        elif choice == '4':
             video_id = input('Enter a Video Id to delete: ')
             delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

    conn.close()

# It means, if function name (denoted by __name__) is equals to 'main' function name then runs the main() function.
if __name__ == "__main__":
    main()