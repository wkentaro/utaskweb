#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import requests
from bs4 import BeautifulSoup


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
