import requests
from slugify import slugify

def link_builder(name, item_id, shop_id):
  name = slugify(name).lower()
  print("https://shopee.co.id/"+name+"-i."+str(shop_id)+"."+str(item_id))

def search_result(prev):
  headers = {
      'authority': 'shopee.co.id',
      'x-shopee-language': 'id',
      'x-requested-with': 'XMLHttpRequest',
      'if-none-match-': '55b03-3af6e068e58fc66314dfb4654f7b19d6',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61',
      'x-api-source': 'pc',
      'accept': '*/*',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://shopee.co.id/search?keyword=ikan',
      'accept-language': 'en-US,en;q=0.9',
      'if-none-match': '17fadebc3da4efe08ee66fcac6692a12',
  }

  params = (
      ('by', 'relevancy'),
      ('keyword', 'ikan'),
      ('limit', '50'),
      ('newest', prev),
      ('order', 'desc'),
      ('page_type', 'search'),
      ('version', '2'),
  )

  response = requests.get('https://shopee.co.id/api/v2/search_items/', headers=headers, params=params)

  json_data = response.json()

  for item in json_data['items']:
    link_builder(item['name'],item['itemid'],item['shopid'])


headers = {
    'authority': 'shopee.co.id',
    'x-shopee-language': 'id',
    'x-requested-with': 'XMLHttpRequest',
    'if-none-match-': '55b03-a1dd9d40f36679268436a4efef2d101d',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61',
    'x-api-source': 'pc',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://shopee.co.id/IKan-Dori-Fillet-patin-fillet-1-kg-i.63826174.1072213705',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_gcl_aw=GCL.1591875318.Cj0KCQjwrIf3BRD1ARIsAMuugNvfTelpIlctbexcPsMz7tWvFG3D4S1g4zDDtVsk4O5kzWh8yhsRiCsaAiuJEALw_wcB; _gcl_au=1.1.955720018.1591875318; _fbp=fb.2.1591875318571.1929258802; SPC_IA=-1; SPC_F=jMD4RtxNJHB7KTTQuHhaLp4bUTTTZXRP; REC_T_ID=a59da87c-abd7-11ea-b162-b49691277aa4; _gac_UA-61904553-8=1.1591875327.Cj0KCQjwrIf3BRD1ARIsAMuugNvfTelpIlctbexcPsMz7tWvFG3D4S1g4zDDtVsk4O5kzWh8yhsRiCsaAiuJEALw_wcB; _med=refer; G_ENABLED_IDPS=google; SPC_EC=-; SPC_U=-; _fbc=fb.2.1594128681018.IwAR0h2MD885DrsAaBLNh-kyxRk4erjueTenGCkvZTQ_-Lg5Qd4GnMxFGX778; SPC_SI=e0vtcc31nr5mb7pslavc3yp4jc62i5bk; csrftoken=aHE1TeKxPZQvgiywPQiyVSkSqbYRDVIn; welcomePkgShown=true; _gid=GA1.3.879419991.1594571253; SPC_CT_2903a5a3="1594573604.vwTu8XRqN3tRPICE7pHdrXP1YaXeMsqiNsmAY8cQpx4="; SPC_CT_410ddde9="1594573948.m2DnP0qL72+pHsrTm6dKqCVOoQqEfPz1SDkaUW98eso="; SPC_CT_a9a2996d="1594573948.DWl0Swt9jfVsehOnxPmZ3ylwtRTW2d9pNvTG2vDrSDo="; SPC_CT_f0dd31c5="1594574005.9WeC7QBJORAL7muHjiD85GENGV40Gv6/cKD4j3o+Eq4="; SPC_CT_6434a50b="1594575042.cLTapTbNM4MYcbpvscTVoMEQUeoZeXpzdnf+fyImJkg="; AMP_TOKEN=%24NOT_FOUND; cto_bundle=cl7tMV83R1d2ZVlicTVOZEdYSHBxck03NmxOd0VEdVpXZXI5cFJBWXhkNHl4Tko1TnlpZldFZ2U1YkRMUUNDbnJzRUxPMzgyQWdESHVKc1dPcmhKbVFsNG9xR3BibXNGUnBBTzVKR0ZnMDI3OW5Yb3B4eUZDWEI1a0lIcUxVdmJYRGZ2VzdScU43Sjh5U1B6dkN3JTJGTkVLQiUyRkpnJTNEJTNE; _ga=GA1.1.97354135.1591875327; _ga_SW6D8G0HXK=GS1.1.1594571250.6.1.1594576648.0; SPC_R_T_ID="aHW6cnHba3w/ZPBgi4InYhenuYSbcH0LRODP6zQZW/rZCrHlchKkQkaupmDtB3dkvznFxrbndvLeSVodU8N1QdBkyuXy7mNk2my15Gg/Ixc="; SPC_T_IV="NjbgcNWEqkmT3FBKXMoNBQ=="; SPC_R_T_IV="NjbgcNWEqkmT3FBKXMoNBQ=="; SPC_T_ID="aHW6cnHba3w/ZPBgi4InYhenuYSbcH0LRODP6zQZW/rZCrHlchKkQkaupmDtB3dkvznFxrbndvLeSVodU8N1QdBkyuXy7mNk2my15Gg/Ixc="',
    'if-none-match': '3cb269fb91b5d896aed7e54eb3bf65f6',
}

params = (
    ('itemid', '1072213705'),
    ('shopid', '63826174'),
)

response = requests.get('https://shopee.co.id/api/v2/item/get', headers=headers, params=params)

print(response.text)