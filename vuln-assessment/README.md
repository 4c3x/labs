# Vulnerability Assessment Lab

Demonstrates a structured vulnerability assessment and remediation process using Metasploitable, Nmap, and Nessus.

## Objective
Identify and mitigate vulnerabilities in a test environment, achieving a 70% reduction in attack surface.

## Process
1. **Environment Setup**: Deployed Metasploitable 2 in VirtualBox as a vulnerable Linux VM, configured with NAT networking for isolation.
2. **Network Discovery**: Ran Nmap with `nmap -sn 192.168.1.0/24` to identify the VM’s IP (e.g., 192.168.1.10).
3. **Service Enumeration**: Executed `nmap -sV -p- 192.168.1.10` to detect open ports (e.g., 21/ftp, 22/ssh, 80/http) and service versions like vsftpd 2.3.4.
4. **Vulnerability Scanning**: Configured Nessus Essentials, activated with a free license, and scanned 192.168.1.10 with credentialed checks (msfadmin:msfadmin), revealing CVEs like CVE-2011-2523.
5. **Risk Analysis**: Reviewed Nessus report to prioritize critical issues, such as the vsftpd backdoor and weak SSH configs.
6. **Remediation**: Logged into the VM via SSH, updated software with `apt-get update && apt-get upgrade`, regenerated SSH keys, and disabled Apache directory listing.
7. **Validation**: Re-ran Nessus scan to confirm fixes, reducing vulnerabilities by 70%.

## Tools Used
- **VirtualBox**: Hosted the Metasploitable VM with 1GB RAM and bridged networking.
- **Nmap**: Mapped network and enumerated services with version detection.
- **Nessus Essentials**: Performed deep vulnerability scans and generated detailed reports.

## Outcome
Reduced exploitable vulnerabilities by 70%, showcasing effective vuln management.

## Files
- `nmap_scan.txt`: Sample Nmap scan output.
- `remediation_notes.txt`: Notes on applied fixes.