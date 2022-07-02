from hentai import Hentai, Format, Utils


def get_id_from_name(name):
    # Searches nHentai for name and returns the gallery id.
    name = name.replace("_", " ")
    name = name.replace("-", " ")
    probable_doujins = Utils.search_by_query(name)
    gallery_id = None
    if probable_doujins:
        gallery_id = probable_doujins[0].id
    return gallery_id


def get_comic_info_from_id(gallery_id):

    def get_web_addr(gallery_id):
        if gallery_id:
            return f"https://nhentai.net/g/{gallery_id}/"
        return ""

    def get_title(doujin):
        if doujin.title(Format.Pretty):
            return doujin.title(Format.Pretty)
        return doujin.title

    def get_groups(doujin):
        tags = ""
        for tag in doujin.group:
            if tags:
                tags = tags + ","
            tags = tags + tag.name
        return tags

    def get_authors(doujin):
        tags = ""
        for tag in doujin.artist:
            if tags:
                tags = tags + ","
            tags = tags + tag.name
        return tags

    def get_tags(doujin):
        tags = ""
        for tag in doujin.tag:
            if tags:
                tags = tags + ","
            tags = tags + tag.name
        return tags

    def get_parodies(doujin):
        tags = ""
        for tag in doujin.parody:
            if tags:
                tags = tags + ","
            tags = tags + tag.name
        return tags

    def get_languages(doujin):
        tags = ""
        for tag in doujin.language:
            if tags:
                tags = tags + ","
            tags = tags + tag.name
        return tags

    def get_characters(doujin):
        tags = ""
        for tag in doujin.character:
            if tags:
                tags = tags + ","
            tags = tags + tag.name
        return tags

    if not gallery_id:
        return {
            "title": "",
            "author": "",
            "group": "",
            "tags": "",
            "parodies": "",
            "characters": "",
            "language": "",
            "web_addr": ""
        }

    doujin = Hentai(gallery_id)
    comic_info = {
        "title": get_title(doujin),             # Maps to Title
        "author": get_authors(doujin),          # Maps to Writer
        "group": get_groups(doujin),            # Maps to Publisher
        "tags": get_tags(doujin),               # Maps to Tags
        "parodies": get_parodies(doujin),       # Maps to Series
        "characters": get_characters(doujin),   # Maps to Characters
        "language": get_languages(doujin),      # Maps to LanguageISO
        "web_addr": get_web_addr(gallery_id)    # Maps to web
    }
    return comic_info


def generate_xml_from_comic_info(comic_info):
    # TODO: Impliment
    comic_info_xml = f'{comic_info["title"]}'
    return comic_info_xml


def nhentai_comic_info(name):
    gallery_id = get_id_from_name(name)
    comic_info = get_comic_info_from_id(gallery_id)
    comic_info_xml = generate_xml_from_comic_info(comic_info)
    return comic_info_xml


if __name__ == "__main__":
    print("Should give 409226:")
    print(get_id_from_name("♥ (HYK…)"))
