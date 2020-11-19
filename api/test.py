
data = {
        "Name": "Gilbert P. Loyogoy",
        "LRN": "12101948",
        "Status": False,
        "Section": "7 Rizal",
        "Quarter": "1",
        "firstgrade": [
            {
                "Subject": "Math",
                "Grade": 79
            },
            {
                "Subject": "English",
                "Grade": 85
            },
            {
                "Subject": "Filipino",
                "Grade": 100
            }
        ]
    }

import requests

req = requests.post("http://127.0.0.1:8000/studentPush", data= data)

print(req.text)