# Basestore Userflow Automation

### 🛒 E-Commerce Sanity Flow Automation | Selenium + Pytest + POM

This automation framework validates the core **user purchase workflow of an e-commerce platform (Basestore)**.  
It covers key sanity flows including product search, cart management, checkout, order confirmation, and email notification.  
The framework is structured using **Page Object Model (POM)**, supports **data-driven testing (JSON & Excel)**, and generates **HTML reports with email triggering** after test execution.

---

## 🎯 Project Objective

✔ Automate core user transaction workflow on an e-commerce website  
✔ Ensure stability through Sanity and Checkout Automation  
✔ Validate UI elements, product pricing, and transaction confirmation  
✔ Enable data-driven test execution using JSON & XLSX  
✔ Generate HTML reports and trigger execution summary via email  

---

## 👤 Role & Ownership

**Role:** QA Automation Engineer (Complete framework development)  
**Responsibility Highlights:**  
✔ Designed and implemented test automation framework using POM  
✔ Enabled HTML reporting and email notification after test completion  
✔ Built reusable utilities for data-driven testing  
✔ Developed sanity test flow for core e-commerce journey

---

## 🛠️ Tech Stack & Tools

| Category            | Tools / Libraries |
|---------------------|--------------------|
| Programming         | Python |
| UI Automation       | Selenium |
| Test Framework      | Pytest |
| Architecture        | Page Object Model (POM) |
| Data Handling       | JSON, Excel (openpyxl) |
| Reporting           | Pytest HTML, Logging |
| Email Notifications | smtplib (SMTP) |
| IDE                 | PyCharm / VS Code |

---

## ⚙️ Features Implemented

✔ End-to-end automation of e-commerce **sanity userflow**  
✔ **POM-based framework** with modular design  
✔ **JSON & Excel Data-driven test execution**  
✔ HTML **Test Reports + Email triggering** after execution  
✔ Screenshot capture on failure  
✔ Cross-browser supported (Chrome, Edge)  
✔ Configurable test data and credentials  

---

## 🧪 Userflow Scenarios Covered

| Flow | Description |
|------|-------------|
| 🔐 Login | Authenticate user using test credentials |
| 🔍 Search Product | Search products with multiple data sets |
| 🛒 Add to Cart | Validate price, quantity, discount |
| 💳 Checkout | Fill address, payment, apply coupons |
| 📦 Order Confirmation | Capture order ID, verify success message |
| 📧 Email Validation | Validate order confirmation email trigger |

---

## ✉️ HTML Reporting & Email Trigger

✔ HTML Report auto-generated using `pytest-html`  
✔ Test summary and results are automatically sent via email after execution  

---

## 📥 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/username/basestore-userflow-automation.git

cd basestore-userflow-automation

# Install dependencies
pip install -r requirements.txt

# Run test
pytest -v --html=reports/report.html --self-contained-html
