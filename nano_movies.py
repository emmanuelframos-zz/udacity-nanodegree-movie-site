import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Nano Movies</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }		
		.rating{
			margin: 0 8em;
		}
		.rating span {
			font-size: 25px;
			cursor: pointer;
			float: right;
		}
		.rating span:hover, .rating span:hover ~ span{
			color: yellow;
		}
		.movie-container{
		    margin-top: 1em;
			margin-bottom: 1em;
		}
		footer{
			background:black;
			height:90px;
			color:white;
			font-weight:bold;
			text-align:center;
			padding-top:40px;
			margin-top: 30px;
			border-top:2px solid black;
		 }	
		.popover{
		     width: 16em;
		}
		.rating-lbl{
			margin: 0;
		}
		.yellow{
			color: yellow;
		}
		.black{
			color: black;
		}
		.title{
		    font-size: 2em;
			color: white;
			font-weight: bold;
		}
		.movie-tile:hover{
			background-color: white !important;			
		}				
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });     
		// Handles the rating functionality, setting colors at the stars
		$(document).on('click', '.rating span', function(event){
			var id = parseInt($(this).attr('id').split('-')[1]);
			var movieId = parseInt($(this).attr('id').split('-')[2]);
			console.log(id);
			for (index = 1; index <= 5; index++){
				if (index <= id){
					$('#rating-'+index+'-'+movieId).addClass('yellow');
					$('#rating-'+index+'-'+movieId).removeClass('black');
				}else{
					$('#rating-'+index+'-'+movieId).addClass('black');
					$('#rating-'+index+'-'+movieId).removeClass('yellow');
				}
			}
		});
		$(document).ready(function(){
			$('[data-toggle="popover"]').popover();   
		});	
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="title" class="navbar-brand" href="#">Nano Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
   <footer>
        <div class="container">
            <p>Nano Copyright &copy; 2017, All Rights Reserved</p>            
        </div>
    </footer>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="movie-container col-md-6 col-lg-4 text-center">
	<div  class="movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
		<img src="{poster_image}" width="220" height="342">
	</div>
    <h2>{movie_title}</h2>
	<a href="#" title="Storyline" data-toggle="popover" data-trigger="focus" data-content="{storyline}">Storyline</a>
	<p class="rating-lbl">Rating</p>
	<div class="rating">
		<span id="rating-5-{movie_id}" class="glyphicon glyphicon-star"></span>
		<span id="rating-4-{movie_id}" class="glyphicon glyphicon-star"></span>
		<span id="rating-3-{movie_id}" class="glyphicon glyphicon-star"></span>
		<span id="rating-2-{movie_id}" class="glyphicon glyphicon-star"></span>
		<span id="rating-1-{movie_id}" class="glyphicon glyphicon-star"></span>
	</div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''	
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.youtube_trailer)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.youtube_trailer)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image=movie.poster_image,
            trailer_youtube_id=trailer_youtube_id,
			storyline=movie.storyline,
			movie_id=movie.id
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('nano_movies.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
