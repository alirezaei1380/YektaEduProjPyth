from BaseAdvertising import BaseAdvertising

class Ad(BaseAdvertising) :

    def __init__(self, id, title, imgUrl, link, advertiser):
        super(Ad, self).__init__()
        self.__id = id
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.setAdvertiser(advertiser)

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setImgUrl(self, imgUrl):
        self.__imgUrl = imgUrl

    def getImgUrl(self):
        return self.__imgUrl

    def setLink(self, link):
        self.__link = link

    def getLink(self):
        return self.__link

    def setAdvertiser(self, advertiser):
        advertiser.addAd(self)

    def describeMe(self):
        return "This class stores some data and communicates(sets and gets) them."