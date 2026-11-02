# Campus Lost and Found Management System

# INTENTIONALLY HARDCODED API KEY
API_KEY = "ghp_a8F3kL9mQ2vR7xN4pT6wY1zB5cD8eG0hJ K2p".replace(" ", "")


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


if __name__ == "__main__":
    main()
