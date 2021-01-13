class BaseAdvertising :

    def __init__(self):
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
        return "This class is designed to reduce duplicated code via inheritance."