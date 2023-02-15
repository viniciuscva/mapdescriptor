from flask import Flask, render_template, request, url_for, jsonify
import folium
import json
from geoutils import generate_text


app = Flask(__name__)

# https://www.youtube.com/watch?v=K2ejI4z8Mbg

# export FLASK_APP=main.py
# flask run
# export FLASK_ENV=development
# export FLASK_ENV=production
# Do not enable debug mode when deploying in production.
# flask --app example --debug run
# export FLASK_DEBUG=1
# set FLASK_DEBUG=1 (for windows)
# export FLASK_DEBUG=false
# export FLASK_DEBUG=true


# criar as páginas do site
# cada página tem:
# route
# função
# template

app = Flask(__name__)

start_coords = (-7.013426639837533, -36.778842655477064,)
folium_map = folium.Map(location=start_coords, zoom_start=7)
folium_map.save('templates/map.html')
text_description = ""

@app.route('/')
def index():
    return render_template('index.html', text_description = text_description)

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/map_bbox', methods = ['POST'])
def example():
    global text_description
    map_bbox = request.get_json()
    south, west = map_bbox['_southWest']['lat'], map_bbox['_southWest']['lng']
    north, east = map_bbox['_northEast']['lat'], map_bbox['_northEast']['lng']
    print('north:', north)
    print('south:', south)
    print('east:', east)
    print('west:', west)
    text_description = generate_text(north, south, east, west)
    #print(text_description)
    return jsonify({'text':text_description})


if __name__ == '__main__':
    app.run(debug=True)
