#!/usr/bin/env python3

import re
import argparse
import random
import string

# -------------------------------
# Password Strength Checker
# -------------------------------
def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase length to at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score == 5:
        strength = "Very Strong 💪"
    elif score >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, suggestions


# -------------------------------
# Strong Password Generator
# -------------------------------
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# -------------------------------
# Improve Weak Password
# -------------------------------
def suggest_stronger_version(password):
    improved = password

    if not re.search(r"[A-Z]", improved):
        improved += random.choice(string.ascii_uppercase)

    if not re.search(r"[0-9]", improved):
        improved += str(random.randint(0, 9))

    if not re.search(r"[!@#$%^&*]", improved):
        improved += random.choice("!@#$%^&*")

    if len(improved) < 8:
        improved += ''.join(random.choice(string.ascii_letters) for _ in range(8 - len(improved)))

    return improved


# -------------------------------
# CLI Arguments
# -------------------------------
def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer 🔐")

    parser.add_argument("password", nargs="?", help="Password to check")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate strong password")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length for generated password")
    parser.add_argument("-s", "--suggest", action="store_true", help="Suggest stronger version")

    args = parser.parse_args()

    # Generate password
    if args.generate:
        print("Generated Password:", generate_strong_password(args.length))
        return

    # Check password
    if args.password:
        strength, suggestions = check_password_strength(args.password)

        print(f"\nPassword: {args.password}")
        print(f"Strength: {strength}")

        if suggestions:
            print("\nSuggestions:")
            for s in suggestions:
                print(f"- {s}")

        # Suggest stronger version
        if args.suggest:
            improved = suggest_stronger_version(args.password)
            print("\nSuggested Stronger Password:", improved)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()