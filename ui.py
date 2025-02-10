from playlist import like_song, create_playlist, add_song_to_playlist, load_liked_songs, load_playlist, undo
from authentication import register_user, login_user, logout_user

current_user = None

def show_login_page():
    global current_user
    print("\nWelcome to Music App")
    print ("Music created for you")
    print ("Create playlists, like songs, and get personal recommendations just for you!")
    print ("Login or Register to get started.")
    while True:
        print("\n1. Register (Create an account to start now! )")
        print("2. Login (Welcome back!)")
        print("3. Exit (Hope to see you again!)")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter you username: ")
            password = input("Enter your password: ")
            register_user(username, password)
        elif choice == "2":
            global current_user
            if not current_user:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if login_user(username, password):
                    current_user = username
                    print(f"Welcome, {current_user}!")
                    break
            else:
                print(f"Already logged in as {current_user}.")
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid option, try again.")

def show_main_menu():
    global current_user

    while True:
        print("\n--- Main Menu ---")
        print("1. Like a song")
        print("2. Create a playlist")
        print("3. Add song to playlist")
        print("4. Show liked songs")
        print("5. Show playlists")
        print("6. More Info")
        print("7. Undo last action")
        print("8. Logout")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            song = input("Enter the song (Title by Artist): ")
            like_song(song)
        elif choice == "2":
            playlist_name = input("Enter playlist name: ")
            create_playlist(playlist_name)
        elif choice == "3":
            playlist_name = input("Enter playlist name: ")
            song = input("Enter the song you want to add (Tile by Artist): ")
            add_song_to_playlist(playlist_name, song)
        elif choice == "4":
            print("Liked Songs:")
            liked_songs =  load_liked_songs()
            for song in liked_songs:
                print(f"- {song}")
        elif choice == "5":
            print("Playlists:")
            playlists = load_playlist()
            for playlist_name, songs in playlists.items():
                print(f"{playlist_name}:")
                for song in songs:
                    print(f"  - {song}")
        elif choice == "6":
            print("Liking a song improves your recommendations.")
            print("Create a playlist to save songs for easy access.")
            print("Add songs to you playlists so that you never miss out on liked songs.")
        elif choice =="7":
            undo()
        elif choice == "8":
            logout_user()
            global current_user
            current_user = None
            print("See you next time!")
            show_login_page()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

def main():
    show_login_page()
    show_main_menu()

if __name__ == "__main__":
    main()