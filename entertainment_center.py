import media
import nano_movies

# Instance of Interstellar movie.
interstellar = media.Movie(
    1,
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to "
    "ensure humanity's survival.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film"
    "_poster.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Instance of Batman movie.
batman = media.Movie(
    2,
    "Batman: The Dark Knight",
    "When the menace known as the Joker wreaks havoc and chaos on the people "
    "of Gotham, the caped crusader must come to terms with one of the greatest"
    " psychological tests of his ability to fight injustice.",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=5y2szViJlaY")

# Instance of Almost Famous movie.
almost_famous = media.Movie(
    3,
    "Almost famous",
    "A high-school boy is given the chance to write a story for Rolling Stone "
    "Magazine about an up-and-coming rock band as he accompanies them on their"
    " concert tour.",
    "https://upload.wikimedia.org/wikipedia/en/d/dd/Almost_famous_poster1.jpg",
    "https://www.youtube.com/watch?v=6iyp0qcf7-w")

# Instance of Star Wars movie.
star_wars = media.Movie(
    4,
    "Star Wars V",
    "After the rebels have been brutally overpowered by the Empire on their "
    "newly established base, Luke Skywalker takes advanced Jedi training with"
    " Master Yoda, while his friends are pursued by Darth Vader as part of his"
    " plan to capture Luke.",
    "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes"
    "_Back.jpg",
    "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

# Instance of Fast and Furious movie
fast_and_furious = media.Movie(
    5,
    "Fast & Furious",
    "Brian O'Conner, back working for the FBI in Los Angeles, teams up with "
    "Dominic Toretto to bring down a heroin importer by infiltrating his "
    "operation.",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/Fast_and_Furious_Poster"
    ".jpg",
    "https://www.youtube.com/watch?v=ZsJz2TJAPjw")

# Instance of Saving Private Ryan movie.
saving_private_ryan = media.Movie(
    6,
    "Saving Private Ryan",
    "Following the Normandy Landings, a group of U.S. soldiers go behind enemy"
    " lines to retrieve a paratrooper whose brothers have been killed in "
    "action.",
    "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster"
    ".jpg",
    "https://www.youtube.com/watch?v=vwAxi4A2YcY")

# List of movies that will be presented in website main page.
movies = [
    interstellar,
    batman,
    star_wars,
    almost_famous,
    fast_and_furious,
    saving_private_ryan]

# This function is used to generate the HTML file based in movies list.
# After this, the HTML file is openend in a web browser.
nano_movies.open_movies_page(movies)
