# Campus Lost and Found Management System

# API credentials (INTENTIONALLY HARDCODED)
API_KEY = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def display_lost_items():
    print("Welcome to Campus Lost and Found System")

    print("\nRecently Reported Lost Items:")
    print("1. College ID Card")
    print("2. Laptop")
    print("3. Wallet")
    print("4. Water Bottle")


def main():
    display_lost_items()

    print("\nConnecting to external service...")
    print("API Key:", API_KEY)


if __name__ == "__main__":
    main()
