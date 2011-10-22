import songretriever
import DBusBase

class ClementineHandler(DBusBase.DBusBase):
    '''Handler for Clementine'''
    NAME = 'Clementine'
    DESCRIPTION = 'Music handler for Clementine'
    AUTHOR = 'Mariano Guerra'
    WEBSITE = 'www.emesene.org'

    def __init__(self, main_window = None,
                 iface_name = 'org.mpris.clementine',
                 iface_path = '/TrackList'):
        DBusBase.DBusBase.__init__(self, main_window, iface_name, iface_path)

    def is_playing(self):
        '''Returns True if a song is being played'''
        if self.is_running():
            is_playing_iface = self.bus.get_object(self.iface_name, '/Player')
            if is_playing_iface:
                status = is_playing_iface.GetStatus()
                if status[0] == 0:
                    return True
        return False

    def get_current_song(self):
        '''Returns the current song in the correct format'''
        if self.is_playing():
            track = self.iface.GetCurrentTrack()
            song = self.iface.GetMetadata(track)
            return songretriever.Song(song['artist'],
                                      song['album'],
                                      song['title'],
                                      song['location'])

