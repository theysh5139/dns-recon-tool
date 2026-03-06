import requests


def get_ip_location(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"

        response = requests.get(url)
        data = response.json()

        lat = data.get("lat")
        lon = data.get("lon")

        map_link = f"https://maps.google.com/?q={lat},{lon}"

        result = {
            "IP Address": data.get("query"),
            "Country": data.get("country"),
            "Region": data.get("regionName"),
            "City": data.get("city"),
            "ZIP": data.get("zip"),
            "Latitude": lat,
            "Longitude": lon,
            "Timezone": data.get("timezone"),
            "ISP": data.get("isp"),
            "Organization": data.get("org"),
            "AS Number": data.get("as"),
            "Google Maps": map_link
        }

        return result

    except Exception as e:
        return {"Error": str(e)}