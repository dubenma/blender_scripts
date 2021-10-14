import bpy

camera_name = "Camera"

def create_camera():    
    # create the first camera
    cam = bpy.data.cameras.new(camera_name)
    cam.lens = 18
    #    cam = bpy.data.cameras[camera_name]
    
    # create camera object
    scn = bpy.context.scene
    cam_obj = bpy.data.objects.new(camera_name, cam)
    scn.collection.objects.link(cam_obj)   

    
def place_camera(location, rotation):  
    cam_obj = bpy.data.objects[camera_name]  
    cam_obj.location = location
    cam_obj.rotation_euler = rotation
    
    
def delete_camera():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[camera_name].select_set(True)
    bpy.ops.object.delete() 

def render(file_name, location, rotation):
    create_camera()
    place_camera(location, rotation)
    bpy.context.scene.camera = bpy.data.objects[camera_name]
    file_path = bpy.path.abspath("//"+"renders\\")
    bpy.context.scene.render.filepath = file_path + file_name 
    bpy.ops.render.render(write_still = True)
    delete_camera()
    
def render_all():    
    f = open(bpy.path.abspath("//"+"cam_positions.txt"), "r")
    
    line = f.readline()
    i = 1
    while line != '':
        location, rotation = read_params(line)
        file_name = "image%d_segmented.jpg" % i
        render(file_name, location, rotation)   
        
        line = f.readline()
        i = i + 1
        
def read_params(line):
    params = line.split(",")
    
    location = (float(params[0]),float(params[1]),float(params[2]))
    rotation = (float(params[3]),float(params[4]),float(params[5])) 
    return location, rotation  
    
if __name__ == "__main__":
    print("\nStarted\n")
    render_all()
    print("\nFinished")
 
    
    
