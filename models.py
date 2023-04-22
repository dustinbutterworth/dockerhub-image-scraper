from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TagSchema:
    creator: int
    id: int
    images: List[dict]
    last_updated: str
    last_updater: int
    last_updater_username: str
    name: str
    repository: int
    full_size: int
    v2: bool
    tag_status: str
    tag_last_pulled: str
    tag_last_pushed: str
    media_type: str = ""
    content_type: str = ""
    content_type: str = ""
    digest: Optional[str] = ""


@dataclass
class RepositorySchema:
    name: str
    namespace: str
    repository_type: str
    status: int
    status_description: str
    description: str
    is_private: bool
    star_count: int
    pull_count: int
    last_updated: str
    date_registered: str
    affiliation: str
    media_types: List[str]
    content_types: List[str]


@dataclass
class ApiResponse:
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[RepositorySchema]

    def __post_init__(self):
        self.results = [RepositorySchema(**x) for x in self.results]


@dataclass
class TagApiResponse:
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[TagSchema]

    def __post_init__(self):
        self.results = [TagSchema(**x) for x in self.results]


@dataclass
class ApiParameters:
    page_size: Optional[str] = 100
    page: Optional[str] = None
