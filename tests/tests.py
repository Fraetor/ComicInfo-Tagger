#! /usr/bin/env python3
import unittest

with open("tests/1.html") as fp:
    html1 = fp.read()

with open("tests/2.html") as fp:
    html2 = fp.read()

import src.html_parser as hp


class TestParser(unittest.TestCase):

    def test_parse_nhentai_metadata(self):
        # Test with most tags.
        expected1 = {'author': 'amano kazumi',
                     'characters': 'shikikan,belfast',
                     'gallery_id': 262397,
                     'group': 'haiiro koubou betsumune',
                     'language': 'japanese',
                     'parodies': 'azur lane',
                     'tags': 'big breasts,sole female,stockings,sole '
                     'male,blowjob,x-ray,collar,maid,garter belt',
                     'title': 'Tenshi wa Mayonaka ni Saezuru',
                     'web_addr': 'https://nhentai.net/g/262397/'}
        actual1 = hp.parse_nhentai_metadata(html1)
        self.assertDictEqual(expected1, actual1,
                             msg="ComicInfo does not match!")

        # Test with some missing tags.
        expected2 = {'author': 'deadnoodles | gomyon',
                     'characters': 'producer,fuyuko mayuzumi',
                     'gallery_id': 409226,
                     'group': '',
                     'language': 'translated,english',
                     'parodies': 'the idolmaster',
                     'tags': 'catgirl',
                     'title': '♥',
                     'web_addr': 'https://nhentai.net/g/409226/'}
        actual2 = hp.parse_nhentai_metadata(html2)
        self.assertDictEqual(expected2, actual2,
                             msg="ComicInfo does not match!")


if __name__ == "__main__":
    unittest.main()
