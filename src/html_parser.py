from bs4 import BeautifulSoup


def test_for_tag_type(tag, tag_type):
    try:
        if tag.name == "span":
            if tag["class"] == ["tags"]:
                if f'href="/{tag_type}/' in str(tag):
                    return True
    except:
        return False
    return False


def extract_tags(tags):
    tag_list = ""
    if tags:
        for tag in tags.find_all("span", class_="name"):
            if tag_list:
                tag_list = tag_list + ","
            tag_list = tag_list + " ".join(tag.string.split())
    return tag_list


def get_gallery_id(soup):
    for string in soup.find("h3", id="gallery_id").strings:
        if string.isnumeric():
            return int(string)


def get_title(soup):
    return soup.find("meta", property="og:title")["content"]


def get_groups(soup):
    def test_for_group(tag):
        return test_for_tag_type(tag, "group")
    tags = soup.find(test_for_group)
    return extract_tags(tags)


def get_authors(soup):
    def test_for_authors(tag):
        return test_for_tag_type(tag, "artist")
    tags = soup.find(test_for_authors)
    return extract_tags(tags)


def get_tags(soup):
    def test_for_tag(tag):
        return test_for_tag_type(tag, "tag")
    tags = soup.find(test_for_tag)
    return extract_tags(tags)


def get_parodies(soup):
    def test_for_parodies(tag):
        return test_for_tag_type(tag, "parody")
    tags = soup.find(test_for_parodies)
    return extract_tags(tags)


def get_languages(soup):
    def test_for_language(tag):
        return test_for_tag_type(tag, "language")
    tags = soup.find(test_for_language)
    return extract_tags(tags)


def get_characters(soup):
    def test_for_character(tag):
        return test_for_tag_type(tag, "character")
    tags = soup.find(test_for_character)
    return extract_tags(tags)


def get_web_addr(soup):
    gallery_id = get_gallery_id(soup)
    if gallery_id:
        return f"https://nhentai.net/g/{gallery_id}/"
    return ""


def parse_nhentai_metadata(html):
    soup = BeautifulSoup(html, 'html.parser')
    comic_info = {
        "gallery_id": get_gallery_id(soup),
        "title": get_title(soup),  # Maps to Title
        "author": get_authors(soup),  # Maps to Writer
        "group": get_groups(soup),  # Maps to Publisher
        "tags": get_tags(soup),  # Maps to Tags (ComicInfo.xml 2.1 feature)
        "parodies": get_parodies(soup),  # Maps to Series
        "characters": get_characters(soup),  # Maps to Characters
        "language": get_languages(soup),  # Maps to LanguageISO
        "web_addr": get_web_addr(soup)  # Maps to web
    }
    return comic_info


if __name__ == "__main__":
    from pprint import pprint

    with open("tests/2.html") as fp:
        html = fp.read()

    pprint(parse_nhentai_metadata(html))
