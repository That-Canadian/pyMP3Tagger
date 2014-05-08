#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from mutagen.mp3 import MP3	#I do not think I actually use this, use id3 instead
from mutagen.id3 import ID3, error, APIC
#from sys import stdin

class Music:
	#initialization, store variable as result of ID3() to be get/set
	def __init__(self, thesong):	#need to figure out file input
		self.song = ID3(thesong)
	
	"""following 5 methods are get methods retrieving values stored in ID3 tags in the already specified file"""
	#get title of song
	def getTitle(self):
		if song['TIT2'].text[0] == '':
			return "No title found"
		else:
			return song['TIT2'].text[0]	

	"""get name of artist
			*
			*TPE1 is the lead performer/soloist tag
			*
			*FUTURE IMPROVEMENTS: May add TOPE, searching for either TPE1 or original artist/performer
			*pseudo code is already present and commented out
	"""
	def getArtist(self):	# or TOPE
		if song['TPE1'].text[0] == '': #&& ( song['TOPE'].text[0] == ''):
			return None
		elif song['TPE1'].text[0] != '':
			return song['TPE1'].text[0] 
		elif song['TOPE'].text[0] != '':
			return song['TOPE'].text[0]

	#get the name of the album
	def getAlbum(self):
		if song['TALB'] == '':
			return None
		else:
			return song['TALB'].text[0]

	#get the track number
	def getTrack(self):
		if song['TRCK'].text[0] == '':
			return None
		else:
			return song['TRCK'].text[0]
	
	#get the album art
	def getAA(self):					#returns boolean whether there is or is not album art already on the file. 
		if song['APIC'].data == None:
			return False
		else:
			return True

	"""setTitle
			*stores the title for the already specified file
			*
			*must include name of new title in method call
			*
			*returns TRUE if write is successful"""	
	def setTitle(self, newTitle):						#newTitle is variable that stores what the title should bee
		#check = 0
		#if song['TIT2'].text[0] == '':
		song['TIT2'] = TIT2(3, newTitle)
		if song['TIT2'].text[0] == newTitle:
			return True
		else:
			return False
		#	check = 1
		#else:
		#	print 'This media already has a title!'
		#return check

	"""setArtist
			*stores the name of the artist for the already specified file
			*
			*must include the name of the new artist in method call
			*
			*returns TRUE if write is successful, otherwise FALSE"""
	def setArtist(self, newArtist):
		song['TPE1'] = TPE1(3, newArtist)
		if song['TPE1'].text[0] == newArtist:
			return True
		else:
			return False

	"""setAlbum
			*stores the name of the album for the already specifed file
			*
			*must include the name of the new album in method call
			*
			*returns TRUE if write is successful, otherwise FALSE
			"""
	def setAlbum(self, newAlbum):
		song['TALB'] = TALB(3, newAlbum)
		if song['TALB'].text[0] == newAlbum:
			return True
		else:
			return False


	"""setTrack
			*stores the track number song on the album for the already specifed file
			*
			*must include the name of the new track number in method call
			*
			*returns TRUE if write is successful, otherwise FALSE
			"""
	def setTrack(self, newTrack):
		song['TRCK'] = TRCK(3, newTrack)
		if song['TRCK'].text[0] == newTrack:
			return True
		else:
			return False
	
	"""CURRENTLY NOT READY FOR DEPLOYMENT	
	
		setAA
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
	test = Music(argv)

	title = test.getTitle()
	#test2 = test.getArtist()
	#test3 = test.
	print title

#if __name__ == '__main__' : sys.exit(main(sys.argv)) #calls main then exits
