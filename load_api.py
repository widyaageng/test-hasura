import requests
import time

def loadtest_api_hasura(url):
    """
    Load test the API
    """
    req = requests.Session()
    req.headers.update({
        'Content-Type': 'application/json',
        'X-Hasura-Admin-Secret': 'myadminsecretkey'
    })
    response = req.send(req.prepare_request(requests.Request('POST', url)))
    
    assert response.status_code == 200
    data = response.json()
    return data


if __name__=="__main__":
    url = "http://127.0.0.1:55946/api/rest/user-friend-stat/widya"

    while True:
        try:
            data = loadtest_api_hasura(url)
            time.sleep(0.01)
            print(data)
        except KeyboardInterrupt as e:
            break
        except Exception as e:
            print(e)
            break