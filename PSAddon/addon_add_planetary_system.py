bl_info = {
    "name": "New Planetary System",
    "author": "",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > Add > Mesh > New Planetary System",
    "description": "Adds a new Planetary System",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }


import bpy
import json
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

jsonFile = 'planetaty-characteristics.json'

def readJsonFile(path):
  """docstring for readJsonFile"""
  with open(path, 'r') as content_file:
    return json.loads(content_file.read())


def add_object(self, context):
  scale_x = self.scale.x
  scale_y = self.scale.y
  planetaryData = readJsonFile(jsonFile)
  sources = ["planets-physical-characteristics.html","planets-orbital-properties.html"]
  # get following props diameter, mass, planet, rotation
  physicalChars = planetaryData[0]
  # get following props planet, distance, revolution
  orbitalChars = planetaryData[2]

  for planet in physicalChars:
    print planet

  verts = [Vector((-1 * scale_x, 1 * scale_y, 0)),
      Vector((1 * scale_x, 1 * scale_y, 0)),
      Vector((1 * scale_x, -1 * scale_y, 0)),
      Vector((-1 * scale_x, -1 * scale_y, 0)),
      ]

  edges = []
  faces = [[0, 1, 2, 3]]

  mesh = bpy.data.meshes.new(name="New Object Mesh")
  mesh.from_pydata(verts, edges, faces)
  # useful for development when the mesh may be invalid.
  # mesh.validate(verbose=True)
  object_data_add(context, mesh, operator=self)


class OBJECT_OT_add_object(Operator, AddObjectHelper):
  """Create a new Mesh Object"""
  bl_idname = "mesh.add_object"
  bl_label = "Add Mesh Object"
  bl_options = {'REGISTER', 'UNDO'}

  scale = FloatVectorProperty(
      name="scale",
      default=(1.0, 1.0, 1.0),
      subtype='TRANSLATION',
      description="scaling",
      )

  def execute(self, context):

    add_object(self, context)

    return {'FINISHED'}


# Registration

def add_object_button(self, context):
  self.layout.operator(
      OBJECT_OT_add_object.bl_idname,
      text="Add Object",
      icon='PLUGIN')


  # This allows you to right click on a button and link to the manual
def add_object_manual_map():
  url_manual_prefix = "https://docs.blender.org/manual/en/dev/"
  url_manual_mapping = (
      ("bpy.ops.mesh.add_object", "editors/3dview/object"),
      )
  return url_manual_prefix, url_manual_mapping


def register():
  bpy.utils.register_class(OBJECT_OT_add_object)
  bpy.utils.register_manual_map(add_object_manual_map)
  bpy.types.INFO_MT_mesh_add.append(add_object_button)


def unregister():
  bpy.utils.unregister_class(OBJECT_OT_add_object)
  bpy.utils.unregister_manual_map(add_object_manual_map)
  bpy.types.INFO_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
  register()
