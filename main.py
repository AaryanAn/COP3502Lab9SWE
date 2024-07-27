def main():
    encoded_password = None
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        userOption = int(input('\nPlease enter an option: '))
        if userOption == 1:
            encodePass = input("Please enter your password to encode: ")
            encoded_password = encode(encodePass)
            print(f"Your encoded password is: {encoded_password}")

        elif userOption == 2:
            if encoded_password is None:
                print("No encoded password found. Please encode a password first.")
            else:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif userOption == 3:
            break


def decode(password):
    ans = ""
    for val in password:
        ans += str(int(val) - 3)
    return ans


def encode(password):
    ans = ""
    for val in password:
        ans += str(int(val) + 3)
    return ans


if __name__ == '__main__':
    main()

# Jerry Payne
