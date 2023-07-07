class Artist:
    def __init__(self, input_name):
        self.name = input_name
        self.songs = list()
        self.albums = list()

    def add_song(self, input_song):
        self.songs.append(input_song.title)
        input_song.artist = self.name

    def add_album(self, input_album):
        self.albums.append(input_album.name)
        input_album.artist = self.name

    def __str__(self):
        return f"{self.name} has the following songs: {self.songs}"
