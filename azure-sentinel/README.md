# Azure Sentinel Lab

Simulates a Security Operations Center (SOC) using Azure Sentinel for log analysis and incident response.

## Objective
Detect and respond to threats efficiently in a cloud environment.

## Process
1. **Setup**: Created a Log Analytics workspace in Azure and enabled Sentinel via the portal.
2. **Log Source**: Deployed a Windows Server 2019 VM, installed the Azure Monitor Agent, and configured it to collect Security Event logs (e.g., Event ID 4625).
3. **Threat Simulation**: Ran `while ($true) { net use \\<VM-IP>\IPC$ /user:test wrongpass }` in PowerShell to simulate brute-force attempts.
4. **Detection**: Wrote a KQL query in Sentinel (`SecurityEvent | where EventID == 4625 | summarize FailedAttempts = count() by Account | where FailedAttempts > 50`) to flag excessive failures.
5. **Alert Rule**: Created an analytics rule with a 5-minute window and 50-attempt threshold to generate incidents.
6. **Automation**: Built a Logic Apps playbook to query the source IP, block it via Azure Firewall, and send an email alert.
7. **Testing**: Triggered the attack again, confirming incident creation and IP blocking within 2 minutes.
8. **Tuning**: Adjusted the threshold to 30 attempts to reduce false positives, improving response time by 40%.

## Tools Used
- **Azure Sentinel**: Analyzed logs and managed incidents.
- **Azure VM**: Generated test logs as a Windows Server.
- **PowerShell**: Simulated threats to trigger alerts.

## Outcome
Achieved a 40% faster response time, proving SOC readiness.

## Files
- `detection_rule.kql`: Sample KQL query.
- `simulate_attack.ps1`: Threat simulation script.