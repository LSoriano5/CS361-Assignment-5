
history = []
liked_songs = []
playlists = {}

def like_song(song):
    if song not in liked_songs:
        liked_songs.append(song)
        history.append(("Like", song))
        print(f"Liked {song}!")
        save_liked_songs()  
    else:
        print(f"{song} is already in your liked songs.")

def save_liked_songs():
    with open("liked_songs.txt", "w") as file:
        for song in liked_songs:
            file.write(f"{song}\n")

def load_liked_songs():
    try:
        with open("liked_songs.txt", "r") as file:
            liked_songs = [line.strip() for line in file.readlines()]
            return liked_songs
    except FileNotFoundError:
        liked_songs = []

def create_playlist(playlist_name):
    if playlist_name not in playlists:
        playlists[playlist_name] = []
        history.append(("create", playlist_name))
        print(f"Playlist '{playlist_name}' created.")
        save_playlists()
    else:
        print(f"Playlist '{playlist_name}' already exists.")

def save_playlists():
    with open("playlists.txt", "w") as file:
        for playlist_name, songs in playlists.items():
            file.write(f"{playlist_name}:\n")
            for song in songs:
                file.write(f"{song}\n")

def add_song_to_playlist(playlist_name, song):
    if playlist_name in playlists:
        if song in playlists[playlist_name]:
            print(f" {song} is already in '{playlist_name}'. Try again!")
        else:
            playlists[playlist_name].append(song)
            history.append(("add", (playlist_name, song)))
            print(f"Added {song} to playlist '{playlist_name}'.")
            save_playlists()
    else:
        print(f"Playlist '{playlist_name}' does not exist.")

def load_playlist():
    playlists = {}
    try:
        with open("playlists.txt", "r") as file:
            current_playlist = None
            for line in file:
                line = line.strip()
                if line.endswith(":"):  
                    current_playlist = line[:-1] 
                    playlists[current_playlist] = []
                elif current_playlist:
                    playlists[current_playlist].append(line)
    except FileNotFoundError:
        playlists = {}
    return playlists

def undo():
    if not history:
        print("No actions to undo.")
        return

    action, details = history.pop()

    if action == "like":
        if details in liked_songs:
            liked_songs.remove(details)
            save_liked_songs()
            print(f"Undo: Removed like for '{details}'")
    elif action == "add":
        playlist, song = details
        if song in playlists.get(playlist, []):
            playlists[playlist].remove(song)
            save_playlists()
            print(f"Undo: Removed '{song}' from '{playlist}'")
    elif action == "create":
        if details in playlists:
            del playlists[details]
            save_playlists()
            print(f"Undo: Deleted playlist '{details}'")