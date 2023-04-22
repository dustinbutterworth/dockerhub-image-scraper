import requests
from dataclasses import asdict

from models import *

base_url = "https://hub.docker.com/v2/repositories"


def get_endpoint(endpoint: str, params: ApiParameters) -> ApiResponse:
    """ Return ApiResponse from dockerhub """
    url = f'{base_url}/{endpoint}'
    print(f'Retrieving: {url}')
    response = requests.get(
        url=url,
        params=asdict(params))
    response.raise_for_status()
    if endpoint.split('/')[-1] == "tags":
        response = TagApiResponse(**response.json())
    elif endpoint.split('/')[-1] == "images":
        response = response.json()
    else:
        response = ApiResponse(**response.json())

    return response
