# -*- coding: utf-8 -*-

import pandas as pd
from collections import Counter
import requests
import pyquery
from collections import defaultdict
# df = pd.read_csv('../../datasets/prescribing_sample/GP_practice_prescribing_data.csv')
# print df['DRUG NAME                              ']

# TODO 1) The most expensive prescription and its name 2) sort by cost 3) use converter to clean columns name
addresses = (
    u'Победы',
    u'Генерала Лизюкова',
    u'Владимира Невского',
)
url = u'http://www.cmlt.ru/ads--p-last-page-1-buildType-8664-cityDistrict-%D0%9A%D0%BE%D0%BC%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9-kitAreaFrom-12-locality-%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6+%D0%B3.-period-0-priceTo-4+500+000-roomNumber-3-roomNumber-4-rubric-88-source-all-totalAreaFrom-82-viewType-list'
data = requests.request('GET', url, timeout=5)
data_html = pyquery.PyQuery(data.content)
ads = data_html('.ansLink')
ads_ids = []
for ad in ads:
    ad_pq = pyquery.PyQuery(ad)
    ad_address = ad_pq.find('div.an_property_value').text()
    for address in addresses:
        if ad_address.find(address) >= 0:
            flat_type = requests.request('GET', 'http://www.cmlt.ru' + ad_pq.attr('href'))
            flat_pq = pyquery.PyQuery(flat_type.content)('.an_property_value').filter(lambda i, this: pyquery.PyQuery(this).text().find(u'кирпичный') >= 0)
            if flat_pq:
                ads_ids.append('http://www.cmlt.ru' + ad_pq.attr('href'))
            break

with open('flats.html', 'wt') as flat:
    flat.write(
        """
        <!DOCTYPE html>
        <html>\n
        <body>\n
        <ol>\n
        """
    )
    for ad_id in ads_ids:
        flat.write('<li> <a target="_blank" href="%s">%s</a>  ' % (ad_id, ad_id))
        flat.write('</li>\n')

    flat.write('</ol>\n</body>\n</html>\n')

print ads_ids

