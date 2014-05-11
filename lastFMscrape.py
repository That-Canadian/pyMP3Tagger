#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import string
import sys



class LastFMScraper:
    
    urlFormat = "http://ws.audioscrobbler.com/2.0/?method={0}&track={1}&artist={2}&album={3}&limit={4}&api_key={5}&format=json"
    urlFormatID = "http://ws.audioscrobbler.com/2.0/?method={0}&mbid={1}&api_key={2}&format=json"
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.urlFormat = self.urlFormat.format('{0}','{1}','{2}','{3}','{4}',api_key)
        self.urlFormatID = self.urlFormatID.format('{0}','{1}',api_key)
        
    def _request(self, method, id=None, track=None, artist=None, album=None,limit=10):
        if track==None :
            track=''
        if artist==None :
            artist=''
        if album==None :
            album=''
        #If we have the mbid, we just use the urlID format to get info
        if id==None :
            url = self.urlFormat.format(method, track, artist, album, limit)
        else :
            url = self.urlFormatID.format(method,id)
            
        return requests.get(url)
        
    def getTrack(self, track, artist=None, album=None):
        r = self._request('track.search', None,track, artist, album,1) #1 result per page, for now
         #should check r.status_code for 200
         #Make sure we actually got a match back
        if r.json()['results']['trackmatches'] != '\n':
            tID = r.json()['results']['trackmatches']['track']['mbid']
        else:
            return None
        
        if tID == '' : return None #if we didnt get a mbid, sometimes happens from lastFM for remixed/re-did tracks
        
        r = self._request('track.getInfo',tID)
        tData = r.json()['track']
        #get the track, artist, and album
        if(r.status_code==200):
            alID = tData['album']['mbid'] #Album mbid
            arID = tData['artist']['mbid'] #Artist mbid
        else:
            return -1 #URL error
        
        r = self._request('album.getInfo', alID) #Get album json page
        
        if(r.status_code == 200): #Now get the album json info
            alData = r.json()['album']
        else:
            return -1 #URL error
            
        r = self._request('artist.getInfo', arID) #Get artist json page
        
        if(r.status_code == 200): #Now get the artist json info
            arData = r.json()['artist']
        else:
            return -1 #URL error
        
        tmpArt = Artist(arData['name'], arID)
        
        #image exists at alData['image'][1]['#text'] for medium size, implement later
        tmpAlb = Album(alData['name'], tmpArt, alData['releasedate'], alID)
        
        
        return Track(tData['name'], tmpArt, tmpAlb, tID) #will be re-written, testing for now
    
class Track:

    def __init__(self, title, artist, album, id):
        self.title = title
        self.artist = artist
        self.album = album
        self.id = id
        
    #string method, for debugging
    def __str__(self):
        return "Title: %s\nArtist: %s\n%s\nMBID: %s" % (self.title, self.artist.name, self.album, self.id)
        
class Artist:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

        
class Album:        
        
        #image exists at alData['image'][1]['#text'] for medium size
        def __init__(self, title, artist, year, id): #add image later
            self.title = title
            self.artist = artist
            #below removes everything past the first comma, and strips the leading and trailing whitespace from the year, if present
            self.year = year.split(',', 1)[0].strip()
            self.id = id
        def __str__(self):
            return "Album: %s\nYear: %s" % (self.title, self.year)
            
def main(argv): #main function, to be called if __name__ == __main__, takes in arguments argv
    if len(argv) < 3:
        sys.stderr.write('Usage: %s "Artist" "Song Name"' % argv[0])
        return 1
    
    scraper = LastFMScraper('416629e370d22d15a6f484fce67b3d9e')
    
    track = scraper.getTrack(argv[2], argv[1])
    print "\nTrack Info : \n"
    print track
    
    
if __name__ == '__main__' : sys.exit(main(sys.argv)) #calls main then exits