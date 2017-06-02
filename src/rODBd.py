from odbAccess import *
from operator import add
odb = openOdb('HE2St.odb')

step = odb.steps['STEP-2']

frame = step.frames[-1]

U = frame.fieldOutputs['U']

all_nodes = odb.rootAssembly.nodeSets[' ALL NODES'].nodes[0]
n_coord = {}
n_disp={}
# extract undeformed nodes, extract deformation field
for node in all_nodes:
    n_coord[node.label] = list(node.coordinates)
    n_disp[U.values[int(node.label)-1].nodeLabel] = list(U.values[int(node.label)-1].data[:])

# map deformation field to undeformed nodes to create the deformed geometry
n_def = {}
for node in n_disp.keys():
    n_def[node] = map(add,n_coord[node],n_disp[node])
    

print n_def

f_def = open("HE2StDefGeo.txt",'w')
# write deformed geometry to file
for node in n_def.keys():
    f_def.write(str(node) + ',   ' + str(n_def[node][0])+ ',   ' + str(n_def[node][1]) + ',   ' + str(n_def[node][2])+'\n')
