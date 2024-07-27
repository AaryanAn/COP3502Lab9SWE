def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        userOption = int(input('\nPlease enter an option: '))
        if userOption == 1:
            encodePass = input("Please enter your password to encode: ")
            encode()
        
        elif userOption == 2:
            print(f"The encoded password is {encode(encodePass)}, and the original password is {encodePass}.")
            decode()

        elif userOption == 3:
            break
        
def decode(password):
    ans = ""
    for val in password:
        ans += str(int(val) - 3)
    return ans

def encode(password):
    ans = ""
    for val in range(len(password)):
        ans += str(int(val) + 3)
    return ans

if __name__ == '__main__':
    main()


# Jerry Payne