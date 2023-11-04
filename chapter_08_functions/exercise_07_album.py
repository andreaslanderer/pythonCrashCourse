
def make_album(artist, album, songs=None):
    """Creates an album dictionary object"""
    album_object = {
        "artist": artist,
        "album": album
    }
    if songs:
        album_object["no_of_songs"] = songs
    return album_object


print(make_album("Guns n' Roses", "Appetite for Destruction"))
print(make_album("Michael Jackson", "Dangerous", 17))
