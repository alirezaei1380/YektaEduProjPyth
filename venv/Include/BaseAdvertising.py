class BaseAdvertising :

    _nextId = 1

    def __init__(self):
        self._id = BaseAdvertising._nextId
        BaseAdvertising._nextId += 1
        self._clicks = 0
        self._views = 0

    @property
    def clicks(self):
        return self._clicks

    @property
    def views(self):
        return self._views

    def incClicks(self):
        self._clicks += 1

    def incViews(self):
        self._views += 1

    def describeMe(self):
        return "Id: " + self._id.__str__() + ", views: " + self.views.__str__()\
               + ", clicks: " + self.clicks.__str__() + ".\n"