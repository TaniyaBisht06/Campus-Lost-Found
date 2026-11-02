import os

# Campus Lost and Found Management System

# Retrieve API key securely from environment variables

API_KEY = os.getenv("API_KEY")

def display_lost_items():
print("Welcome to Campus Lost and Found System")

```
print("\nRecently Reported Lost Items:")
print("1. College ID Card")
print("2. Laptop")
print("3. Wallet")
print("4. Water Bottle")
```

def main():
display_lost_items()

```
if API_KEY:
    print("\nConnecting to external service...")
    print("API Key loaded securely.")
else:
    print("\nAPI Key not configured.")
```

if **name** == "**main**":
main()
