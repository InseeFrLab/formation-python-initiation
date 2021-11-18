"""Test that all course notebooks have an associated solution file."""
import os

COURSE_DIR = "course"
chapters = os.listdir(COURSE_DIR)
for chapter in chapters:
    dir_chapter = os.path.join(COURSE_DIR, chapter)
    ipynb_paths = [f for f in os.listdir(dir_chapter) if f.endswith(".ipynb")]
    for ipynb in ipynb_paths:
        ipynb_name = ipynb.split(".")[0]
        solution_files = os.listdir(os.path.join(dir_chapter, "solutions"))
        solution_py = ipynb_name + ".py"
        if solution_py not in solution_files:
            path_missing = os.path.join(dir_chapter, "solutions", solution_py)
            raise FileNotFoundError(f"{path_missing} not found.")
