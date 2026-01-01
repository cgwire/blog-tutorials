import os
import shutil

import gazu

gazu.set_host("http://localhost/api")
user = gazu.log_in("admin@example.com", "mysecretpassword")

productions = gazu.project.all_projects()

for i, item in enumerate(productions):
    print(f"{i}. {item['name']}")

choice = int(input("Select a project: "))

production = productions[choice]

playlists = gazu.playlist.all_playlists_for_project(production)

for i, item in enumerate(playlists):
    print(f"{i}. {item['name']}")

choice = int(input("Select a playlist: "))

playlist = gazu.playlist.get_playlist(playlists[choice])
playlist_name = playlist["name"]

for shot in playlist["shots"]:
    shot_data = gazu.shot.get_shot(shot["entity_id"])
    shot_name = shot_data["name"]
    sequence_name = shot_data["sequence_name"]

    shot_dir = os.path.join(
        playlist_name,
        sequence_name,
        shot_name,
    )
    os.makedirs(shot_dir, exist_ok=True)

    preview = gazu.files.get_preview_file(shot["preview_file_id"])

    preview_filename = f"{preview['original_name']}.{preview['extension']}"
    preview_path = os.path.join(shot_dir, preview_filename)

    gazu.files.download_preview_file(preview, preview_path)

shutil.make_archive(
    base_name=playlist_name,
    format="zip",
    root_dir=os.path.dirname(playlist_name),
    base_dir=os.path.basename(playlist_name),
)
