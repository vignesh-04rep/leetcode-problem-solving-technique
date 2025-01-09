# understand the code the actual code which i written was run the testcase but it not work on 
# the many test case i still waiting for clear under standing
# the code which written by me 
# was
# if (str1[i] or str2[i]) not in it:
#   it.append(str[i])
 
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])
    