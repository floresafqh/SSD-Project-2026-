# SSD-Project-2026-
# Secure Inventory Management System

## Project Description
A fully functional, lightweight secure inventory management system built natively using the Django framework. This application incorporates robust secure development principles mapped directly to the OWASP Top 10, OWASP ASVS and NIST SSDF guidelines to eliminate systemic injection vectors, authentication vulnerabilities and unauthorized access.

## Security Features Implemented
* Injection Vulnerability Prevention: Employs parameterized Object Relational Mapping (ORM) database lookups to completely block SQL Injection (SQLi).

* Cross-Site Scripting (XSS) Mitigation: Leverages Django’s context aware auto escaping template context layout engine.

* Input Validation Hardening: Server side whitelisting enforced using explicit alphanumeric regex patterns and boundary value validations.

* Role-Based Access Control (RBAC): Strict view layer routing authorization via login boundaries, alongside a read only tracking configuration for administrative oversight.

* Comprehensive Defensive Logging: Features a transaction audit tracker capturing operational execution milestones and failed login requests.

**Clone the Repository:**
   ```bash
   git clone <your-repository-link>
   cd secure_inventory_project
