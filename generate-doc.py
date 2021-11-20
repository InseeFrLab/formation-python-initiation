"""Generate doc of a training program for https://www.sspcloud.fr."""

import os
import json
import urllib


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
    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(PROJECT_DIR, "METADATA.json"), "r") as file:
        md = json.load(file)

    # Main URLs
    LAUNCHER_TMPLT = ("https://datalab.sspcloud.fr/launcher/inseefrlab-helm-charts-datascience/"
                      "jupyter?init.personalInit=%C2%ABhttps%3A%2F%2Fraw.githubusercontent.com"
                      "%2FInseeFrLab%2Fformation-python-initiation%2Fmain%2Finit-onyxia.sh%C2%BB"
                      "&init.personalInitArgs=%C2%AB{init_args}%C2%BB&security.allowlist.enabled=false")
    COURSE_NAME_ENCODED = urllib.parse.quote(md['name'])
    DEFAULT_URL = f"https://www.sspcloud.fr/documentation?search=&path=%5B%22{COURSE_NAME_ENCODED}%22%5D"


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
        for chapter in section_md["chapters"].keys():
            # Build chapter block
            chapter_md = section_md["chapters"][chapter]
            init_args = urllib.parse.quote(f"{section} {chapter}")
            launcher_url = LAUNCHER_TMPLT.format(init_args=init_args)
            chapter_doc = generate_block(name=chapter_md["name"],
                                            abstract=chapter_md["abstract"],
                                            authors=md["authors"],
                                            contributors=md["contributors"],
                                            types=md["types"],
                                            tags=md["tags"],
                                            category=md["category"],
                                            img_url=md["img_url"],
                                            deployment_url=launcher_url
                                            )
            section_doc["parts"].append(chapter_doc)

        doc_json["parts"].append(section_doc)

    # Export doc
    with open(os.path.join(PROJECT_DIR, "doc-course.json"), "w") as file:
        json.dump(doc_json, file, indent=4)
