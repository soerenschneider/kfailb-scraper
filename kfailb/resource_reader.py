"""
Reads resources from the dedicated resources folder.
"""

import pkg_resources


def parse_urls():
    """
    Reads the urls to fire requests against
    :return: List of urls to use.
    """
    try:
        path = 'resources/urls.txt'
        filename = pkg_resources.resource_filename(__name__, path)
        with open(filename, 'r') as file:
            urls = file.read().splitlines()
            return urls
    except FileNotFoundError as e:
        print(e)
        return []


def read_user_agents():
    """
    Reads the user agents from the resources file.
    :return: list of the user agents to chose from randomly.
    """
    try:
        path = 'resources/user_agents.txt'
        filename = pkg_resources.resource_filename(__name__, path)
        with open(filename, 'r') as file:
            user_agents = file.read().splitlines()
            return user_agents
    except FileNotFoundError:
        return []