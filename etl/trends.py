from pytrends.request import TrendReq

def fetch_google_trends(product_name):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([product_name], cat=0, timeframe='today 12-m')
    data = pytrends.interest_over_time()
    return data
