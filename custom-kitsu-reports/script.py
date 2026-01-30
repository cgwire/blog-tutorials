import json
from datetime import date
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import gazu

# -----------------------------
# Configuration
# -----------------------------
STUDIO_NAME = "My Animation Studio"
STUDIO_LOGO = "studio_logo.png"  # local file path
PROJECT_NAME = "My Project"
OUTPUT_PDF = "activity_report.pdf"

gazu.set_host("http://localhost/api")
user = gazu.log_in("admin@example.com", "mysecretpassword")

projects = gazu.project.all_projects()
project = projects[0]

tasks = gazu.task.all_tasks_for_project(project)

report = []

for task in tasks:
    assignees = [gazu.person.get_person(p_id)["full_name"] for p_id in task["assignees"]]

    task_info = {
        "date": task["updated_at"],
        "entity": gazu.entity.get_entity(task["entity_id"])["name"],
        "type": gazu.task.get_task_type(task["task_type_id"])["name"],
        "status": gazu.task.get_task_status(task["task_status_id"])["name"]
    }

    for artist in assignees:
        report.append({**task_info, "artist": artist})

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("report.html")

html = template.render(
    studio_name=STUDIO_NAME,
    studio_logo=STUDIO_LOGO,
    project_name=PROJECT_NAME,
    report_date=date.today().isoformat(),
    rows=report
)

HTML(string=html, base_url=".").write_pdf(OUTPUT_PDF)

print(f"PDF generated: {OUTPUT_PDF}")
