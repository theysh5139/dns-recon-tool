import dns.resolver
from concurrent.futures import ThreadPoolExecutor


def check_subdomain(sub, domain):

    target = f"{sub}.{domain}"

    try:
        dns.resolver.resolve(target, "A")
        return target

    except:
        return None


def find_subdomains(domain, wordlist):

    found = []

    with open(wordlist) as f:
        subs = f.read().splitlines()

    with ThreadPoolExecutor(max_workers=50) as executor:

        results = executor.map(lambda s: check_subdomain(s, domain), subs)

        for r in results:
            if r:
                found.append(r)

    return found