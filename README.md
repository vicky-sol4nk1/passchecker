

````markdown
# 🔐 Password Strength Analyzer & Leak Checker

A Python-based command-line tool to analyze password strength and detect if a password has been exposed in common hacker wordlists like `rockyou.txt`.

---

![Screenshot](passchecker.png)

---


## 📸 Example Usage

### 🔹 Help Menu
```bash
python passchecker.py -h
````

### 🔹 Check Password Strength

```bash
python passchecker.py password123
```

### 🔹 Get Suggestions

```bash
python passchecker.py password123 -s
```

### 🔹 Generate Strong Password

```bash
python passchecker.py -g -l 16
```

### 🔹 Check if Password is Leaked

```bash
python passchecker.py password123 --check-leak
```

### 🔹 Use Custom Wordlist

```bash
python passchecker.py password123 --check-leak -w rockyou.txt
```

---

## 📂 Wordlist Support

The tool automatically checks for common wordlists in the current directory:

* `rockyou.txt`
* `passwords.txt`
* `wordlist.txt`
* `common.txt`

You can also provide your own wordlist using:

```bash
-w <path_to_wordlist>
```

---

## ⚠️ Important Note

* Wordlists like `rockyou.txt` are large (~14M passwords), so the first load may take time.
* This tool is for **educational and ethical use only**.

---

## 🎯 Learning Outcomes

This project helped me understand:

* Password security concepts
* Real-world use of wordlists in cybersecurity
* Building CLI tools using Python
* Writing clean and modular code

---


## 🚀 Features

- 🔍 Check password strength (Weak / Moderate / Strong)
- 💡 Suggest improvements for weak passwords
- ⚡ Generate strong random passwords
- 🧠 Detect leaked passwords using wordlists
- 📂 Supports:
  - Default wordlists (auto-detect in current directory)
  - Custom wordlists (user provided)
- 🖥️ Clean and simple CLI interface
- 
## 📌 Future Improvements

* 🌐 API integration (HaveIBeenPwned)
* 🎨 GUI version
* ⚡ Faster large file handling
* 📊 Password entropy calculation

---

## 🙌 Acknowledgment

This project was developed during my internship at **Pinnacle Labs**.

---

## 📬 Feedback

Feel free to open issues or suggest improvements!

---


