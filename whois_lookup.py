import whois


def format_value(value):
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)

    return str(value)


def get_whois(domain):
    try:
        data = whois.whois(domain)

        result = {
            "Domain Name": format_value(data.domain_name),
            "Registrar": format_value(data.registrar),
            "Creation Date": format_value(data.creation_date),
            "Expiration Date": format_value(data.expiration_date),
            "Name Servers": format_value(data.name_servers)
        }

        return result

    except Exception as e:
        return {"Error": str(e)}