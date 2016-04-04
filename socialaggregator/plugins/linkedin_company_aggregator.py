from datetime import datetime
from linkedin import linkedin

from django.conf import settings
from django.utils import timezone
from generic import GenericAggregator


class Aggregator(GenericAggregator):

    ACCESS_TOKEN = settings.EDSA_LINKEDIN_ACCESS_TOKEN

    def init_connector(self):
        self.connector = linkedin.LinkedInApplication(token=self.ACCESS_TOKEN)

    def search(self, query):
        res = self.connector.get_company_updates(query, params={})

        tz = timezone.get_current_timezone()
        datas = []
        for value in res['values']:
            if 'updateContent' in value and 'companyStatusUpdate' in value['updateContent']:
                share = value['updateContent']['companyStatusUpdate']['share']

                if 'content' in share and 'submittedUrl' in share['content']:
                    link, media_url_type = share['content']['submittedUrl'], 'link'
                else:
                    link = media_url_type = ''

                data = {'social_id': share['id'],
                        'name': 'linkedin share %s' % share['id'],
                        'slug': 'linkedin_share_%s' % share['id'],
                        'ressource_date': tz.localize(
                            datetime.fromtimestamp(int(share['timestamp']) / 1000)),
                        'description': share['comment'],
                        'media_url': link,
                        'media_url_type': media_url_type,
                        'author': value['updateContent']['company']['name'],
                        }
                datas.append(data)

        return datas
