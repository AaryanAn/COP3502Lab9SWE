

def decode(password):
    ans = ""
    for val in password:
        ans += str(int(val) - 3)
    return ans