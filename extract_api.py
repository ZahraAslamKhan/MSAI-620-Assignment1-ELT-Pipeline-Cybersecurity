import requests
import pandas as pd
from config import cve_api_url

def get_cve_data():
    response = requests.get(cve_api_url)
    if response.status_code == 200:
        data = response.json()
        # NVD returns a dict with "vulnerabilities" list
        if "vulnerabilities" in data:
            records = []
            for item in data["vulnerabilities"]:
                cve_id = item["cve"]["id"]
                description = item["cve"]["descriptions"][0]["value"]
                published = item["cve"]["published"]
                last_modified = item["cve"]["lastModified"]
                records.append({
                    "cve_id": cve_id,
                    "description": description,
                    "published": published,
                    "last_modified": last_modified
                })
            table = pd.DataFrame(records)
            table.to_csv("data/raw/cve.csv", index=False)
            table.to_json("data/raw/cve.json", orient="records")
            return table
        else:
            print("No vulnerabilities found in response")
            return pd.DataFrame()
    else:
        print("Error fetching CVE data:", response.status_code)
        return pd.DataFrame()
