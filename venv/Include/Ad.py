from BaseAdvertising import BaseAdvertising

class Ad(BaseAdvertising) :

    def __init__(self, title, imgUrl, link, advertiser):
        super(Ad, self).__init__()
        self._title = title
        self._imgUrl = imgUrl
        self._link = link
        self.setAdvertiser(advertiser)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def imgUrl(self):
        return self._imgUrl

    @imgUrl.setter
    def imgUrl(self, imgUrl):
        self._imgUrl = imgUrl

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    def setAdvertiser(self, advertiser):
        advertiser.addAd(self)

    def describeMe(self):
        return "This class stores some data and communicates(sets and gets) them."