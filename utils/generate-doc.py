"""Generate doc of a training program for https://www.sspcloud.fr."""
import logging
import os
from os.path import dirname
import json
import urllib.parse

import frontmatter


def extract_metadata_md(md_path):
    """Extract title and abstract metadata from a .md file."""
    with open(md_path, "r") as md_file:
        fm = frontmatter.load(md_file)

    return fm["title"], fm["abstract"]


def generate_block(name, abstract, authors, contributors, types, tags, category,
                   img_url, article_url=None, deployment_url=None):
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
        "img_url": img_url
    }

    if article_url is None and deployment_url is None:
        block["parts"] = []
    if deployment_url is not None:
        block["deploymentUrl"] = deployment_url
    if article_url is not None:
        block["articleUrl"] = article_url

    return block


if __name__ == "__main__":

    # Load course metadata
    PROJECT_DIR = dirname(dirname(os.path.abspath(__file__)))
    with open(os.path.join(PROJECT_DIR, "METADATA.json"), "r") as file:
        md = json.load(file)

    # Main URLs
    LAUNCHER_TMPLT = ("https://datalab.sspcloud.fr/launcher/inseefrlab-helm-charts-datascience/jupyter"
                      "?onyxia.friendlyName=«python-initiation»"
                      "&init.personalInit=«https://raw.githubusercontent.com/InseeFrLab/formation-python-initiation/main/utils/init-jupyter.sh»"
                      "&init.personalInitArgs=«{init_args}»"
                      "&security.allowlist.enabled=false")
    COURSE_NAME_ENCODED = urllib.parse.quote(md['name'])
    # DEFAULT_URL = f"https://www.sspcloud.fr/documentation?search=&path=«{COURSE_NAME_ENCODED}»"

    # Build documentation's top block
    doc_json = generate_block(name=md["name"], 
                              abstract=md["abstract"], 
                              authors=md["authors"], 
                              contributors=md["contributors"], 
                              types=md["types"], 
                              tags=md["tags"], 
                              category=md["category"], 
                              img_url=md["img_url"]
                              )
    for section in md["sections"].keys():
        # Build section block
        section_md = md["sections"][section]
        section_doc = generate_block(name=section_md["name"],
                                     abstract=section_md["abstract"],
                                     authors=md["authors"],
                                     contributors=md["contributors"],
                                     types=md["types"], 
                                     tags=md["tags"],
                                     category=md["category"],
                                     img_url=md["img_url"]
                                     )
        for chapter in section_md["chapters"]:
            # Build chapter block if notebook exists
            MD_PATH = os.path.join(PROJECT_DIR, "course", section, f"{chapter}.md")

            if os.path.isfile(MD_PATH):
                name, abstract = extract_metadata_md(MD_PATH)

                init_args = urllib.parse.quote(f"{section} {chapter}")
                launcher_url = LAUNCHER_TMPLT.format(init_args=init_args)

                chapter_doc = generate_block(name=name,
                                             abstract=abstract,
                                             authors=md["authors"],
                                             contributors=md["contributors"],
                                             types=md["types"],
                                             tags=md["tags"],
                                             category=md["category"],
                                             img_url=md["img_url"],
                                             deployment_url=launcher_url
                                             )
                section_doc["parts"].append(chapter_doc)

            else:
                raise FileNotFoundError(f"{MD_PATH} not found.")

        doc_json["parts"].append(section_doc)

    # Escape all quotes for CI dispatch step
    # print(json.dumps(doc_json, indent=4))
    doc_final = json.dumps(doc_json).replace('"', '\\"').replace("'", "\\'")

    # Export doc
    with open(os.path.join(PROJECT_DIR, "doc-course.txt"), "w") as file:
        file.write(doc_final)
