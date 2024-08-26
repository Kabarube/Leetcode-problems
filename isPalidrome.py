def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    string = str(x)
    reverse = string[::-1]

    if string != reverse:
        return False
    return True


x = 0
string = str(x)

if x >= 0:
    isPal = True
    for idx, i in enumerate(string[: len(string) // 2]):
        print(f"index: {idx}, number: {i}, case: {string[-(int(idx) + 1)]}")

        if i == string[-(int(idx) + 1)]:
            print(f"{i} is {string[-(int(idx) + 1)]}")
            isPal = True
        else:
            isPal = False
            break
    if isPal == False:
        print("Not a Palindrome")
    else:
        print("Palindrome")

else:
    print(False)
