"""
Version 0.2

UPDAT: Switched to EasyID3 implementation
REASON: signficantly easier to use

"""
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, os
import mutagen
from mutagen.easyid3 import EasyID3

class Music:
	#intialization, store variable as result of ID3() to be get/set
	def __init__(self, thesong):	#need to figure out file input
		try:
			self.song = EasyID3(thesong)			
		except mutagen.id3.error:
			self.song = EasyID3()
			self.song.save(thesong)

	"""following 5 methods are get methods retrieving values stored in ID3 tags in the already specified file"""
	#get title of song
	def getTitle(self):
		print self.song["title"]
	"""get name of artist
			*
			*TPE1 is the lead performer/soloist tag
			*
			*FUTURE IMPROVEMENTS: May add TOPE, searching for either TPE1 or original artist/performer
			*pseudo code is already present and commented out
	"""
	def getArtist(self):	# or TOPE
		print self.song["artist"]

	#get the name of the album
	def getAlbum(self):
		print self.song["album"]

	#get the track number
	def getAlbumYear(self):
		print self.song["date"]
	
	"""get the album art
	Does not currently work

	Do not use
	"""
	def getAA(self):					#returns boolean whether there is or is not album art already on the file. 
		print self.song["albumartistsort"]

	"""setTitle
			*stores the title for the already specified file
			*
			*must include name of new title in method call
			*
			*returns TRUE if write is successful"""	
	
	#newTitle is variable that stores what the title should bee
	def setTitle(self, newTitle):						
		self.song["title"] = newTitle
		self.song.save()

	"""setArtist
			*stores the name of the artist for the already specified file
			*
			*must include the name of the new artist in method call
			*
			*returns TRUE if write is successful, otherwise FALSE"""
	def setArtist(self, newArtist):
		self.song["artist"] = newArtist
		self.song.save()
	"""setAlbum
			*stores the name of the album for the already specifed file
			*
			*must include the name of the new album in method call
			*
			*returns TRUE if write is successful, otherwise FALSE
			"""
	def setAlbum(self, newAlbum):
		self.song["album"] = newAlbum
		self.song.save()

	"""setTrack
			*stores the track number song on the album for the already specifed file
			*
			*must include the name of the new track number in method call
			*
			*returns TRUE if write is successful, otherwise FALSE
			"""
	def setalbumyear(self, newyear):
		self.song["date"] = newyear
		self.song.save()
	"""currently not ready for deployment	
	
		setaa
			*stores album cover art for the already specifed file
			*
			*must include the name of the new album in method call
			*
			*returns TRUE if write is successful, otherwise FALSE
			
	def setAA(self, afile):									#afile is the variable that will store the image file
		albumcover = open(afile, 'rb').read()
		if albumcover.endswith('jpg'):
			pic = APIC(3,'image/jpeg', 3, 'Front cover', albumcover)
		elif albumcover.endswith('png'):
			pic = APIC(3,'image/png', 3, 'Front cover', albumcover)
		if song['TALB'].text[0] == newAlbum:
			return True
		else:
			return False


SIDE NOTES: NEED TO BE REMOVED BEFORE FINAL PUSH
from sys import stdin
a = Music('song.mp3')
print(a.getTitle(stdin))
"""

def main(argv):
	if len(argv) < 2:
		sys.stderr.write('Usage %s "music file"' % argv[0])
		return 1
	test = Music(argv[1])
#	test.setTitle("An song that never existed")
	test.getTitle()
	
	test.getArtist()
	test.getAlbum()
	test.getAlbumYear()
	#test.getAA()
	
if __name__ == '__main__' : 
	sys.exit(main(sys.argv)) #calls main then exits
