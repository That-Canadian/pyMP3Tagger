#-*- coding: utf-8 -*-

import requests
import string

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
            id = r.json()['results']['trackmatches']['track']['mbid']
        else:
            return None
            
        r = self._request('track.getInfo',id)
        data = r.json()['track']
        
        return Track(data['name'], data['artist']['name'], data['album']['title'], id) #will be re-written, testing for now
    
class Track:

    def __init__(self, title, artist, album, id):
        self.title = title
        self.artist = artist
        self.album = album
        self.id = id
        
    #string method, for debugging
    def __str__(self):
        return "Title: %s\nArtist: %s\nAlbum: %s\nID: %s" % (self.title, self.artist, self.album, self.id)
        
class Artist:

    def __init__(self, name, uri):
        self.name = name
        self.uri = uri

        
class Album:        
        
        def __init__(self, title, artist, uri=None):
            self.title = title
            
