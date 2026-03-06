def print_banner():
    print("=" * 40)
    print("        DNS Recon Tool")
    print("=" * 40)


def print_results(record_type, results):
    print(f"\n{record_type} Records:")

    for r in results:
        print(" -", r)


def print_dict(data):
    print("\n" + "=" * 40)

    for key, value in data.items():
        print(f"{key:<15} : {value}")

    print("=" * 40)