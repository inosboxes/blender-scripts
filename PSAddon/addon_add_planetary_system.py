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

def add_planet(radius, distance):
  """docstring for add_planet"""
  bpy.ops.mesh.primitive_ico_sphere_add(
      subdivisions = 2,
      size = radius,
      location = (0.0, distance, 0.0),
      rotation = (0.0, 0.0, 0.0));

def add_object(self, context):

  planetaryData = readJsonFile(jsonFile)

  """ A.U. in km"""
  AU = float(149597870.7)
  FACTOR = float(1000000)

  for name, properties in planetaryData.iteritems():
    """ (A.U.) """
    distance = ( float(properties.distance) * AU) / FACTOR
    """ km """
    radius = ( float(properties.diameter) / 2) / FACTOR
    add_planet(radius, distance)


class OBJECT_OT_add_object(Operator, AddObjectHelper):
  """Create a new Planetary System"""
  bl_idname = "mesh.add_object"
  bl_label = "Add Planetary System"
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
      text="Add Planetary System",
      icon='PLUGIN')


  # This allows you to right click on a button and link to the manual
def add_object_manual_map():
  url_manual_prefix = "https://docs.blender.org/manual/en/dev/"
  url_manual_mapping = ( ("bpy.ops.mesh.add_object", "editors/3dview/object"),)
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
