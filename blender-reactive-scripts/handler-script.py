import bpy
from datetime import datetime

@bpy.app.handlers.persistent
def on_render_complete(scene, depsgraph):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    open("test.txt", "w").write(f"Completed: {timestamp}\n")

bpy.app.handlers.render_complete.append(on_render_complete)
