pyMP3Tagger
===========

Final project for UNIX class, scrapes missing MP3 tags from Last.fm, takes in a single MP3 file
or folder/directory, and goes through all files.

<more>
Dependencies:
Requests - http://docs.python-requests.org/en/latest/#
Mutagen - https://pypi.python.org/pypi/mutagen/1.22


Usage:

lastFMscrape.py : This file may be ran standalone taking in 2 command line arguments, artist name, then song, both surrounded in double quotes
it will then print to console the track information.

mp3tag.py: This file may be ran standalone initializing a class taking in the file name. Methods can then be
run requesting various ID3 tags. Set methods can also be run to set these methods.

Current GET deployment: mp3tag.py can read the title, artist, album, track number, and album cover art
Current SET deployment: mp3tag.py can set the title, artist, album, track number but setting album cover art is
NOT READY
