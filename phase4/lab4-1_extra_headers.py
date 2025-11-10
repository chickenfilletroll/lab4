#!/usr/bin/env python3
# lab4-1_extra_headers.py
import requests, sys

def test_headers(url):
    test_cases = [
        {"name": "Normal", "headers": {}},
        {"name": "X-Forwarded-For", "headers": {"X-Forwarded-For": "1.2.3.4"}},
        {"name": "Fake Referer", "headers": {"Referer": "http://evil.example/"}},
        {"name": "French Language", "headers": {"Accept-Language": "fr-FR"}},
        {"name": "All Headers", "headers": {
            "X-Forwarded-For": "1.2.3.4",
            "Referer": "http://evil.example/",
            "Accept-Language": "fr-FR"
        }}
    ]
    
    for test in test_cases:
        try:
            r = requests.get(url, headers=test["headers"], timeout=5)
            print(f"\n[+] {test['name']}:")
            print(f"    Status: {r.status_code}")
            print(f"    Server: {r.headers.get('Server', 'N/A')}")
            print(f"    Content-Length: {len(r.text)}")
            if 'Location' in r.headers:
                print(f"    Redirect: {r.headers['Location']}")
        except Exception as e:
            print(f"\n[!] {test['name']} failed: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python lab4-1_extra_headers.py <url>")
        sys.exit(1)
    test_headers(sys.argv[1])


#python3 lab4-1_extra_headers.py http://httpbin.org/headers: server headers all the same, different content-length
#python3 lab4-1_extra_headers.py http://scanme.nmap.org: results all the same