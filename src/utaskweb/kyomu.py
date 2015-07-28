#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import requests
from bs4 import BeautifulSoup

from .common import get_text_if_exists


def get_admin_announces():
    """Get announces from the administration office of University of Tokyo"""
    url = "http://www.c.u-tokyo.ac.jp/zenki/news/kyoumu/index.html"
    host = url.split("/zenki", 2)[0]

    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    # updated
    updated = soup.find('p', {'id': 'update'})
    updated = updated.text.strip().split(u'：')[1]
    # announces
    data=[]
    newslist=soup.find("div", id="newslist2").find('dl')
    for line in newslist.find_all(['dt', 'dd']):
        if line == "\n":
            continue
        if str(line).startswith("<dt>"):
            imgs = line.find_all('img')
            date = get_text_if_exists(line.contents[0]).strip()
            data.append(
                    {"date"       : date,
                     "kind_image" : host + imgs[0].attrs["src"],
                     "grade_image": host + imgs[1].attrs["src"],
                    },
            )
        elif str(line).startswith("<dd>"):
            href = line.contents[0].attrs['href']
            if not href.startswith('http'):
                href = host + line.contents[0].attrs["href"]
            data[len(data)-1]["href"] = href
            data[len(data)-1]["announce"] = line.contents[0].string

    return updated, data

