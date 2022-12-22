import json
import os


__all__ = ['get_credentials']


def get_credentials(profile: str = "global") -> dict[str, str]:
    credentials_file = os.path.expanduser("~/ftrack_cred.json")
    with open(credentials_file) as _file:
        credentials = json.load(_file)
    return credentials[profile]
