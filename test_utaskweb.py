#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import requests
from bs4 import BeautifulSoup

import utaskweb


def assert_text_obj(obj):
    unicode_obj = unicode(obj)
    assert type(unicode_obj) == unicode


def test_get_text_if_exists():
    node1 = BeautifulSoup('<tr>Hello World</tr>')
    node2 = BeautifulSoup('Hello World')
    text1 = utaskweb.common.get_text_if_exists(node1)
    text2 = utaskweb.common.get_text_if_exists(node2)
    assert text1 == text2


def test_get_class_cancels():
    updated, cancels = utaskweb.get_class_cancels(date_fill=True)
    assert_text_obj(updated)
    for cancel in cancels:
        for text in cancel.values():
            assert_text_obj(text)


def test_get_admin_announces():
    updated, announces = utaskweb.get_admin_announces()
    assert_text_obj(updated)
    for announce in announces:
        for text in announce.values():
            if type(text) not in [unicode, str]:
                print dir(text)
            assert_text_obj(text)


def test_get_class_roomchanges():
    updated, roomchanges = utaskweb.get_class_roomchanges(date_fill=True)
    assert_text_obj(updated)
    for roomchange in roomchanges:
        for text in roomchange.values():
            assert_text_obj(text)

