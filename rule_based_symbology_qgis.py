import os

project_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'mapdescriptor')
os.chdir(project_dir)


with open('poi_types.txt') as f:
	poi_types = f.read()
poi_types = poi_types.split('\n')


poi_rules = ( (poi_type, f'"poi_class" LIKE \'{poi_type}\'', (1/2000.0, 1,) ) for poi_type in poi_types)

layer = QgsProject.instance().mapLayersByName('patos_pois_xml points')[0]
symbol = QgsSymbol.defaultSymbol(layer.geometryType())
renderer = QgsRuleBasedRenderer(symbol)
root_rule = renderer.rootRule()

for label, expression, scale in poi_rules:
	rule = root_rule.children()[0].clone()
	rule.setLabel(label)
	rule.setFilterExpression(expression)

	try:
		symbol = QgsSvgMarkerSymbolLayer(f'icons/amenities/{label}.svg')
	except:
		symbol = QgsSvgMarkerSymbolLayer('/home/carlos/Documents/mapdescriptor/icons/amenities/other.svg')
	symbol.setSize(6)
	symbol.setStrokeWidth(1)
	rule.symbol().changeSymbolLayer(0, symbol )

	if scale is not None:
		rule.setMinimumScale(scale[0])
		rule.setMaximumScale(scale[1])

	root_rule.appendChild(rule)

# delete the default rule
root_rule.removeChildAt(0)

# apply the renderer to the layer
layer.setRenderer(renderer)