password = input("Test your password's strength: ")
strength = 0


def lengthChecker():
    if (len(password) < 8):
        strength += 1
    elif (len(password) >= 8 and len(password) < 14):
        strength += 2
    elif (len(password) >= 14):
        strength += 3
    else:
        return 0
    

def characterVariety(password):
    strength = 0

    # Uppercase check
    if any(c.isupper() for c in password):
        strength += 1

    # Lowercase check
    if any(c.islower() for c in password):
        strength += 1

    # Digit check
    if any(c.isdigit() for c in password):
        strength += 1

    # Special character check
    if any(not c.isalnum() for c in password):
        strength += 1

    return strength


def has_common_pattern(password):
    """Check for obvious/common patterns and keyboard patterns."""
    pw = password.lower()

    common_patterns = [
        "password", "qwerty", "asdf", "zxcv",
        "1234", "12345", "123456",
        "abcd", "abcde", "abcdef",
        "letmein", "admin"
    ]

    for pattern in common_patterns:
        if pattern in pw:
            return True
    return False


def has_repeated_run(password, max_run=3):
    """Check for long runs of the same character, e.g. 'aaaa'."""
    if not password:
        return False

    run_length = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            run_length += 1
            if run_length > max_run:  # e.g. more than 3 in a row
                return True
        else:
            run_length = 1
    return False


def is_step_sequence(s):
    """Check if the whole string is a step sequence like 'abcd' or '4321'."""
    if len(s) < 4:
        return False

    step = ord(s[1]) - ord(s[0])
    if step not in (1, -1):  # only care about +1 or -1 sequences
        return False

    for i in range(1, len(s) - 1):
        if ord(s[i + 1]) - ord(s[i]) != step:
            return False

    return True


def has_sequence(password):
    """Check for ascending/descending sequences inside the password."""
    pw = password.lower()
    n = len(pw)

    # Look at all substrings of length >= 4
    for length in range(4, n + 1):
        for start in range(0, n - length + 1):
            sub = pw[start:start + length]

            # Only check alphabetic-only or digit-only substrings
            if sub.isalpha() or sub.isdigit():
                if is_step_sequence(sub):
                    return True

    return False


def entropy_ok(password):
    """
    Returns True if the password passes all unpredictability checks:
    - no common patterns
    - no long repeated characters
    - no simple sequences
    """
    # All characters the same, like 'aaaaaa' or '111111'
    if len(set(password)) == 1:
        return False

    if has_common_pattern(password):
        return False

    if has_repeated_run(password, max_run=3):
        return False

    if has_sequence(password):
        return False

    return True


def check_strength(password):
    """Combine length, character variety and entropy to get a score."""
    score = 0

    # Length scoring
    if len(password) < 8:
        score += 0          # too short
    elif len(password) < 14:
        score += 1          # okay length
    else:
        score += 2          # very good length

    # Character variety (0–4)
    score += characterVariety(password)

    # Entropy / pattern checks
    if not entropy_ok(password):
        score -= 2          # penalty for simple / common patterns

    return score


def label_strength(score):
    """Turn numeric score into a human-friendly label."""
    if score <= 1:
        return "Very weak"
    elif score <= 3:
        return "Weak"
    elif score <= 5:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very strong"


def diagnose(password):
    """Explain why the password lost or gained points."""
    messages = []

    # Length checks
    if len(password) < 8:
        messages.append("Password is too short (less than 8 characters).")
    elif len(password) < 14:
        messages.append("Password could be longer (14 characters).")
    else:
        messages.append("Good length (14+ characters).")

    # Character variety diagnostics
    if not any(c.isupper() for c in password):
        messages.append("Missing uppercase letter.")
    if not any(c.islower() for c in password):
        messages.append("Missing lowercase letter.")
    if not any(c.isdigit() for c in password):
        messages.append("Missing a digit.")
    if not any(not c.isalnum() for c in password):
        messages.append("Missing a special character (!, @, #, $, etc.).")

    # Entropy / pattern checks
    if len(set(password)) == 1:
        messages.append("All characters are the same.")
    if has_common_pattern(password):
        messages.append("Contains a common pattern (e.g., '1234', 'password').")
    if has_repeated_run(password):
        messages.append("Contains repeated characters (more than 3 in a row).")
    if has_sequence(password):
        messages.append("Contains an alphabetical or numeric sequence (e.g., 'abcd', '1234').")
    if entropy_ok(password):
        messages.append("No obvious patterns detected.")

    return messages


final_score = check_strength(password)
print("Password score:", final_score)
print("Password strength:", label_strength(final_score))

print("\nReasons:")
for msg in diagnose(password):
    print("-", msg)
