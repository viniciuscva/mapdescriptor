from flask import Flask, render_template, request, url_for, jsonify
import folium
import json

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

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/map_bbox', methods = ['POST'])
def example():
    map_bbox = request.get_json()
    print(map_bbox)
    return map_bbox


    #return render_template('example.html')


if __name__ == '__main__':
    app.run(debug=True)
