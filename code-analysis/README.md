# Static Code Analysis Lab

Highlights static application security testing (SAST) using Snyk within a DevSecOps pipeline.

## Objective
Enhance code security by resolving vulnerabilities in a forked repository.

## Process
1. **Repo Selection**: Forked a vulnerable Node.js repo (e.g., `express-example`) and cloned it with `git clone https://github.com/4c3x/express-example.git`.
2. **Setup**: Installed dependencies with `npm install` and noted outdated packages in `package.json`.
3. **Snyk Integration**: Installed Snyk globally (`npm install -g snyk`) and authenticated with `snyk auth`.
4. **Initial Scan**: Ran `snyk test`, identifying a high-severity vuln in `lodash` (CVE-2019-10744).
5. **Prioritization**: Reviewed Snyk output, focusing on the dependency path (`express > lodash@4.17.11`).
6. **Fix**: Updated to `lodash@4.17.21` with `npm install lodash@4.17.21 --save` and re-ran `snyk test` to verify.
7. **Automation**: Added a `.github/workflows/snyk.yml` file to run `snyk monitor` on push events, using a Snyk API token.
8. **Validation**: Audited with `npm audit` and confirmed an 80% risk reduction via Snyk’s online report.

## Tools Used
- **Snyk**: Scanned and monitored code for vulnerabilities.
- **Node.js**: Ran the sample application and managed dependencies.
- **GitHub Actions**: Automated Snyk scans in the pipeline.

## Outcome
Reduced critical risks by 80%, integrating security into development.

## Files
- `package.json`: Sample dependency file.
- `.snyk`: Policy file for scan settings.