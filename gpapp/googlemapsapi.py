#coding:utf-8
#!/usr/bin/env python

URL = 'https://maps.googleapis.com/maps/api/'
JSON = 'json?'
KEY_GET_PARAM = '&key='
FIND_PLACE_TEXT = 'place/findplacefromtext/'
INPUT_ADDRESS = 'input='
TYPE_GET_INPUT = '&inputtype=textquery'
DETAIL = 'place/details/'
PLACE_ID = 'placeid='
GET_FIELDS = '&fields=formatted_address,geometry'
STATIC_MAP = 'staticmap?'
POSITION = 'center='
GET_ZOOM = '&zoom=18.5'
GET_SIZE = '&size=600x300'
TYPE_GET_MAP = '&maptype=roadmap'
GET_MARKER = '&markers=color:red%7Clabel:A%7C'

# place_id search on Google Map API
def get_place_id_list(self, address, key_value):
    """
        Google map API place_id search function
    """
    place_id = urllib.request.urlopen(
        # ~ 'https://maps.googleapis.com/maps/api/place/findplacefromtext/'\
            # ~ f'json?input={address_encode}&inputtype=textquery&key={key}'
        f'{URL}{FIND_PLACE_TEXT}{JSON}{INPUT_ADDRESS}{address}{TYPE_GET_INPUT}'\
        f'{KEY_GET_PARAM}{key_value}'
    )
    result = json.loads(place_id.read().decode('utf8'))
    return result

# address on Google Map API
def get_address(self, place_id, key_value):
    """
        Google map API address search with place_id function
        Result OK
        {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'
        }
        Invalid API Key
        {
           "error_message" : "The provided API key is invalid.",
           "html_attributions" : [],
           "status" : "REQUEST_DENIED"
        }
        Invalid Place_id
        {
           "html_attributions" : [],
           "status" : "INVALID_REQUEST"
        }
    """
    address_found = urllib.request.urlopen(
        # ~ 'https://maps.googleapis.com/maps/api/place/details/'\
            # ~ f'json?placeid={place_id}&fields=formatted_address,geometry&key={key}'
        f'{URL}{DETAIL}{JSON}{PLACE_ID}{place_id}{GET_FIELDS}'\
        f'{KEY_GET_PARAM}{key_value}'
    )
    result = json.loads(address_found.read().decode('utf8'))
    return result

# map static search on Google Map API
def get_static(self, address, key_value):
    """
        Display of the static map at the user's request
    """
    display_address = address['address']['result']['formatted_address']
    # longitude and latitude display
    localization =\
        address['address']['result']['geometry']['location']
    # display map
    display_map = f'{URL}{STATIC_MAP}{POSITION}{display_address}{GET_ZOOM}'\
        f"{GET_SIZE}{TYPE_GET_MAP}{GET_MARKER}{localization['lat']},"\
        f"{localization['lng']}{KEY_GET_PARAM}{key_value}"
        # ~ 'https://maps.googleapis.com/maps/api/staticmap?center='\
        # ~ f'{formatting_address}'\
        # ~ '&zoom=18.5&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C'\
        # ~ f"{localization['lat']},{localization['lng']}&key={key}"
    return display_map
