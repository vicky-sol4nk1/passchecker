#!/usr/bin/env python3

import argparse
import random
import string
import os

# ---------- Strength Checker ----------
def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length < 6 or score <= 1:
        return "Weak"
    elif length >= 8 and score >= 3:
        return "Strong"
    else:
        return "Moderate"


# ---------- Suggestions (Text) ----------
def suggest(password):
    suggestions = []

    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters")
    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters")
    if not any(c.isdigit() for c in password):
        suggestions.append("Add numbers")
    if not any(not c.isalnum() for c in password):
        suggestions.append("Add special characters")

    return suggestions


# ---------- Strong Version Generator ----------
def suggest_strong_password(password):
    new_pass = list(password)

    if not any(c.isupper() for c in new_pass):
        new_pass.append(random.choice(string.ascii_uppercase))

    if not any(c.islower() for c in new_pass):
        new_pass.append(random.choice(string.ascii_lowercase))

    if not any(c.isdigit() for c in new_pass):
        new_pass.append(random.choice(string.digits))

    if not any(not c.isalnum() for c in new_pass):
        new_pass.append(random.choice("!@#$%^&*"))

    random.shuffle(new_pass)
    return ''.join(new_pass)


# ---------- Generate Password ----------
def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))


# ---------- Load Wordlist ----------
def load_wordlist(path):
    if not path or not os.path.exists(path):
        return set()

    print(f"[+] Loading wordlist: {path}")
    with open(path, "r", encoding="latin-1", errors="ignore") as f:
        return set(line.strip() for line in f)


# ---------- Default Wordlist ----------
def load_default_wordlist():
    possible_files = [
        "rockyou.txt",
        "passwords.txt",
        "wordlist.txt",
        "common.txt"
    ]

    # Check current directory
    for file in possible_files:
        if os.path.exists(file):
            print(f"[+] Found wordlist: {file}")
            return load_wordlist(file)

    # Optional Linux path
    linux_path = "/usr/share/wordlists/rockyou.txt"
    if os.path.exists(linux_path):
        return load_wordlist(linux_path)

    print("[!] No wordlist found")
    return set()


# ---------- Leak Check ----------
def check_leak(password, wordlist):
    return password in wordlist


# ---------- MAIN ----------
def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Analyzer 🔐"
    )

    parser.add_argument("password", nargs="?", help="Password to check")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate strong password")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length for generated password")
    parser.add_argument("-s", "--suggest", action="store_true", help="Suggest improvements")

    parser.add_argument("-w", "--wordlist", help="Custom wordlist")
    parser.add_argument("--check-leak", action="store_true", help="Check if password is leaked")

    args = parser.parse_args()

    # ---------- Generate Mode ----------
    if args.generate:
        pwd = generate_password(args.length)
        print(f"\nGenerated Password: {pwd}\n")
        return

    if not args.password:
        print("Please provide a password or use -g to generate one.")
        return

    password = args.password

    print(f"\nPassword: {password}")

    # ---------- Strength ----------
    strength = check_strength(password)
    print(f"Strength: {strength} ⚠️" if strength != "Strong" else f"Strength: {strength} ✅")

    # ---------- Suggestions ----------
    if args.suggest:
        print("\nSuggestions:")
        for s in suggest(password):
            print(f"- {s}")

        strong_version = suggest_strong_password(password)
        print(f"\n💡 Strong Version: {strong_version}")

    # ---------- Leak Check ----------
    if args.check_leak:
        if args.wordlist:
            wl = load_wordlist(args.wordlist)
        else:
            wl = load_default_wordlist()

        if wl:
            if check_leak(password, wl):
                print("\n[!] WARNING: Password found in hacker wordlist (LEAKED!) 🚨")
            else:
                print("\n[+] Password not found in wordlist ✅")
        else:
            print("\n[!] Leak check skipped (no wordlist)")

    print()


if __name__ == "__main__":
    main()