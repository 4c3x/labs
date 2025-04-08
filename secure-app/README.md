# Secure Web App

Showcases a secure Flask-based login system designed to prevent unauthorized access.

## Objective
Develop a web application with robust security, validated against OWASP Top 10 risks.

## Process
1. **Setup**: Created a Python virtual environment with `python3 -m venv venv` and installed Flask and bcrypt via `pip install flask flask-wtf bcrypt`.
2. **App Design**: Built `app.py` with Flask, defining a login route and session management using a secret key (`app.secret_key = os.urandom(24)`).
3. **Credential Security**: Hashed passwords with `bcrypt.generate_password_hash()` before storing in a SQLite database.
4. **Input Validation**: Used Flask-WTF to add CSRF protection and reject malformed inputs like `<script>` tags.
5. **Encryption**: Generated a self-signed SSL certificate with `openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem` and ran Flask with `ssl_context=('cert.pem', 'key.pem')`.
6. **Testing**: Scanned with OWASP ZAP’s active scan on `https://localhost:5000`, identifying an XSS flaw; fixed by escaping outputs (`{{ data | e }}`).
7. **Hardening**: Added a CSP header (`Content-Security-Policy: default-src 'self'`) to block external scripts.
8. **Deployment**: Wrote a `Dockerfile` and built/run it with `docker build -t secure-app .` and `docker run -p 5000:5000 secure-app`.

## Tools Used
- **Python (Flask, bcrypt)**: Built the app and secured passwords.
- **OWASP ZAP**: Tested for vulnerabilities like XSS and SQL injection.
- **Docker**: Packaged the app for secure, portable deployment.

## Outcome
Delivered a secure app with no critical flaws, ready for production use.

## Files
- `app.py`: Main Flask application.
- `templates/login.html`: Login page template.