#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7873697236:AAHiUdrogxbCsBDAYTuj3jSZopRzm24dZVQ")
    API_ID = int(os.environ.get("API_ID", "25663773"))
    API_HASH = os.environ.get("API_HASH", "211365a39963382b3048cf6586dcff61")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7414415335")
