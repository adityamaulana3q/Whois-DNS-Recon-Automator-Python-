import whois
import socket
import csv
import dns.resolver

def get_dns_records(domain):
    """Ambil DNS records (A, AAAA, MX)"""
    records = {"A": [], "AAAA": [], "MX": []}
    try:
        # A record (IPv4)
        answers = dns.resolver.resolve(domain, 'A')
        records["A"] = [rdata.to_text() for rdata in answers]
    except Exception:
        records["A"] = ["N/A"]

    try:
        # AAAA record (IPv6)
        answers = dns.resolver.resolve(domain, 'AAAA')
        records["AAAA"] = [rdata.to_text() for rdata in answers]
    except Exception:
        records["AAAA"] = ["N/A"]

    try:
        # MX records
        answers = dns.resolver.resolve(domain, 'MX')
        records["MX"] = [rdata.to_text() for rdata in answers]
    except Exception:
        records["MX"] = ["N/A"]

    return records

def get_whois_info(domain):
    """Ambil informasi WHOIS"""
    try:
        w = whois.whois(domain)
        return {
            "registrar": w.registrar if w.registrar else "N/A",
            "creation_date": str(w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date),
            "expiration_date": str(w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date),
            "name_servers": ";".join(w.name_servers) if w.name_servers else "N/A"
        }
    except Exception as e:
        return {
            "registrar": f"Error: {e}",
            "creation_date": "N/A",
            "expiration_date": "N/A",
            "name_servers": "N/A"
        }

def main():
    with open("domains.txt", "r") as f:
        domains = [line.strip() for line in f if line.strip()]

    with open("domain_report.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["domain", "registrar", "creation_date", "expiration_date", "name_servers", "A_record", "AAAA_record", "MX_record"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for domain in domains:
            print(f"[+] Processing {domain} ...")

            whois_info = get_whois_info(domain)
            dns_info = get_dns_records(domain)

            writer.writerow({
                "domain": domain,
                "registrar": whois_info["registrar"],
                "creation_date": whois_info["creation_date"],
                "expiration_date": whois_info["expiration_date"],
                "name_servers": whois_info["name_servers"],
                "A_record": ";".join(dns_info["A"]),
                "AAAA_record": ";".join(dns_info["AAAA"]),
                "MX_record": ";".join(dns_info["MX"])
            })

    print("[✓] Selesai! Hasil tersimpan di domain_report.csv")

if __name__ == "__main__":
    main()


