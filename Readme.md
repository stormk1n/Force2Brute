# 🗿 Force2Brute

Force2Brute is a fast, lightweight, and modular service enumeration and credential validation tool designed for penetration testing and security auditing. Built with scalability in mind, Force2Brute functions as a centralized engine capable of handling single targets or large-scale multi-entity lists simultaneously.

Currently, Force2Brute features a robust **FTP protocol verification module**, with plans to expand into a multi-service framework.

---

## 🚀 Features

* **Flexible Inputs:** Mix and match single inputs with massive wordlists effortlessly.
* **Smart Parsing:** Built-in validation checks for missing parameters and missing files.
* **Error Resilience:** Gracefully handles authentication rejections, network drops, and timeouts without crashing.
* **Clean Formatting:** Customized CLI help output designed for maximum terminal legibility.

---

## 🛠️ Installation & Setup

Force2Brute is written in pure Python 3 and uses native libraries, meaning no heavy external dependencies are required.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Force2Brute
   cd Force2Brute
   ```

2. **Make the script executable:**
   ```bash
   chmod +x Force2Brute
   ```

3. **Optional: Run globally as a native command:**
   ```bash
   mv Force2Brute.py Force2Brute
   sudo cp Force2Brute /usr/local/bin/
   ```

---

## 📖 Usage Examples

If installed globally, replace `./Force2Brute.py` with `Force2Brute`.

### 1. Single Target, Single User, Single Password
```bash
./Force2Brute.py -t 10.129.168.78 -u admin -p password123
```

### 2. Single Target with Username and Password Wordlists
```bash
./Force2Brute.py -t 10.129.168.78 -U users.txt -P passwords.txt
```

### 3. Mass Enumeration across Multiple Targets
```bash
./Force2Brute.py -T targets.txt -U common_users.txt -P rockyou.txt
```

---

## 🗺️ Project Roadmap

Force2Brute is built to grow. Future iterations of this framework will introduce:
- [ ] Terminal colorization (ANSI colors for Success/Failure tracking)
- [ ] SSH enumeration module
- [ ] SMB protocol mapping and authentication module
- [ ] Multi-threading for hyper-speed concurrent checks

---
<!--
## ⚠️ Disclaimer

This tool is developed strictly for educational purposes, authorized security auditing, and penetration testing. The author accepts no liability for misuse or damage caused by this utility. Always secure proper authorization before testing network infrastructure. -->
