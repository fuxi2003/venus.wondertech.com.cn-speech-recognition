import requests

headers = {'API_SECRET': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbiI6ZmFsc2UsImVtYWlsIjoiaGFja2F0aG9uQHdvbmRlcnRlY2guY29tLmNuIiwiZXhwIjoxNjk3MDc4NTI1LCJ1c2VyaWQiOiJjNjBjYzcxNy02NDczLTRkMDctOWU3Yi02NWJlNTM5MDFiZjQifQ.LpZXDpIqOoZZb4537xKVwvjvadiAf1AjRVTvWQBSMog'}

url='https://venus.wondertech.com.cn/api/'
files={
    'file':('slingshot_swish_01.wav',open('./slingshot_swish_01.wav','rb'))
 }
response = requests.request("POST", url, files=files,headers=headers)

print(response.text)