import json
import time
import requests


def get_house_lists():
    start_page = 0
    house_output = {}
    for _ in range(60):
        timestamp = int(time.time())
        params = f"type=2&shType=list&regionid=6&section=67&price=500$_1500$&shape=2&pattern=2,3&houseage=5_10,10_20&order=price_asc&firstRow={start_page}&totalRows=1180&timestamp={timestamp}"
        url = f"https://sale.591.com.tw/home/search/list?{params}"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55",
            "X-CSRF-TOKEN": "npK7llyQ2RxmfjC5WJKP0sQc3Zg1pFWrsbQc0cMt",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": "T591_TOKEN=440b33df18ed0cc1eaa6efcd6f4c6595; tw591__privacy_agree=0; is_new_index=1; is_new_index_redirect=1; __auc=1f5185af17d3903a3b58d5ce995; _ga=GA1.4.1174099801.1625194986; marketSearchHistory=[{%22search_type%22:5%2C%22sectionid%22:43}]; 78c780df159f0c0739847733a192a9f1=1; userLoginHttpReferer=https%253A%252F%252Fsale.591.com.tw%252F; new_rent_list_kind_test=0; webp=1; PHPSESSID=avrqimcmr00dvrm3l8pbkg6bu1; _gid=GA1.3.1009946283.1648916319; last_search_type=2; _gid=GA1.4.1009946283.1648916319; urlJumpIp=6; urlJumpIpByTxt=%E6%A1%83%E5%9C%92%E5%B8%82; user_sessionid=avrqimcmr00dvrm3l8pbkg6bu1; bid[pc][1.163.121.251]=3228; index_keyword_search_analysis=%7B%22role%22%3A%222%22%2C%22type%22%3A%222%22%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A1%2C%22hasPrompt%22%3A0%2C%22history%22%3A2%7D; newUI=1; user_index_role=2; user_browse_recent=a%3A5%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A10683411%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A10824745%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A10797980%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bi%3A12319559%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bi%3A12319637%3B%7D%7D; house_detail_stat=%5B%7B%22type%22%3A%222%22%2C%22resource%22%3A%228%22%2C%22post_id%22%3A%2210837363%22%7D%2C%7B%22type%22%3A%222%22%2C%22resource%22%3A%228%22%2C%22post_id%22%3A%2210930258%22%7D%2C%7B%22type%22%3A%222%22%2C%22resource%22%3A%228%22%2C%22post_id%22%3A%2210858855%22%7D%2C%7B%22type%22%3A%222%22%2C%22resource%22%3A%228%22%2C%22post_id%22%3A%2210789270%22%7D%2C%7B%22type%22%3A%222%22%2C%22resource%22%3A%228%22%2C%22post_id%22%3A%2210884598%22%7D%5D; XSRF-TOKEN=eyJpdiI6InppZ0RRbWdIUGZVM2YwZ1RBUEtcL2VRPT0iLCJ2YWx1ZSI6Ik9qR2JPckZVTDBtNjhXY2RmNmdZanJ4OFFaWnN6Y1h5b05ENEVKMUVyZ0k3QWxUTVdEUnQ2T2o2bnF6Yk9JbE9mcmxMOHkyTnZDNUZDSWYwOU9ZUW9nPT0iLCJtYWMiOiIxODRkOGViYTJkODE0NGUwMzljYzUxN2Q4MDYzYjUxZTg4OTI2MDY2N2NjYTRiYWU5Yzk4Nzc2NzRiYzAzZDExIn0%3D; _gat_UA-97423186-1=1; 591_new_session=eyJpdiI6ImdUNWRqMEV2c1A3ejdMd2xwRVU5VkE9PSIsInZhbHVlIjoia083aCtYZjlwMERXNmpPN0lGQlwvelwvdkVYUWN5VlRGS1pRVFF0ZjZHXC95a1E0Y3F0STBwUFNjNlwvZnlkTkdzZUwwbVNDK0RBYWJCUWFLTG5NU3MzSFpBPT0iLCJtYWMiOiIzN2U0ZjMyZDhlNmI4ZGQ2OTAwNmFiNzM1ZjNmMzNjNGJlNzM0ZDA1YjE2OWYzYzAxNzg0MzU5ZmUzZDc0OWVhIn0%3D; _gat=1; _dc_gtm_UA-97423186-1=1; _ga_ZDKGFY9EDM=GS1.1.1648997211.10.1.1649001998.0; _ga=GA1.3.1174099801.1625194986"
        }
        rsp = requests.get(url, headers=headers)
        rsp_json = rsp.json()
        h_list = {}
        for h in rsp_json["data"]["house_list"]:
            if "2衛" in h["room"] and h["community_link"] not in h_list:
                h_list.update({h["community_link"]: {"room": h["room"],
                              "url": h["community_link"],
                              "name": h["community_name"],
                              "price": h["price"],
                              "unit_price": h["unit_price"]}})

        house_output.update({f"start_page_{start_page}": h_list})

        start_page += 30

    with open("outputs/house_output.json", "w") as f:
        json.dump(house_output, f, indent=2)


if __name__ == "__main__":
    get_house_lists()
