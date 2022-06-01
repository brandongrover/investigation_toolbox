import requests
import config
import json
from datetime import datetime

def logger(input_data):
  current_date = datetime.today().strftime('%Y-%m-%d')
  current_time = datetime.today().strftime('%H:%M:%S')
  with open(f"logs\error_log-{current_date}.txt", "a") as f:
    f.write(f"{current_time} | {input_data}\n")
  f.close()

class host_queries():
    def __init__(self, hostname):
        self.hostname = hostname
        self.whois_lookup_key = config.api_config['api']['whois_lookup']['key']
        self.whois_lookup_url = config.api_config['api']['whois_lookup']['url']

    def whois_lookup(self):
        querystring = {
            "key": self.whois_lookup_key,
            "domain": self.hostname,
            "format": "json"
        }
        r = requests.request(method="GET", url=self.whois_lookup_url, params=querystring, timeout=config.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text