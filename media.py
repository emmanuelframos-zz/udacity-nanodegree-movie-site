class Video():

    def __init__(self, id, title, storyline, poster_image, youtube_trailer):
        self.id = id
        self.title = title
        self.storyline = storyline
        self.poster_image = poster_image
        self.youtube_trailer = youtube_trailer

class Movie(Video):

    def __init__(self, id, title, storyline, poster_image, youtube_trailer):
        Video.__init__(self, id, title, storyline, poster_image, youtube_trailer)
