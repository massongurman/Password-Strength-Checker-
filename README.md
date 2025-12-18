Password Strength Checker
About

This project is a simple Python program that checks how strong a password is based on common security rules. The goal is to help users understand whether a password is weak or strong and why, using basic checks that are commonly discussed in cybersecurity.The program runs in the terminal and gives immediate feedback after a password is entered. What It Checks Password length Longer passwords score higher than short ones.

Character types

Checks if the password includes:
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Common weak patterns

Looks for obvious or commonly used patterns such as:
- password, 12345
- Keyboard patterns like qwerty or asdf

How It Works

The user enters a password in the terminal. The program runs a series of checks on the password. Each check contributes to a total strength score. The final result is displayed as weak, moderate, or strong.
Example

**Test your password's strength:** **hello123**

**Password Strength:** **Weak**

Why I Made This
Password security is one of the most basic but important concepts in cybersecurity. This project was created to practice:
- Python fundamentals
- Input validation and string handling
- Applying real-world security rules in code

Tools Used:
- Python
- Command line interface

Possible Improvements:
- Adding more advanced scoring 
- Giving suggestions to improve weak passwords
- Turning it into a small web app or GUI

Note
This project is for learning purposes only and does not store or log passwords.
