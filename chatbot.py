import random

data = {
    "Mf Doom": {"album": "Madvillainy", "release_date": "2004", "top_40_hits": 2, "songs": ["Accordion", "Meat Grinder", "Rhinestone Cowboy"]},
    "oasis": {"album": "Definitely Maybe", "release_date": "1994", "top_40_hits": 8, "songs": ["Wonderwall", "Supersonic", "Live Forever"]},
    "frank sinatra": {"album": "In the Wee Small Hours", "release_date": "1955", "top_40_hits": 30, "songs": ["My Way", "Night and Day", "Fly Me to the Moon"]},
    "Ray charles": {"album": "Modern Sounds in Country and Western Music", "release_date": "1962", "top_40_hits": 15, "songs": ["Hit the Road Jack", "I Can't Stop Loving You", "Georgia on My Mind"]},
    "laufey": {"album": "Typical of Me", "release_date": "2021", "top_40_hits": 1, "songs": ["Street by Street", "Magnolia", "Like the Movies"]},
    
}
def add_artist():
    artist_name = input("Enter the artist's name: ")
    album_name = input("Enter the album's name: ")
    release_date = input("Enter the album's release date (e.g. '2004'): ")
    top_40_hits = int(input("Enter the number of top 40 hits for the artist: "))
    songs = input("Enter the songs, separated by commas: ").split(',')
    songs = [song.strip() for song in songs]

    data[artist_name] = {
        "album": album_name,
        "release_date": release_date,
        "top_40_hits": top_40_hits,
        "songs": songs
    }

def chatbot():
    print("Welcome to the Music Chatbot!")
    while True:
        question = input("\nWhat would you like to know?(if you want enter [random song] for a random song) If you want to add an extra artist enter[add}(or 'exit' to quit): ").lower()
        
        if question == "exit":
            break
        
        
        if "random song" in question:
            artist = random.choice(list(data.keys()))
            song = random.choice(data[artist]['songs'])
            print(f"Here's a random song: {song} by {artist}")
            continue
        if question == "add":
            add_artist()
            print("Artist added successfully!")
            continue
        
        found = False
        for artist, info in data.items():
            if question == artist.lower():
                print(f"Artist: {artist}\nAlbum: {info['album']}\nRelease Date: {info['release_date']}\nTop 40 Hits: {info['top_40_hits']}\nSongs: {', '.join(info['songs'])}")
                found = True
                break
            elif question in info['songs']:
                print(f"Song: {question}\nArtist: {artist}\nFrom Album: {info['album']}\nRelease Date: {info['release_date']}")
                found = True
                break
            elif "release date" in question and info['album'].lower() in question:
                print(f"Album: {info['album']} was released in {info['release_date']}")
                found = True
                break
            elif "top 40 hits" in question and artist.lower() in question:
                print(f"{artist} has {info['top_40_hits']} top 40 hits.")
                found = True
                break

        if not found:
            print("Data not found or question format not recognized. Please try again.")

chatbot()
