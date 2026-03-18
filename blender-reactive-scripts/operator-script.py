import bpy

class AutoFrameOperator(bpy.types.Operator):
    bl_idname = "studio.auto_frame"
    bl_label = "Auto Frame Selected"

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            target = context.active_object
            if target:
                self.frame_camera_to(context, target)
            return {'FINISHED'}

        if event.type in {'RIGHTMOUSE', 'ESC'}:
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def frame_camera_to(self, context, target):
        camera = context.scene.camera
        if not camera:
            return
        focal_length = 85
        camera.data.lens = focal_length
        
        print(f"Framed camera on: {target.name}")

def register():
    bpy.utils.register_class(AutoFrameOperator)

def unregister():
    bpy.utils.unregister_class(AutoFrameOperator)