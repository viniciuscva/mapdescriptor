def earth_bbox_area(north, south, east, west):
    
    from pyproj import Geod
    
    geod = Geod('+a=6378137 +f=0.0033528106647475126')
    lats = [north, north, south, south]
    lons = [east, west, west, east]
    area, perim = geod.polygon_area_perimeter(lons, lats)
    return abs(area)

def generate_text(north, south, east, west):
    
    import osmnx as ox
    import pandas as pd
    import inflect
    
    p = inflect.engine()
    pluralize = p.plural
    
    pois = ox.geometries.geometries_from_bbox(north, south, east, west, tags={'amenity':True})
    pois = pd.DataFrame(pois)
    pois.reset_index(inplace=True)
    pois = pois[['element_type', 'osmid', 'amenity', 'name', 'geometry', 'opening_hours']]
    area = earth_bbox_area(north, south, east, west)
    numbers_of_pois = pois.amenity.value_counts().to_dict()
    
    text = ""
    text += f"The total area selected is {round(area,2)}km2. In this area you can find "
    for poi_type in numbers_of_pois:
        text += str(numbers_of_pois[poi_type]) + " " + pluralize(poi_type) + ", "
    text += "enjoy the visit. "
    return text