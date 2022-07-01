#!/usr/bin/env python3

from bs4 import BeautifulSoup


with open("test.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')


# Filters
def test_for_gallery_id(tag):
    try:
        if tag.name == "h3":
            if tag["id"] == "gallery_id":
                return True
    except:
        return False
    return False


def get_gallery_id(soup):
    for string in soup.find(test_for_gallery_id).strings:
        if string.isnumeric():
            return int(string)


def get_group(soup):
    return ["Test"]


def get_author(soup):
    return ["Test"]


def get_tags(soup):
    return ["Test"]


def get_parodies(soup):
    return ["Test"]


def get_languages(soup):
    return ["Test"]


comic_info = {
    "gallery_id": get_gallery_id(soup),
    "author": get_author(soup),
    "group": get_group(soup),
    "tags": get_tags(soup),
    "parodies": get_parodies(soup),
    "language": get_languages(soup)

}

print(comic_info)
