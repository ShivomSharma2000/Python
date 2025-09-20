from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("localhost:27017")

db = client['ytmanager']
video_collection = db['videos']

print(video_collection)

def list_videos(): 
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": name, "time": time}})

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})    

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

if __name__ == "__main__":
    main()