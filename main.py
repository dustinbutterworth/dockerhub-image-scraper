from typing import List
from time import sleep
from dhapi import get_endpoint
from models import *
from sys import argv
import os
import json


def json_dump_dir_creator(endpoint: str) -> str:
    """ create json dump directory and return that path for use """
    path = f'{endpoint}_dumps'
    os.makedirs(path, exist_ok=True)
    return path


def get_image_dumps(
        endpoint: str,
        tags: List[TagSchema],
        repo_name: str,
        dump_path: str):
    """ dump image data into json file for searching through later """
    for tag in tags:
        tag_name = tag.name
        params = ApiParameters()
        image_endpoint = f'{endpoint}/{tag.name}/images'
        response = get_endpoint(image_endpoint, params)
        sleep(1)
        file = os.path.join(
            dump_path,
            f"{dump_path}_{repo_name}_{tag_name}.json")
        with open(file, 'w+') as f:
            json.dump(response, f, indent=4)


def get_all_tags(
        endpoint: str,
        repositories: List[RepositorySchema],
        dump_path: str):
    """ Gets all tags passes to pass on and get dumps """
    for repo in repositories:
        tag_endpoint = f'{endpoint}/{repo.name}/tags'
        tags = get_all_paginated_results(tag_endpoint)
        repo_name = repo.name
        get_image_dumps(tag_endpoint, tags, repo_name, dump_path)


def get_all_paginated_results(endpoint: str) -> List[ApiResponse]:
    """ Get paginate results from dockerhub api """
    params = ApiParameters()
    if endpoint.split('/')[-1] == "tags":
        params.page_size = 5
    response = get_endpoint(endpoint, params)
    results = response.results
    page = 1
    while response.next:
        if endpoint.split('/')[-1] == "tags":
            break
        page += 1
        params.page = page
        response = get_endpoint(endpoint, params)
        sleep(1)
        results.extend(response.results)
        # some of these have like 10000 tags, so I'm breaking after the first
        # page.
    return results


if __name__ == "__main__":
    endpoint = argv[1]
    dump_path = json_dump_dir_creator(endpoint)
    images = get_all_paginated_results(endpoint)
    get_all_tags(endpoint, images, dump_path)
