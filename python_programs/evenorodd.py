
def iseven(n):
    rem = n%2
    if rem == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    n = 15
    if iseven(n):
        print("True")
    else:
        print("false")