import datetime

__author__ = 'User'

from meetupdriver import MeetUpDriver


class MeetUpClient(object):
    driver = None

    def __init__(self):
        self.driver = MeetUpDriver()

    def get_events(self, cat_id, limit=0, offset=0):
        """

        :param cat_id: category id
        :param limit: event qty for one request (optional)
        :param offset: skip X page
        :return: events list
        """
        if offset > 2: #aq shemomavali data shevzgude gadmosagzavni monacemebis moculobis shesamcireblad
            return []
        final_result = []
        params = {"category": cat_id}
        if limit:
            params["page"] = limit
        if offset:
            params["offset"] = offset
        events_list = self.driver.request("/2/open_events", params)
        #print json.dumps(events_list["meta"])
        for result in events_list["results"]:
            item = {}
            item["id"] = result["id"]
            item["title"] = result["name"]
            item["date"] = datetime.datetime.fromtimestamp(int(result["time"]) / 1000.0)
            item["description"] = result["description"] if "description" in result.keys() else "None"
            item["group_name"] = result["group"]["name"]
            item["category_id"] = cat_id  # self.get_id_of_group_category(int(result["group"]["id"]))
            final_result.append(item)
        if events_list["meta"]["next"]:
            return final_result + self.get_events(cat_id, limit, offset + 1)
        else:
            return final_result


    def get_id_of_group_category(self, group_id):

        group = self.driver.request("/2/groups", {"group_id": group_id})

        result = group["results"][0]["category"]["id"]

        # print "[done]"

        return result


if __name__ == "__main__":
    from pymongo import MongoClient

    events = MongoClient()["challenge"]["events"]
    cats = MongoClient()["challenge"]["categories"]
    client = MeetUpClient()
    k = 0

    cat_id = [int(i["cid"]) for i in list(cats.find())]
    # print cat_id
    for cat in cat_id:
        for i in client.get_events(cat):
            # events.insert(i)
            print i
            k += 1
        print k