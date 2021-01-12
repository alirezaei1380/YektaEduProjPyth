from BaseAdvertising import BaseAdvertising

class Advertiser(BaseAdvertising) :

    __allAdvertisers = []

    def __init__(self, id, name):
        super(Advertiser, self).__init__()
        self.__id = id
        self.__name = name
        self.__ads = []
        Advertiser.__allAdvertisers.append(self)

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getClicks(self):
        total = super(Advertiser, self).getClicks()
        for ad in self.__ads :
            total += ad.getClicks()
        return total

    def getViews(self):
        total = super(Advertiser, self).getViews()
        for ad in self.__ads :
            total += ad.getViews()
        return total

    def getTotalClicks():
        total = 0
        for ad in Advertiser.__allAdvertisers :
            total += ad.getClicks()
        return total

    def help():
        return "Id is a unique code for each object,\n" +\
        "Name is obviously the name of the advertiser,\n" +\
        "Clicks shows how many clicks the advertisers has had,\n" +\
        "And views shows how many views the advertiser has had."

    def describeMe(self):
        return "This class stores some data and communicates(sets and gets) them and also" +\
        "calculates the totalClicks of all advertisers."

    def addAd(self, ad):
        self.__ads.append(ad)