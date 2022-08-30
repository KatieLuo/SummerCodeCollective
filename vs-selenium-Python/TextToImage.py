import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'vsco nostalgia',
    },
    headers={'api-key': 'ebd84227-71a0-4e66-b308-223348ec1f4e'}
)
print(r.json())