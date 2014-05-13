pyMP3Tagger
===========
Done in python 2.7.6 <br>
Final project for UNIX class, scrapes missing MP3 tags from Last.fm, takes in a single MP3 file
or folder/directory, and goes through all files. (Final functionality still in progress)

<more>
Dependencies:
Requests - http://docs.python-requests.org/en/latest/user/install/#install <br>
Mutagen - https://pypi.python.org/pypi/mutagen/1.22<br>

Usage:<br>
lastFMscrape.py : This file may be ran standalone taking in 2 command line arguments, artist name, then song, both surrounded in double quotes
it will then print to console the track information.<br>
Ex:<br>
python lastFMscrape.py "Artist" "Song"<br>
<br>
mp3tag.py: This file may be ran standalone initializing a class taking in the file name. Methods can then be
run requesting various ID3 tags. Set methods can also be run to set these methods.
Current deployment in mp3tag: mp3tag.py can read the title, artist, album, release year
CURRENT EXAMPLE: <br>
$ python mp3tag.py song.mp3 <br>
[u'songtitle'] <br>
[u'artistname'] <br>
[u'albumname'] <br>
[u'albumyear']
