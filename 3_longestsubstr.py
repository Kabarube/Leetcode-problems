def lengthOfLongestSubstring(s):
    """

    :type s: str

    :rtype: int
    """


# Generate a new sequence of characters, and check for repeating characters iteratively
s = "aabaab!bb"
counter = 0
substr = ""
substr_list = []


charSet = set()
l = 0
result = 0

for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
    charSet.add(s[r])
    result = max(result, r - l + 1)

charList = []
l = 0
res = 0

for r in range(len(s)):
    while s[r] in charList:
        charList.remove(s[l])
        l += 1
    charList.append(s[r])
    res = max(res, r - l + 1)

print(res)
# for char in s:
#     if char in substr:
#         idx = substr.index(char)

#         substr = substr[idx:]
#         print(substr)

#     else:
#         substr += char
#         substr_list.append(substr)
#         counter += 1


# max_len = -1
# for ele in substr_list:
#     if len(ele) > max_len:
#         max_len = len(ele)
#         longest_substr = ele

# str_length = len(longest_substr)

# print(f"string {longest_substr}, counter: {str_length}")
