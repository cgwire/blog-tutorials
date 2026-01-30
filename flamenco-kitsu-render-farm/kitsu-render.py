import os
import gazu

import bpy

gazu.set_host("http://localhost/api")
user = gazu.log_in("admin@example.com", "mysecretpassword")

projects = gazu.project.all_projects()
project = projects[0]

tasks = gazu.task.all_tasks_for_project(project)

rendering = gazu.task.get_task_type_by_name("Rendering")
todo = gazu.task.get_task_status_by_name("todo")

render_tasks = [
    t
    for t in tasks
    if t["task_type_id"] == rendering["id"] and t["task_status_id"] == todo["id"]
]

for task in render_tasks:
    files = gazu.files.get_all_preview_files_for_task(task)
    if not files:
        continue

    latest = files[-1]
    if latest["extension"] == "blend":
        task_to_render = task
        latest_blend = latest
        break

if task_to_render is None:
    raise RuntimeError("No render task with a .blend preview found")

target_path = os.path.join(
    "/tmp", latest_blend["original_name"] + "." + latest_blend["extension"]
)
gazu.files.download_preview_file(latest_blend, target_path)

bpy.ops.wm.open_mainfile(filepath=target_path)

output_path = os.path.join(
    "/tmp", latest_blend["name"] + ".mp4"
)

bpy.context.scene.render.image_settings.file_format = "FFMPEG"
bpy.context.scene.render.ffmpeg.format = "MPEG4"
bpy.context.scene.render.ffmpeg.codec = "H264"
bpy.context.scene.render.ffmpeg.constant_rate_factor = "HIGH"
bpy.context.scene.render.ffmpeg.gopsize = 12
bpy.context.scene.render.ffmpeg.audio_codec = "AAC"
bpy.context.scene.render.filepath = output_path

bpy.ops.render.render(animation=True)

result = gazu.task.publish_preview(
    task_to_render,
    todo,
    comment="rendered",
    preview_file_path=output_path,
)
