from artist import Artist
from song import Song
from album import Album
from playlist import Playlist

if __name__ == "__main__":
    rkm = Artist("RKM")
    # print(vars(rkm))

    hits = Album("Hits")
    # print(vars(hits))

    song1 = Song("Song 1", 2023)
    song2 = Song("Song 2", 2023)
    rkm.add_song(song1)
    rkm.add_song(song2)
    # print(vars(rkm))
    # print(vars(song1))
    # print(vars(song2))

    hits.add_song(song1)
    hits.add_song(song2)
    rkm.add_album(hits)
    # print(vars(hits))
    # print(vars(rkm))
    playlist1 = Playlist("Playlist 1")
    playlist1.add_song(hits.songs)
    # print(vars(playlist1))

    print(playlist1)

    print(rkm)
