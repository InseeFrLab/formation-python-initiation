"""Generate doc of a training program for https://www.sspcloud.fr."""

import os
import json 

def generate_block(name, abstract, authors, contributors, types, tags, category,
                   image_url, article_url=None, deployment_url=None):
    """Generate json documentation for a training program block.
    
    If both `article_url` and `deployment_url` are None, the block is assumed
    to be a container for further sub-blocks (i.e. has an "open" button).
    Otherwise, either one of or both `article_url` and `deployment_url` must
    be provided. 
    """
    block = {
        "name": name,
        "abstract": abstract,
        "authors": authors,
        "contributors": contributors,
        "types": types,
        "tags": tags,
        "category": category,
        "imageUrl": image_url
    }

    if article_url is None and deployment_url is None:
        block["parts"] = []
    if deployment_url is not None:
        block["deploymentUrl"] = deployment_url
    if article_url is not None:
        block["articleUrl"] = article_url

    return block


def get_metadata_ipynb(ipynb_path):
    """Extract title and abstract from the metadata of a Jupyter Notebook.
    
    An error is raised if these metadata are not present.
    """
    with open(ipynb_path, "r") as file:
        ipynb_json = json.load(file)
    ipynb_metadata = ipynb_json["metadata"]

    if "title" not in ipynb_metadata.keys() or "abstract" not in ipynb_metadata.keys():
        raise KeyError("'title' and 'abstract' fields must be set in each notebook's metadata.")

    return ipynb_metadata["title"], ipynb_metadata["abstract"]






CWD = os.getcwd()
COURSE_DIR = os.path.join(CWD, "course")
chapters = [ch for ch in COURSE_DIR if os.path.isdir(os.path.join(COURSE_DIR, ch))]
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


if __name__ == "__main__":
    FORMATION = "Initiation à Python"
    ABSTRACT = "Cours introductif à Python : fondamentaux du langage et premières manipulations de données"
    AUTHORS = ["inseefrlab"]
    CONTRIBUTORS = ["Romain Avouac, Julie Djiriguian, Yves-Laurent Bénichou, Lino Galiana"]
    TYPES = ["Site documentaire"]
    TAGS = ["discover", "learn"]
    CATEGORY = "datascience with R and Python"
    IMG_URL = "https://raw.githubusercontent.com/InseeFrLab/www.sspcloud.fr/main/src/app/assets/img/python.jpg"