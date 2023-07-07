class Playlist:
    def __init__(self, input_name):
        self.name = input_name
        self.songs = list()

    def add_song(self, input_song):
        self.songs += input_song

    def __str__(self):
        return f"This playlist has the following songs: {self.songs}"
