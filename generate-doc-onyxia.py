"""Generate doc of a training program for https://www.sspcloud.fr."""

import os
import json 

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

    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Build documentation's top block
    with open(os.path.join(PROJECT_DIR, "METADATA.json"), "r") as file:
        md = json.load(file)
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
        section_doc = generate_block(name=section,
                                     abstract=section_md["abstract"],
                                     authors=md["authors"], 
                                     contributors=md["contributors"],
                                     types=md["types"], 
                                     tags=md["tags"], 
                                     category=md["category"],
                                     img_url=md["img_url"]
                                     )
        
        if "chapters" in section_md:
            for chapter in section_md["chapters"].keys():
                # Build chapter block
                pass
        doc_json["parts"].append(section_doc)
                