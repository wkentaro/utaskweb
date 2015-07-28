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
