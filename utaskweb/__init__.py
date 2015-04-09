#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import requests
from bs4 import BeautifulSoup


def get_class_cancels(date_fill=False):
    url = "http://www.c.u-tokyo.ac.jp/zenki/classes/cancel/index.html"

    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    # updated
    updated = soup.find('div', {'id':'main'})
    updated = updated.h2.span.text.strip().split()[1]
    # cancels
    cancels = []
    for i, tr in enumerate(soup.find_all("tr")[1:]):
        tdata = tr.find_all("td")
        if date_fill is True and tdata[0].get_text(strip=True) == '':
            date = cancels[i-1]['date']
            day = cancels[i-1]['day']
            period = cancels[i-1]['period']
        else:
            date = tdata[0].get_text(strip=True)
            day = tdata[1].get_text(strip=True)
            period = tdata[2].get_text(strip=True)
        cancels.append(
            {"date": date,
             "day": day,
             "period": period,
             "subject": tdata[3].get_text(strip=True),
             "teacher": tdata[4].get_text(strip=True),
             "room": tdata[5].get_text(strip=True),
             "updated": tdata[6].get_text(strip=True),
            }
        )
    return updated, cancels


def get_class_roomchanges(date_fill=False):
    url = "http://www.c.u-tokyo.ac.jp/zenki/classes/classroomchange/index.html"

    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    # updated
    updated = soup.find('div', {'id':'main'}).h2.find_all('span')
    year = updated[0].text.strip().split()[1]
    month_day = updated[1].text.strip().split()[0]
    updated = year + month_day
    # changes
    changes = []
    for i, row in enumerate(soup.find_all("tr")[1:]):
        data = row.find_all("td")
        if date_fill is True and data[0].get_text(strip=True) == '':
            date = changes[i-1]['date']
            day = changes[i-1]['day']
            period = changes[i-1]['period']
        else:
            date = data[0].get_text(strip=True)
            day = data[1].get_text(strip=True)
            period = data[2].get_text(strip=True)
        changes.append(
            {"date": date,
             "day": day,
             "period": period,
             "subject": data[3].get_text(strip=True),
             "teacher": data[4].get_text(strip=True),
             "before_change": data[5].get_text(strip=True),
             "after_change": data[6].get_text(strip=True),
             "updated": data[7].get_text(strip=True),
            }
        )
    return updated, changes


def get_admin_announces():
    """Get announces from the administration office of University of Tokyo"""
    url="http://www.c.u-tokyo.ac.jp/zenki/news/kyoumu/index.html"
    host=url.split("/zenki", 2)[0]

    res=requests.get(url)
    soup=BeautifulSoup(res.text)
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
            data.append(
                    {"date"       : line.contents[0].strip(),
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

