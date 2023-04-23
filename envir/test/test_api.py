#### Welcome new app ############

import requests 

ENDPOINT = 'http://petstore-demo-endpoint.execute-api.com/petstore/pets'
response = requests.get(ENDPOINT)
print (response)
data = response.json()


def test_api_call():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass