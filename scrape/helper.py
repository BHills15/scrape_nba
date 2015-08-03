import json
import urllib2

def get_data_from_url(url, index):
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    headers = data['resultSets'][index]['headers']
    rows = data['resultSets'][index]['rowSet']
    return [dict(zip(headers, row)) for row in rows]
