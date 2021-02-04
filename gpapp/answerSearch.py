#coding:utf-8
#!/usr/bin/env python

import json
import urllib.request, urllib.parse


class Research:
    """
        class for managing the internal API process
        Google Map and wikimedia
    """
    def __init__(self, user, dataDiscussion):
        """Constructor of processing"""
        self.user = user
        self.dataDiscussion = dataDiscussion
        self.map_status = {}

    #================================
    # address coordinate calculation
    #================================
    def map_coordinates(self):
        """
            calculating the coordinates of the question asked to granbpy
            Vars :
                - parser_answer
                - place_id_dict
                - map_status
        """

        # keyword isolation for question
        parse_answer = self.user.question('parser')
        place_id_dict = self.get_place_id_list(
            address=parse_answer
        )
        # creation and test public key api google map
        try:
            place_id = place_id_dict['candidates'][0]['place_id']
        except IndexError:
            self.map_status = {}
        else:
            # creation of api google map coordinate address display setting
            # and wikipedia address history display setting
            self.map_status = {
                'address': self.get_address(place_id=place_id),
                'map': '',
                'history': self.get_history(search_history=' '.join(parse_answer))
            }
        return self.map_status

    #===================================
    # place_id search on Google Map API
    #===================================
    def get_place_id_list(self, address):
        """
            Google map API place_id search function
        """
        key = self.dataDiscussion.keys['map']
        # environment variable
        # replacing space by "% 20" in the string of characters
        address_encode = urllib.parse.quote(str(address))
        place_id = urllib.request.urlopen(
            'https://maps.googleapis.com/maps/api/place/findplacefromtext/'\
                f'json?input={address_encode}&inputtype=textquery&key={key}'
        )
        result = json.loads(place_id.read().decode('utf8'))
        return result

    #===========================
    # address on Google Map API
    #===========================
    def get_address(self, place_id):
        """
            Google map API address search with place_id function
        """
        key = self.dataDiscussion.keys['map'] # environment variable
        address_found = urllib.request.urlopen(
            'https://maps.googleapis.com/maps/api/place/details/'\
                f'json?placeid={place_id}&fields=formatted_address,geometry&key={key}'
        )
        result = json.loads(address_found.read().decode('utf8'))
        return result

    #=================================
    # history search on wikimedia API
    #=================================
    def get_history(self, search_history):
        """
            wikipedia API (Wikimedia) history search
        """
        # replacing space by "% 20" in the string of characters
        history_encode = urllib.parse.quote(search_history)

        history_found = urllib.request.urlopen(
            'https://fr.wikipedia.org/w/api.php?action=opensearch&search='\
                f'{history_encode}&format=json'
        )
        result = json.loads(history_found.read().decode('utf8'))
        return result

    #=========================================
    # map display in the Google Map Satic API
    #=========================================
    def get_map(self):
        """
            function of displaying the geolocation of the address
            asked to grandpy on the map of the Google Map Static API
        """
        key = self.dataDiscussion.keys['staticMap']  # environment variable
        location_map = self.map_coordinates()
        # adress display
        # replacing space by "% 20" in the string of characters
        formatting_address = urllib.parse.quote(
            location_map['address']['result']['formatted_address']
        )
        # longitude and latitude display
        localization = location_map['address']['result']['geometry']['location']
        # display map
        display_map = 'https://maps.googleapis.com/maps/api/staticmap?center='\
            f'{formatting_address}'\
            '&zoom=18.5&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C'\
            f"{localization['lat']},{localization['lng']}&key={key}"

        self.map_status['map'] = display_map
        return self.map_status
