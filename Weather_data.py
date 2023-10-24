import requests
import json
from datetime import datetime,timedelta
import math

data = {
    "product": "civil",
    "init": "2021110200",
    "dataseries": [
        {
            "timepoint": 3,
            "cloudcover": 6,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 3,
            "temp2m": 29,
            "rh2m": "78%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "oshowerday"
        },
        {
            "timepoint": 6,
            "cloudcover": 6,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 3,
            "temp2m": 32,
            "rh2m": "65%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "oshowerday"
        },
        {
            "timepoint": 9,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 3,
            "temp2m": 31,
            "rh2m": "73%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "lightrainday"
        },
        {
            "timepoint": 12,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 28,
            "rh2m": "76%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 15,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 27,
            "rh2m": "76%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 18,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 26,
            "rh2m": "76%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 21,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 25,
            "rh2m": "82%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 24,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 25,
            "rh2m": "85%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 27,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 29,
            "rh2m": "73%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 30,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 31,
            "rh2m": "63%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 33,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 32,
            "rh2m": "70%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 36,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 28,
            "rh2m": "71%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 39,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 27,
            "rh2m": "78%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 42,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 26,
            "rh2m": "85%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 45,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 25,
            "rh2m": "82%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 48,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 25,
            "rh2m": "85%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 51,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 29,
            "rh2m": "73%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 54,
            "cloudcover": 6,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 32,
            "rh2m": "65%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 57,
            "cloudcover": 5,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 31,
            "rh2m": "68%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 60,
            "cloudcover": 7,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 28,
            "rh2m": "66%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 63,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 27,
            "rh2m": "72%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 66,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 26,
            "rh2m": "75%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 69,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "none",
            "prec_amount": 4,
            "temp2m": 25,
            "rh2m": "83%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "cloudynight"
        },
        {
            "timepoint": 72,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 25,
            "rh2m": "85%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 75,
            "cloudcover": 5,
            "lifted_index": -1,
            "prec_type": "none",
            "prec_amount": 4,
            "temp2m": 29,
            "rh2m": "74%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "pcloudyday"
        },
        {
            "timepoint": 78,
            "cloudcover": 6,
            "lifted_index": -1,
            "prec_type": "none",
            "prec_amount": 4,
            "temp2m": 32,
            "rh2m": "61%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "mcloudyday"
        },
        {
            "timepoint": 81,
            "cloudcover": 8,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 32,
            "rh2m": "67%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 84,
            "cloudcover": 8,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 29,
            "rh2m": "74%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 87,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "none",
            "prec_amount": 4,
            "temp2m": 28,
            "rh2m": "72%",
            "wind10m": {
                "direction": "SE",
                "speed": 2
            },
            "weather": "cloudynight"
        },
        {
            "timepoint": 90,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "none",
            "prec_amount": 4,
            "temp2m": 27,
            "rh2m": "73%",
            "wind10m": {
                "direction": "W",
                "speed": 2
            },
            "weather": "cloudynight"
        },
        {
            "timepoint": 93,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 26,
            "rh2m": "79%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 96,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 26,
            "rh2m": "80%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 99,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 29,
            "rh2m": "74%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 102,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 31,
            "rh2m": "62%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 105,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 31,
            "rh2m": "70%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 108,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 29,
            "rh2m": "75%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 111,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "none",
            "prec_amount": 4,
            "temp2m": 28,
            "rh2m": "73%",
            "wind10m": {
                "direction": "SE",
                "speed": 2
            },
            "weather": "cloudynight"
        },
        {
            "timepoint": 114,
            "cloudcover": 8,
            "lifted_index": -1,
            "prec_type": "none",
            "prec_amount": 4,
            "temp2m": 27,
            "rh2m": "73%",
            "wind10m": {
                "direction": "SW",
                "speed": 2
            },
            "weather": "cloudynight"
        },
        {
            "timepoint": 117,
            "cloudcover": 3,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 26,
            "rh2m": "74%",
            "wind10m": {
                "direction": "W",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 120,
            "cloudcover": 4,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 26,
            "rh2m": "75%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 123,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 30,
            "rh2m": "71%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 126,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 31,
            "rh2m": "70%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 129,
            "cloudcover": 8,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 32,
            "rh2m": "67%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 132,
            "cloudcover": 7,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 29,
            "rh2m": "74%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 135,
            "cloudcover": 7,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 4,
            "temp2m": 28,
            "rh2m": "80%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 138,
            "cloudcover": 8,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 5,
            "temp2m": 27,
            "rh2m": "84%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 141,
            "cloudcover": 6,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 5,
            "temp2m": 25,
            "rh2m": "84%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 144,
            "cloudcover": 8,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 5,
            "temp2m": 25,
            "rh2m": "87%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 147,
            "cloudcover": 6,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 5,
            "temp2m": 29,
            "rh2m": "79%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 150,
            "cloudcover": 6,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 31,
            "rh2m": "67%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 153,
            "cloudcover": 6,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 31,
            "rh2m": "69%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 156,
            "cloudcover": 7,
            "lifted_index": -6,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 28,
            "rh2m": "75%",
            "wind10m": {
                "direction": "E",
                "speed": 2
            },
            "weather": "tsrainnight"
        },
        {
            "timepoint": 159,
            "cloudcover": 8,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 27,
            "rh2m": "82%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 162,
            "cloudcover": 8,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 26,
            "rh2m": "81%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 165,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 25,
            "rh2m": "85%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 168,
            "cloudcover": 9,
            "lifted_index": -1,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 25,
            "rh2m": "80%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 171,
            "cloudcover": 5,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 29,
            "rh2m": "78%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainday"
        },
        {
            "timepoint": 174,
            "cloudcover": 5,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 31,
            "rh2m": "67%",
            "wind10m": {
                "direction": "E",
                "speed": 3
            },
            "weather": "rainday"
        },
        {
            "timepoint": 177,
            "cloudcover": 7,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 30,
            "rh2m": "70%",
            "wind10m": {
                "direction": "E",
                "speed": 3
            },
            "weather": "rainday"
        },
        {
            "timepoint": 180,
            "cloudcover": 6,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 27,
            "rh2m": "80%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 183,
            "cloudcover": 4,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 26,
            "rh2m": "80%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 186,
            "cloudcover": 4,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 25,
            "rh2m": "83%",
            "wind10m": {
                "direction": "NW",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 189,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 24,
            "rh2m": "90%",
            "wind10m": {
                "direction": "N",
                "speed": 2
            },
            "weather": "rainnight"
        },
        {
            "timepoint": 192,
            "cloudcover": 9,
            "lifted_index": -4,
            "prec_type": "rain",
            "prec_amount": 6,
            "temp2m": 25,
            "rh2m": "89%",
            "wind10m": {
                "direction": "NE",
                "speed": 2
            },
            "weather": "rainday"
        }
    ]
}
#ret = requests.get('http://www.7timer.info/bin/api.pl?lon=100.5352&lat=13.7401&product=civil&output=json')
#data = ret.json()

def get_data(data,key):
    data_s = data['dataseries']
    ans = []
    dt = datetime.strptime(data['init'], '%Y%m%d%H')
    for i in range(len(data_s)):
        s = data_s[i]
        ans.append((dt+timedelta(hours=s['timepoint']), s[key]))
    return (ans) # ถ้าส่ง ans เฉยๆ จะเรียงข้อมูล

def get_hourly_average_data(tuples):
    data_t = tuple(tuples)
    ans = {}
    for i in range(len(data_t)):
        k = data_t[i][0].hour + 7 #ไม่ต้องบวกก็ได้ บวกแล้วได้ค่าเดียวกับอาจารย์
        if (k not in ans):
            ans[k] = [data_t[i][1]]
        else: ans[k].append(data_t[i][1])

    for key in ans.keys():
        x = ans[key]
        ans[key] = sum(x)/len(x)
    return ans

def get_daily_min_max(tuples):
    data_t = tuple(tuples)
    ans = {}
    for i in range(len(data_t)):
        k = data_t[i][0].date()
        if (k not in ans):
            ans[k] = [data_t[i][1]]
        else: ans[k].append(data_t[i][1])

    for key in ans.keys():
        x = ans[key]
        ans[key] = (min(x), max(x))
    return ans

def normalize(tuples):
    data_v = tuple(tuples)
    amount = len(data_v)
    ans = []
    x_avg = sum([v for t,v in data_v])/amount

    sum_x = 0
    for i in range(len(data_v)): sum_x += (data_v[i][1] - x_avg)**2

    s = math.sqrt(sum_x/amount)

    for i in range(len(data_v)): ans.append((data_v[i][0], (data_v[i][1] - x_avg) / s))

    return (ans)  # ถ้าส่ง ans เฉยๆ จะเรียงข้อมูล

def find_closest_weather(data,x):
    data_a = {}

    temp = dict(normalize(get_data(data,'temp2m')))
    rh = dict(normalize(set([(t,int(v[:-1])) for t,v in get_data(data,'rh2m')])))
    prec = dict(normalize(get_data(data,'prec_amount')))
    clo = dict(normalize(get_data(data,'cloudcover')))
    lif = dict(normalize(get_data(data,'lifted_index')))

    data_v = data['dataseries']
    dans = {}
    dt = datetime.strptime(data['init'], '%Y%m%d%H')
    for i in range(len(data_v)):
        s = data_v[i]
        dans[dt + timedelta(hours=s['timepoint'])] = s

    for key in temp.keys():data_a[key] = {'t':temp[key], 'r':rh[key], 'p':prec[key], 'c':clo[key], 'l':lif[key]}

    ans = []
    for key in data_a.keys():
        d = data_a[key]
        distance = (x['temp2m'] - d['t'])**2 + (x['rh2m'] - d['r'])**2\
                   + (x['prec_amount'] - d['p']) ** 2 + (x['cloudcover']-d['c'])**2\
                   + (x['lifted_index']-d['l'])**2
        if (len(ans) > 0):
            if (distance < ans[0][0]): ans[0] = (distance, key)
        else : ans.append((distance,key))
    dt = datetime.strptime(data['init'], '%Y%m%d%H')

    return dans[ans[0][1]]['weather']

temp = get_data(data,'temp2m')
rh = get_data(data,'rh2m')
print(temp)
print(rh) 

print(get_hourly_average_data(temp))

rh=set([(t,int(v[:-1])) for t,v in rh])
print(get_hourly_average_data(rh))

print(get_daily_min_max(temp))
print(normalize(get_data(data,'temp2m')))

print(find_closest_weather(data,{'temp2m':1.2,'rh2m':1.1,'prec_amount':1.1,'cloudcover':0.1,'lifted_index':0.1}))
print(find_closest_weather(data,{'temp2m':0.3,'rh2m':-1.1,'prec_amount':-3,'cloudcover':0,'lifted_index':0}))
