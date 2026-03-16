import bpy
import csv

obj = bpy.data.objects["Camera"]
scene = bpy.context.scene

obj.animation_data_clear()

with open("camera_path.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        frame = int(row[0])
        x, y, z = float(row[1]), float(row[2]), float(row[3])
        scene.frame_set(frame)
        obj.location = (x, y, z)
        obj.keyframe_insert(data_path="location", frame=frame)

action = obj.animation_data.action
action.name = "CAM_flythrough_v01"

slot = action.slots[0]
channelbag = action.layers[0].strips[0].channelbag(slot)

for fcurve in channelbag.fcurves:
    for kp in fcurve.keyframe_points:
        kp.interpolation = "LINEAR"
    fcurve.update()

print("Done. Keyframes inserted and interpolation set.")
