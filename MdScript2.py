import requests

from qiniu import Auth

access_key = '...'
secret_key = '...'

q = Auth(access_key, secret_key)

bucket_domain = '...' #可以在空间设置的域名设置中找到
key = 'test_private_key'
base_url = 'http://%s/%s' % (bucket_domain, key)
private_url = q.private_download_url(base_url, expires=3600)
print(private_url)
r = requests.get(private_url)
assert r.status_code == 200
