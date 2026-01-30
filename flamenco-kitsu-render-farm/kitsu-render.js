const JOB_TYPE = {
  label: "Kitsu Render",
  settings: [],
};

function compileJob(job) {
  const settings = job.settings;

  const task = author.Task("kitsu-render", "misc");

  task.addCommand(
    author.Command("exec", { exe: "python3", args: ["kitsu-render.py"] }),
  );

  job.addTask(task);
}
