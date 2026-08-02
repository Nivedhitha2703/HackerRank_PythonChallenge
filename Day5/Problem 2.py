import re

n = int(input())

for _ in range(n):
    card = input().strip()

    # Check overall format
    if not re.match(r'^[456]\d{3}(-?\d{4}){3}$', card):
        print("Invalid")
        continue

    # Remove hyphens
    card = card.replace('-', '')

    # Check for 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card):
        print("Invalid")
    else:
        print("Valid")
