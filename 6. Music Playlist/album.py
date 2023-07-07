class Album:
    def __init__(self, input_name):
        self.name = input_name
        self.songs = list()
        self.artist = str()

    def add_song(self, input_song):
        self.songs.append(input_song.title)
