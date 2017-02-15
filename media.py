
class Video:
    """This class represents a parent class (code reusing) for Video objects, such as: Movies, Series and Documentaries."""

    def __init__(self, id, title, storyline, poster_image, youtube_trailer):
        """
        Attributes
        -----------
        id: Movie's database identificator
        title: Movie's title
        storyline: Movie's storyline
        poster_image: URL movie's of poster
        youtube_trailer: URL of movie's Youtube trailer
        """

        self.id = id
        self.title = title
        self.storyline = storyline
        self.poster_image = poster_image
        self.youtube_trailer = youtube_trailer


class Movie(Video):
    """This class is a subtype of Video, and inherit attributes from parent class."""

    def __init__(self, id, title, storyline, poster_image, youtube_trailer):
        Video.__init__(
            self,
            id,
            title,
            storyline,
            poster_image,
            youtube_trailer)
