import json

data = '{"var1":"harry", "var2":"56"}'
print(data)
parsed = json.loads(data)

print(type(parsed))

data2 = {
    "channel": "ytpro",
    "cars":['rabdi','gajab','taigooo'],
    "reel": ('dhaai','milk',589),
    "lol": False
}

js = json.dumps(data2)

print(js)

