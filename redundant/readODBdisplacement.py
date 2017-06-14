from odbAccess import *

odb = openOdb(path='C:\\Users\\bioengsu\\Desktop\\dssr2017ABI-tjac799\\data\\HE2St.odb')

step = odb.steps['STEP-2']

frame = step.frames[-1]

U = frame.fieldOutputs['U']

all_nodes = odb.rootAssembly.nodeSets[' ALL NODES'].nodes[0]
n_coord = {}
for node in all_nodes:
    n_coord[node.label] = node.coordinates

print U
