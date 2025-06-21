# gogdns by fin
import requests as r

def dns_type_to_code(dns_type: str) -> int:
    dns_types = {
        "A": 1,
        "NS": 2,
        "MD": 3,
        "MF": 4,
        "CNAME": 5,
        "SOA": 6,
        "MB": 7,
        "MG": 8,
        "MR": 9,
        "NULL": 10,
        "WKS": 11,
        "PTR": 12,
        "HINFO": 13,
        "MINFO": 14,
        "MX": 15,
        "TXT": 16,
        "AAAA": 28,
        "SRV": 33,
        "NAPTR": 35,
        "OPT": 41,
        "DS": 43,
        "RRSIG": 46,
        "NSEC": 47,
        "DNSKEY": 48,
        "TLSA": 52,
        "SVCB": 64,
        "HTTPS": 65,
        "CAA": 257,
    }

    return dns_types.get(dns_type.upper(), -1)

def _dohreq(domain: str, rrtype: str,
            check: bool = True,
            dnssec_ok: bool = False,
            subnet: str = "0.0.0.0/0") -> list: # list being the results
    baseurl = "https://dns.google/resolve"
    
    params = {
        "name": domain,
        "type": rrtype,
        "cd": str(int(not check)), # Turns True into 1 (False into 0) then into "1" (same for false)
        "do": str(int(dnssec_ok)), # Turns True into 1 (False into 0) then into "1" (same for false)
        "edns_client_subnet": subnet
    }
    
    res = r.get(baseurl, params=params)
    jsondata = res.json()
    
    if jsondata.get("Status") != 0 or "Answer" not in jsondata:
        return None
    
    results = []
    for entry in jsondata["Answer"]:
        if entry["type"] == dns_type_to_code(rrtype):
            results.append(entry["data"])
    return results

def gets(domain: str):
    ...

__all__ = ["gets"]