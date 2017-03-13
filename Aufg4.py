
def checkIfPalindrome(n):
    b = str(n)
    isPalindrome = True
    for idx, digit in enumerate(b):
        if b[idx] is not b[-1-idx]:
            isPalindrome = False;
            break;
        if idx >= len(b)/2:
            break;
    return isPalindrome

palindromes = []

for i in range (999, 100, -1):
    for j in range (999, i, -1):
        prod = i*j
        if checkIfPalindrome(prod):
            print(i, j, prod)
            palindromes.append(prod)

print(max(palindromes))
