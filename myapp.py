import pymongo


class MyApp(object):
    db = None

    def __init__(self):
        self.db = pymongo.MongoClient()["challenge"]

    def get_persons_list(self):
        plist = [{"id": i["pid"], "name": i["fname"] + " " + i["lname"]} for i in list(self.db["persons"].find())]
        return plist

    def get_recommended(self, pid, limit=20):
        cat_list = [int(i["catid"]) for i in self.db["person_interests"].find({"pid": str(pid)})]
        # print cat_list

        result = list(self.db["events"].find({"category_id": {"$in": cat_list}}).limit(limit))
        result = [{"title": e["title"], "id": e["id"]} for e in result]
        return result


if __name__ == "__main__":
    print MyApp().get_recommended(45)