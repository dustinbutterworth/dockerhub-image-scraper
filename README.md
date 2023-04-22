# Dockerhub Image Scraper

For a given user profile, use the dockerhub api to list all their repositories then list the 5 most recent images of each tag of those images, then scrap the image data from `https://hub.docker.com/v2/repositories/{user}/{repository}/tags/{tag}/images`

You can find secrets and sensitive information in there, and no docker pulls necessary.

# prerequisites
```
python -m venv venv
pip install -r requirements.txt
```

# Usage
Run `main.py` with the username as an argument:

```
python main.py nginx
```

# Output
Outout goes into {user}_dumps directory in json format for you to search through.

# TODO
Add proper [rate limiting](https://docs.docker.com/docker-hub/api/latest/#tag/rate-limiting)
