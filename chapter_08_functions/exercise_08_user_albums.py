
def make_album(artist, album, songs=None):
    result = {
        "artist": artist,
        "album": album
    }
    if songs:
        result["no_of_songs"] = songs
    return result


while True:
    print(f"Create a new album. Enter 'q' anytime to quit the program.")

    new_artist = input("Artist: ")
    if new_artist == 'q':
        break

    new_album = input("Album: ")
    if new_album == 'q':
        break

    new_songs = input("Songs (optional): ")
    if new_songs:
        if new_songs == 'q':
            break
        else:
            print(make_album(new_album, new_artist, int(new_songs)))
    else:
        print(make_album(new_album, new_artist))
