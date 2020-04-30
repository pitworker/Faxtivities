from phaxio import PhaxioApi

testKey = '[Phaxio test key]'
testSec = '[Phaxio test secret code]'

liveKey = '[Phaxio live key]'
liveSec = '[Phaxio live secret code]'

name = 'recipient name'
number = 'recipient fax number'

files = []

for i in range(4):
    files.append(name + `i` + '.html')

api = PhaxioApi(liveKey, liveSec)
response = api.Fax.send(to=number,
                        files=files)
print(response.data.id)
