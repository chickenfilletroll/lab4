# Lab 4.1 Reflection!!

# Server headers observed
- scanme.nmap.org: Apache/2.4.7 Ubuntu
- example.com: null (in phase 1)
- testphp.vulnweb.com: Apache
- httpbin.org: gunicorn/19.9.0
- demo.testfire.net: Apache-Coyote/1.1

These were helpful for identifying the server software and versions, which could reveal some  potential vulnerabilities.

# Differences between target sites
- Headers: Each site used different server software (Apache, gunicorn)
- Titles: scanme.nmap.org had security-focused title, example.com was just normal ig 
-Forms: testphp.vulnweb.com had login forms and user inputs, example.com had none 
- Keywords: testphp.vulnweb.com had one count of "error" and "admin" out of the list of keywords, every other website i tested all had 0 for the keywords

# Defensive use
Server admins can use this info to:
- Remove server headers to hide software versions
- Monitor for suspicious user-agents like sqlmap/nikto
- Implement firewalls to block automated scanning tools

## Ethical precautions
- Only scan authorized targets (like scanme.nmap.org ,testphp.vulnweb.com/)
- Never scan systems without explicit permission T-T
- Use educational/test sites designed for security practice
- Understand that unauthorized scanning is illegal :(
