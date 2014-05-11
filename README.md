pyMP3Tagger
===========

Final project for UNIX class, scrapes missing MP3 tags from Last.fm, takes in a single MP3 file
or folder/directory, and goes through all files. (Final functionality still in progress)

<more>
Dependencies:
Requests - http://docs.python-requests.org/en/latest/#

Mutagen - https://pypi.python.org/pypi/mutagen/1.22

Usage:

lastFMscrape.py : This file may be ran standalone taking in 2 command line arguments, artist name, then song, both surrounded in double quotes
it will then print to console the track information.
Ex:
python lastFMscrape.py "Artist" "Song"

mp3tag.py: This file may be ran standalone initializing a class taking in the file name. Methods can then be
run requesting various ID3 tags. Set methods can also be run to set these methods.
Current deployment in mp3tag: mp3tag.py can read the title, artist, album, release year
CURRENT EXAMPLE: 
$ ./mp3tag.py song.mp3
[u'songtitle']
[u'artistname']
[u'albumname']
[u'albumyear']
