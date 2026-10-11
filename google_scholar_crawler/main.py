from scholarly import scholarly
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(name)s: %(message)s')
scholarly.set_logger(True)
import jsonpickle
import json
from datetime import datetime
import os
import requests

# Reject a blocked hosted-runner IP quickly instead of entering scholarly 1.5.1's
# unbounded 403 retry loop. Other matrix jobs can then try a different runner.
if os.environ.get('GITHUB_RUN_ID'):
    response = requests.get(
        'https://scholar.google.com/citations',
        params={'user': os.environ['GOOGLE_SCHOLAR_ID'], 'hl': 'en', 'pagesize': 100},
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/146.0.0.0 Safari/537.36'},
        timeout=15,
    )
    if response.status_code != 200 or 'gsc_rsb_st' not in response.text:
        raise RuntimeError(f'Google Scholar rejected this runner or returned a non-profile page (HTTP {response.status_code})')

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
if os.environ.get('GITHUB_RUN_ID'):
    author['sync_run_id'] = os.environ['GITHUB_RUN_ID']
    author['sync_run_attempt'] = os.environ.get('GITHUB_RUN_ATTEMPT', '1')
if type(author.get('citedby')) is not int or author['citedby'] < 0:
    raise ValueError('Google Scholar returned an invalid citation count')
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
