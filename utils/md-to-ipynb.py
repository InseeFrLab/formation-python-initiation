import json
import subprocess
import os
import sys

import frontmatter


def md_to_ipynb(md_path):
    """Convert a .md file in Jupyter notebook and set title using metadata."""
    ipynb_path = os.path.splitext(md_path)[0] + ".ipynb"

    # Extract metadata from qmd
    with open(md_path, "r") as md_file:
        fm = frontmatter.load(md_file)
    nb_title = fm["title"]

    # Convert qmd to ipynb
    CMD = f"jupytext --to notebook {md_path}"
    subprocess.run(CMD.split())

    with open(ipynb_path, "r") as json_file:
        ipynb_json = json.load(json_file)

    # Replace md metadata cell by ipynb title cell
    ipynb_json["cells"][0] = {
        "cell_type": "markdown",
        "source": [
            f'# {nb_title}'
        ],
        "metadata": {}
        }

    # Add kernel specs
    ipynb_json["metadata"]["kernelspec"] = {
        "display_name": "Python 3 (ipykernel)",
        "language": "python",
        "name": "python3"
        }

    with open(ipynb_path, "w") as json_file:
        json.dump(ipynb_json, json_file)
    

if __name__ == "__main__":

    md_to_ipynb(md_path=sys.argv[1])
