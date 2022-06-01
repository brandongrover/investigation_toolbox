import requests
import config
import json

class ip_queries():
    def __init__(self, ipv4):
        self.ipv4 = ipv4
        self.ipdb_key = config.api_config['api']['abuse_ipdb']['key']
        self.ipdb_url = config.api_config['api']['abuse_ipdb']['url']

    def abuse_ipdb(self):
        querystring = {
            'ipAddress': self.ipv4,
            'maxAgeInDays': '90'
        }
        headers = {
            'Accept': 'application/json',
            'Key': self.ipdb_key
        }
        r = requests.request(method='GET', url=self.ipdb_url, headers=headers, params=querystring, timeout=config.request_timeout)
        r_text = json.dumps(r.json()['data'], sort_keys=False, indent=4)
        return r_text