import requests
import pandas as pd

#Contoh kode 5101201 = S-1 Akuntansi
kode = 5101201
base_url = f"https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend={kode}"

all_data = []

headers = {
    "Origin": "https://sscasn.bkn.go.id"
}

#offset = total data - 10
#contoh: karena total data 135, maka offset sampai 125
offset_number = 125
for offset in range(0, ((offset_number // 10) * 10), 10):
  url = f"{base_url}&offset={offset}"
  response = requests.get(url, headers=headers)
  
  if response.status_code == 200:
    json_data = response.json()
    data = json_data.get("data", {}).get("data", [])
    all_data.extend(data)
    print(f"Offset {offset} success")
  else:
    print(f"Failed in offset {offset}")
    break

df = pd.DataFrame(all_data)

df.to_excel("formasi_2.xlsx", index=False)
print("End")
