import requests

headers = {
    'authority': 'shopee.co.id',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': '3cb269fb91b5d896aed7e54eb3bf65f6',
}

params = (
    ('itemid', '1072213705'),
    ('shopid', '63826174'),
)

response = requests.get('https://shopee.co.id/api/v2/item/get?itemid=1072213705&shopid=63826174', headers=headers, params=params)

print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://shopee.co.id/api/v2/item/get?itemid=1072213705&shopid=63826174', headers=headers)
