# -*- coding: utf-8 -*-
__author__ = 'mjafar'

import re
import urllib
from bs4 import BeautifulSoup

from core.scripts.twitter_related import on_demand
from core.utils.logging import log


class Hungry(on_demand.BaseOnTimelineDemandScript):
    command_pattern = '(%s)' % ')|('.join([r'چ(ی|ه) بخوری؟م', r'گ(رس|ش)نمه', r'چ(ی|ه) بپزم', r'hungry'])

    def received_command(self, command, data):
        match = re.search(self.command_pattern, command)

        if match:
            log("{0} is hungry".format(data['user']['screen_name']))

            raw_url = 'http://chibepazam.com/'
            page = BeautifulSoup(urllib.urlopen(raw_url).read())
            food_name = page.select('div.title').string
            receipe_url = page.select('img[src$=ok.gif]').parent['href']

            response = '@{0} {1} {2}' % (data['user']['screen_name'], food_name, receipe_url)

            self.twitter.update_status(
                status=response,
                in_reply_to_status_id=data['id_str']
            )