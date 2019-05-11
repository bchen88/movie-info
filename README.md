
MovieRetrievalViaOmdbapi command line to retrieve a movie name from OMDb API

###Environment:

centOS 7.6
Python 2.7.5
docker 18.09.6

###Prerequisites:

You need to obtain your personal API key from the OMDb API website
in order to be able to use the tool. Once you have it, you
can pass it via `--apikey` argument.

### Usage:

First build docker images

    docker build -t python-movie-title .

Show docker images you just build

    docker images

### usage examples:

Show info about the movie 'Avengers: Endgame', the tool will query the movie info from http://www.omdbapi.com/ website

    docker run --rm python-movie-title --apikey xxxxxxxx -t "Avengers: Endgame"
