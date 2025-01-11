#its the simple while problem but i failed to write but i try my best to understand the code 
# the best solution was
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        currIndex = 0
        i = 0
        # Keep Track of Current Letter Index for Arr
        while i < len(chars):
            currentLetter = chars[i]
            count = 0
            # Traverse and while we are on same char then add to count
            while(i < len(chars) and chars[i] == currentLetter):
                i += 1
                count += 1
            # Set current Letter in Arr then go to next index
            chars[currIndex] = currentLetter
            currIndex += 1
            # If Count
            if count > 1:
                for j in str(count):
                    chars[currIndex] = j
                    currIndex += 1
        return currIndex