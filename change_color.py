import glob
import bpy


def load_all():
    file_path = "E:\\dubenma1\\data\\B315"
    objs = (glob.glob("E:\\dubenma1\\data\\B315\\*.obj"))

    for o in objs:
        imported_object = bpy.ops.import_scene.obj(filepath=o)
        obj_object = bpy.context.selected_objects[0] ####<--Fix
        print('Imported name: ', obj_object.name)
        
def delete_all():
    # Select objects by type
    for o in bpy.context.scene.objects:
        o.select_set(True)

    # Call the operator only once
    bpy.ops.object.delete()
    
def delete_materials():
    for x in bpy.context.object.material_slots: #For all of the materials in the selected object:
        bpy.context.object.active_material_index = 0 #select the top material
        bpy.ops.object.material_slot_remove() #delete it
        
def create_material():
    ob = bpy.context.active_object
    
    name = "pillar"

    # Get material
    mat = bpy.data.materials.get(name)
    if mat is None:
        # create material
        mat = bpy.data.materials.new(name=name)

    # Assign it to object
    if ob.data.materials:
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)
        
    mat.diffuse_color = (1,1,0,1)
    
if __name__ == "__main__":
#    delete_all()
#    load_all()
    delete_materials()
    create_material()

