from flask import Flask, render_template, request
from dns_lookup import full_scan
from whois_lookup import get_whois
from ip_geo import get_ip_location
from subdomain_finder import find_subdomains
import concurrent.futures

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    results = {}

    if request.method == "POST":
        domain = request.form["domain"]

        with concurrent.futures.ThreadPoolExecutor() as executor:

            dns_future = executor.submit(full_scan, domain)
            whois_future = executor.submit(get_whois, domain)
            sub_future = executor.submit(find_subdomains, domain, "subdomains.txt")

            dns_data = dns_future.result()
            whois_data = whois_future.result()
            subdomains = sub_future.result()

        ip = None
        if dns_data.get("A"):
            ip = dns_data["A"][0]

        geo_data = get_ip_location(ip) if ip else {}

        results = {
            "dns": dns_data,
            "whois": whois_data,
            "subdomains": subdomains,
            "geo": geo_data
        }

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)