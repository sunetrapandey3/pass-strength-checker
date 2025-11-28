import math
import re

BREACHED_WORDS = [
    "password", "qwerty", "letmein", "admin",
    "12345", "india", "welcome", "abc123"
]

def entropy(pwd):
    charset = 0
    if re.search(r"[a-z]", pwd): charset += 26
    if re.search(r"[A-Z]", pwd): charset += 26
    if re.search(r"[0-9]", pwd): charset += 10
    if re.search(r"[^A-Za-z0-9]", pwd): charset += 32

    return len(pwd) * math.log2(charset) if charset else 0


def analyze_password(pwd):
    score = 0
    suggestions = []

    # Basic checks
    if len(pwd) >= 12: score += 1
    else: suggestions.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", pwd): score += 1
    else: suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", pwd): score += 1
    else: suggestions.append("Add lowercase letters.")

    if re.search(r"[0-9]", pwd): score += 1
    else: suggestions.append("Add some numbers.")

    if re.search(r"[^A-Za-z0-9]", pwd): score += 1
    else: suggestions.append("Add special characters.")

    # Repeated chars
    if re.search(r"(.)\1\1", pwd):
        suggestions.append("Avoid repeating characters like aaa or 111.")
        score -= 1

    # Breached/common patterns
    for w in BREACHED_WORDS:
        if w in pwd.lower():
            suggestions.append(f'Remove common password pattern: "{w}"')
            score -= 2

    # Entropy scoring
    e = entropy(pwd)
    if e > 60: score += 1
    if e > 80: score += 1

    strength_labels = [
        "Very Weak", "Weak", "Fair", "Medium",
        "Strong", "Very Strong", "Cyber Fortified"
    ]

    # Clamp score
    score = max(0, min(score, 6))

    return {
        "password": pwd,
        "score": score,
        "entropy_bits": round(e, 2),
        "strength": strength_labels[score],
        "suggestions": suggestions,
    }
