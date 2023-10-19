# Simple chatbot for searching artist, album, and song names

data = {
    "Mf Doom": {"album": "Madvillainy", "song": "Accordion"},
    "oasis": {"album": "Definitely Maybe", "song": "Wonderwall"},
    "frank sinatra": {"album": "In the Wee Small Hours", "song": "My Way"},
    "Ray charles": {"album": "Modern Sounds in Country and Western Music", "song": "Hit the Road Jack"},
    "laufey": {"album": "Typical of Me", "song": "Street by Street"},
    "the beatles": {"album": "Abbey Road", "song": "Come Together"},
    "Elton John": {"album": "Goodbye Yellow Brick Road", "song": "Rocket Man"},
    "the wallflowers": {"album": "Bringing Down the Horse", "song": "One Headlight"},
    "New radicals": {"album": "Maybe You've Been Brainwashed Too", "song": "You Get What You Give"},
    "super grass": {"album": "I Should Coco", "song": "Alright"},
    "flock of seagulls": {"album": "A Flock of Seagulls", "song": "I Ran"},
    "tv girl": {"album": "Death of a Party Girl", "song": "Lovers Rock"},
    "butthole surfers": {"album": "Locust Abortion Technician", "song": "Pepper"},
    "Jerry Lee Lewis": {"album": "Live at the Star Club, Hamburg", "song": "Great Balls of Fire"}
}

def chatbot():
    print("Welcome to the Music Chatbot!")
    while True:
        search = input("Enter artist, album, or song name (or 'exit' to quit): ").lower()
        if search == "exit":
            break
        found = False
        for artist, info in data.items():
            if search == artist.lower():
                print(f"Artist: {artist}\nAlbum: {info['album']}\nSong: {info['song']}")
                found = True
                break
            elif search == info['album'].lower() or search == info['song'].lower():
                print(f"Artist: {artist}\nAlbum: {info['album']}\nSong: {info['song']}")
                found = True
                break
        if not found:
            print("Data not found.")

chatbot()
