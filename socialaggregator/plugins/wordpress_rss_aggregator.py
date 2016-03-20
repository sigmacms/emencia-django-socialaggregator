import feedparser
from datetime import datetime

from django.utils import timezone
try:
    from django.utils.text import slugify
except ImportError:
    # older django
    from django.template.defaultfilters import slugify
from generic import GenericAggregator


class Aggregator(GenericAggregator):

    datetime_format = "%a, %d %b %Y %H:%M:%S +0000"

    def init_connector(self):
        pass

    def search(self, query):
        res = feedparser.parse(query)
        tz = timezone.get_current_timezone()
        datas = []
        for feed in res['entries']:
            content = feed['content'][0]
            if content['language']:
                language = content['language']
            else:
                language = ''
            data = {'social_id': feed['id'],
                    'name': feed['title'],
                    'slug': slugify(feed['title']),
                    'ressource_date': tz.localize(
                        datetime.strptime(feed['published'], self.datetime_format)),
                    'description': content['value'],
                    'language': language,
                    'media_url': feed['link'],
                    'media_url_type': 'url',
                    'author': feed['author'],
                    }
            datas.append(data)

        return datas
