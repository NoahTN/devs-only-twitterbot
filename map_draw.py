from PIL import Image
from io import BytesIO
import requests

class MapDraw:
    def get_image(self, coords):
        response = requests.get('https://www.mapquestapi.com/staticmap/v5/map?boundingBox=36.74,-121.99,36.5,-121.59&zoom=11&traffic=flow|cons|inc&size=700,500@2x&key=MfFt1rJi4T1sJLHkfIaITmfEzMdO57HM')
        img = Image.open(BytesIO(response.content))
        img.save("test.jpg")
        return img

map_draw = MapDraw()
map_draw.get_image([[]])
#map_draw.draw_outages([[36.648949, -121.791796]])



