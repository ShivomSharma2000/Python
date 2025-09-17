import json

file_name = 'youtube.txt'

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)                 # In load, we are getting/load the data from mentioned file.
    except FileNotFoundError:
        return []

# Helper function 
def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)                     # In dump, we have 2 arguments dump(which file/data, where to dump/add)

def list_all_videos(videos):
    # In videos, we haven't indexes so for printing or use index we have to use 'enumerate' function which is used for putting
    #  indexes and it's useful when we have to updated the video there we should have indexes for updating the data.
    print("\n")
    print("*" * 70)
    
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video details")
        print("4. Delete a Youtube video")
        print("5. Exist the app")
        choice = input("Enter your choice")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")


# It means, if function name (denoted by __name__) is equals to 'main' function name then runs the main() function.
if __name__ == "__main__":
    main()