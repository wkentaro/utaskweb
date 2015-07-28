#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def get_text_if_exists(node):
    if 'text' in dir(node):
        return node.text.strip()
    return node
