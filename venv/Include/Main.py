from BaseAdvertising import BaseAdvertising
from Advertiser import Advertiser
from Ad import Ad

if __name__ == '__main__':
    advertiser1 = Advertiser("name1")
    advertiser2 = Advertiser("name2")
    ad1 = Ad("title1", "img-url1", "link1", advertiser1)
    ad2 = Ad("title2", "img-url2", "link2", advertiser2)
    print(ad2.describeMe())
    print(advertiser1.describeMe())
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad2.incViews()
    ad1.incClicks()
    ad1.incClicks()
    ad2.incClicks()
    print(advertiser2.name)
    advertiser2.name = "new name"
    print(advertiser2.name)
    print(ad1.clicks)
    print(advertiser2.clicks)
    print(Advertiser.getTotalClicks())
    print(Advertiser.help())