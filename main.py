from dns_lookup import query_record, full_scan
from whois_lookup import get_whois
from subdomain_finder import find_subdomains
from ip_geo import get_ip_location
from utils import print_banner, print_results, print_dict


def menu():
    print("\nChoose an option:")
    print("1. Lookup A record")
    print("2. Lookup MX record")
    print("3. Lookup NS record")
    print("4. Lookup TXT record")
    print("5. Full DNS scan")
    print("6. WHOIS lookup")
    print("7. Subdomain finder")
    print("8. IP geolocation")
    print("9. Exit")


def run():
    print_banner()

    domain = input("Enter domain: ")

    while True:
        menu()

        choice = input("Select option: ")

        if choice == "1":
            results = query_record(domain, "A")
            print_results("A", results)

        elif choice == "2":
            results = query_record(domain, "MX")
            print_results("MX", results)

        elif choice == "3":
            results = query_record(domain, "NS")
            print_results("NS", results)

        elif choice == "4":
            results = query_record(domain, "TXT")
            print_results("TXT", results)

        elif choice == "5":
            results = full_scan(domain)

            for record, data in results.items():
                print_results(record, data)

        elif choice == "6":
            data = get_whois(domain)
            print_dict(data)

        elif choice == "7":
            subdomains = find_subdomains(domain, "subdomains.txt")

            print("\nDiscovered Subdomains:")

            for sub in subdomains:
                print(" -", sub)

        elif choice == "8":
            ip = query_record(domain, "A")[0]

            data = get_ip_location(ip)
            print_dict(data)

        elif choice == "9":
            print("Exiting tool.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    run()