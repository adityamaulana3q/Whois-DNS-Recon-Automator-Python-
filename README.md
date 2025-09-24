# Whois & DNS Recon Automator (Python)

Script Python sederhana untuk melakukan **WHOIS & DNS reconnaissance otomatis** pada daftar domain dari file teks, lalu menyimpan hasil ringkas ke file CSV.

## ✨ Fitur
- Membaca daftar domain dari `domains.txt`
- Melakukan **WHOIS query** untuk mendapatkan:
  - Registrar
  - Creation date
  - Expiration date
  - Name servers
- Melakukan **DNS lookup** untuk mendapatkan:
  - IPv4 (A record)
  - IPv6 (AAAA record)
  - Mail server (MX record)
- Menyimpan hasil ke `domain_report.csv`

---

## 📦 Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/USERNAME/whois-dns-recon.git
   cd whois-dns-recon
