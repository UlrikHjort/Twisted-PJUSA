import requests
import sys


r = requests.get('http://localhost:8004/register?domain=asterisk1.adaheads.com&username=' + sys.argv[1] + '&password=' + sys.argv[2])
print r.status_code

print r.headers['content-type']

print r.encoding
