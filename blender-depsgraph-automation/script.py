import bpy
import csv
import os

def get_evaluated_mesh_stats(context, output_path):
    depsgraph = context.evaluated_depsgraph_get()
    rows = []

    for obj in context.scene.objects:
        if obj.type != 'MESH':
            continue

        obj_eval = obj.evaluated_get(depsgraph)
        mesh = obj_eval.to_mesh()

        try:
            vert_count = len(mesh.vertices)
            poly_count = len(mesh.polygons)
            dims = obj_eval.dimensions

            rows.append({
                "name": obj.name,
                "verts": vert_count,
                "polys": poly_count,
                "dim_x": round(dims.x, 4),
                "dim_y": round(dims.y, 4),
                "dim_z": round(dims.z, 4),
            })
        finally:
            obj_eval.to_mesh_clear()

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "verts", "polys", "dim_x", "dim_y", "dim_z"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Report written to {output_path}")


get_evaluated_mesh_stats(
    bpy.context,
    os.path.expanduser("~/mesh_report.csv")
)