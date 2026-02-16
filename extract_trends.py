from pytrends.request import TrendReq
import pandas as pd
from config import trend_keywords, trend_timeframe

def get_trends_data():
    pytrends = TrendReq()
    pytrends.build_payload(trend_keywords, timeframe=trend_timeframe)
    table = pytrends.interest_over_time()
    table.to_csv("data/raw/trends.csv", index=False)
    table.to_json("data/raw/trends.json", orient="records")
    return table
