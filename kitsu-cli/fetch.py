import os

import click
import gazu
import questionary

gazu.set_host("http://localhost/api")
user = gazu.log_in("admin@example.com", "mysecretpassword")


@click.group()
def cli():
    """My Studio Kitsu Tool"""
    pass


@cli.command()
@click.argument("project_name", required=True)
@click.argument("output_path", required=True)
def pull(project_name, output_path):
    click.echo(f"Fetching TODO render tasks for project: {project_name}")

    project = gazu.project.get_project_by_name(project_name)

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
        size = len(files)

        if size > 0:
            latest = files[size - 1]
            if latest["extension"] == "blend":
                target_path = os.path.join(
                    output_path, latest["name"] + "." + latest["extension"]
                )
                gazu.files.download_preview_file(latest, target_path)


if __name__ == "__main__":
    cli()
