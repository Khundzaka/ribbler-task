import json
import requests


class MeetUpDriver(object):
    key = None
    api_url = "https://api.meetup.com"

    def __init__(self):
        self.key = open("api_key.txt").readline()

    def getKey(self):
        print self.key

    def request(self, url_path, data):
        params = {"key": self.key}
        params.update(data)
        r = requests.get(self.api_url + url_path, params=params)
        return json.loads(r.text)


if __name__ == "__main__":
    meet = MeetUpDriver()
    print meet.getKey()

#    stream = open("temp.txt", "w")

    result = meet.request("/2/open_events", {"topic": "dogs"})
    print result
#    for res in result["results"]:
#        stream.write(json.dumps(res)+"\n")