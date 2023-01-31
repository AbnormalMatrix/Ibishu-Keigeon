import re
import numpy as np
# import open3d as o3d
import bpy
import bmesh

input_string = """{"nodeMaterial":"|NM_PLASTIC"},
         {"frictionCoef":0.5},
         {"collision":true},
         {"selfCollision":true},
         {"group":["pigeon_door_R", "pigeon_doorpanel_R"]},

         {"nodeWeight":0.5},
         ["d1r",-0.63,-0.56, 0.29],
         ["d2r",-0.66,-0.126, 0.29],
         ["d3r",-0.66,0.3, 0.29],

         ["d4r",-0.67,-0.56, 0.562],
         ["d5r",-0.67,-0.126, 0.562, {"selfCollision":false}],
         ["d6r",-0.67,0.3, 0.562],

         ["d7r",-0.63,-0.56, 0.87],
         ["d8r",-0.64,-0.126, 0.87, {"selfCollision":false}],
         ["d9r",-0.64,0.3, 0.87],

         {"nodeWeight":0.3},
         {"group":"pigeon_door_R"},
         ["d10r",-0.59, -0.37, 1.18],
         ["d11r",-0.52, -0.2, 1.42],
         ["d12r",-0.52, 0.3, 1.42],
         ["d13r",-0.59, 0.3, 1.18],

         //rigidifier
         {"selfCollision":false},
         {"collision":false},
         {"nodeWeight":0.5},
         ["d14r",-0.4, -0.126, 0.8],
         {"group":""},"""


class Node:
    def __init__(self, node_id, x, y, z):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.z = z
    
    def translate(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
    
    def rename(self, node_id):
        self.node_id = node_id
    

class Beam:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2




nodes = {}
beams = []

for line in input_string.split('\n'):

    if line.strip().startswith('['):
        
        try:
            line = line.split('{')[0].strip()
            node_id, x, y, z = re.findall(r'[\w\.-]+', line)


            print(node_id, x, y, z)

            node = Node(node_id, x, y, z)
            nodes[node_id] = node
            

        except:
            print('error')
            pass




for node in nodes.values():
    print(node)

    # create an empty in blender
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(float(node.x), float(node.y), float(node.z)))
    node.blender_object = bpy.context.object
    node.blender_object.name = node.node_id

    # resize the empty
    bpy.ops.transform.resize(value=(0.1, 0.1, 0.1))



