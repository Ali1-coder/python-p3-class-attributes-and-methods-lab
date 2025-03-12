class Song:

    all=[]
    count=0
    artists=set()
    genres=set()
    genre_count={}
    artist_count={}

    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        

        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)
        
    
    @classmethod
    def add_song_to_count(cls,song):
        cls.all.append(song)
        cls.count +=1

    @classmethod
    def add_to_genres(cls,song):
        cls.genres.add(song.genre)

    @classmethod
    def add_to_artists(cls,song):
        cls.artists.add(song.artist)

    @classmethod
    def add_to_genre_count(cls,song):
        if song.genre in Song.genre_count:
            Song.genre_count[song.genre] +=1
        else:
            Song.genre_count[song.genre] = 1

    @classmethod
    def add_to_artist_count(cls,song):
        if song.artist in Song.artist_count:
            Song.artist_count[song.artist] +=1
        else:
            Song.artist_count[song.artist] =1