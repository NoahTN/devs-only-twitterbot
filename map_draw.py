from PIL import Image
from io import BytesIO
import requests

class MapDraw:
    def get_image_url(self, coords):
        request = 'https://www.mapquestapi.com/staticmap/v5/map?boundingBox=36.74,-121.99,36.5,-121.59&zoom=11&traffic=flow|cons|inc&size=700,500@2x&key=MfFt1rJi4T1sJLHkfIaITmfEzMdO57HM'
        for coord in coords:
            request += f'&shape=radius:0.5km|{coord[0]},{coord[1]}'
        return request


