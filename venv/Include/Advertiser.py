from BaseAdvertising import BaseAdvertising

class Advertiser(BaseAdvertising) :

    _allAdvertisers = []

    def __init__(self, id, name):
        super(Advertiser, self).__init__()
        self._id = id
        self._name = name
        self._ads = []
        Advertiser._allAdvertisers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def clicks(self):
        totalClicks = super(Advertiser, self).clicks
        for ad in self._ads :
            totalClicks += ad.clicks
        return totalClicks

    @property
    def views(self):
        totalViews = super(Advertiser, self).views
        for ad in self._ads :
            totalViews += ad.views
        return totalViews

    def getTotalClicks():
        totalClicks = 0
        for ad in Advertiser._allAdvertisers :
            totalClicks += ad.clicks
        return totalClicks

    def help():
        return"""Id is a unique code for each object,
Name is obviously the name of the advertiser,
Clicks shows how many clicks the advertisers has had,
And views shows how many views the advertiser has had."""

    def describeMe(self):
        return "This class stores some data and communicates(sets and gets) them and also" +\
        "calculates the totalClicks of all advertisers."

    def addAd(self, ad):
        self._ads.append(ad)