import dns.resolver


def query_record(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        results = []

        for data in answers:
            results.append(str(data))

        return results

    except dns.resolver.NoAnswer:
        return ["No record found"]

    except dns.resolver.NXDOMAIN:
        return ["Domain does not exist"]

    except Exception as e:
        return [f"Error: {e}"]


def full_scan(domain):
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
    scan_results = {}

    for record in record_types:
        scan_results[record] = query_record(domain, record)

    return scan_results