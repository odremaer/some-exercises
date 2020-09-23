# def brackets_check(str):
#     b = 0
#     b1 = 0
#     b2 = 0
#     for let in str:
#         if let == '(':
#             b += 1
#         elif let == ')':
#             b -= 1
#
#         if let == '[':
#             b1 += 1
#         elif let == ']':
#             b1 -= 1
#
#         if let == '{':
#             b2 += 1
#         elif let == '}':
#             b2 -= 1
#         print(b,b1,b2)
#         if (b == 2) or (b1 == 2) or (b2 == 2):
#             break
#
#     return True if (b == 0 and b1 == 0 and b2 == 0) else False
#
#
#
#
#
#
# print(brackets_check('{[}]'))


# import collections
#
# def dictFromString(s):
#     d = collections.defaultdict(int)
#     for c in s:
#         d[c]+=1
#     print(d)
#     return d
#
# def areAnagrams(a,b):
#     return dictFromString(a) == dictFromString(b)
#
#
# print(areAnagrams('privet','tevirps'))


# def generate(cur, open, closed, n):
#     k = 0
#     if len(cur) == 2*n:
#         print(cur)
#         return
#     if open < n:
#         generate(cur+'(', open + 1, closed, n)
#     if closed < open:
#         generate(cur + ')', open, closed + 1, n)
#
# 
# def parens(n):
#     generate('',0,0,n)
#
#
# parens(3)

# class Solution:
#     def replaceElements(self, arr):
#         for i in range(0,len(arr)):
#             if i == (len(arr)-1):
#                 arr[i] = -1
#                 return arr
#
#             item = arr[i+1]
#             for j in range(i+2, len(arr)):
#                 if item < arr[j]:
#                     item = arr[j]
#             arr[i]=item
#         return arr
#
#
#
# obj = Solution()

# # class Solution:
# #     def longestPalindrome(self, s: str) -> str:
# #         slist = list(s)
# #         word = ''
# #         maxl = ''
# #         while len(slist) != 0:
# #             word = ''
# #             for i in slist:
# #                 word += i
# #                 if word == word[::-1] and len(maxl) < len(word):
# #                     maxl = word
# #             slist.pop(0)
# #         return maxl
# #
# # obj = Solution()
# # print(obj.longestPalindrome('bhfasabb'))
# #
# #
# # def palindrom(s):
# #     word = ''
# #     for i in range(1,len(s)):
# #         word += s[len(s)-i]
# #     word += s[0]
# #     return word
# #
# # print(palindrom('kak dela'))


# class Solution:
#     def __init__(self, a):
#         self.a = a
#         print(a)
#
# obj = Solution
# print(obj)
# obj(5)
