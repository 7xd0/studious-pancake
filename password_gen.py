def generate_passwords(start, end, even=None):
    """
    Generate a list of numeric passwords based on range.
    If even=True → only even numbers
    If even=False → only odd numbers
    If even=None → all numbers
    """
    passwords = []
    for num in range(start, end + 1):
        if even is None:
            passwords.append(str(num))
        elif even and num % 2 == 0:
            passwords.append(str(num))
        elif not even and num % 2 != 0:
            passwords.append(str(num))
    return passwords


def main():
    print("🔐 Password Range Generator")
    try:
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
    except ValueError:
        print("❌ Please enter valid integers.")
        return

    mode = input("Choose type (all / even / odd): ").strip().lower()
    even = None
    if mode == "even":
        even = True
    elif mode == "odd":
        even = False

    passwords = generate_passwords(start, end, even)
    
    print(f"\nGenerated {len(passwords)} passwords:")
    for p in passwords:
        print(p)

    save = input("\n💾 Do you want to save them to a file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (e.g., passwords.txt): ")
        with open(filename, "w") as f:
            f.write("\n".join(passwords))
        print(f"[✔] Passwords saved to {filename}")

if __name__ == "__main__":
    main()
