import itertools
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        top = [1, 2, 4, 8]
        bottom = [1, 2, 4, 8, 16, 32]
        for i in range(0, num+1):
            print(i)
            hours = list(map(lambda x: sum(x), itertools.combinations(top, i)))
            minutes = list(map(lambda x: sum(x), itertools.combinations(bottom, num-i)))
            
            print(hours, minutes)
            # if len(hours) == 0: hours = [0]
            # if len(minutes) == 0: minutes = [0]
            for h in hours:
                for m in minutes:
                    if 0 <= h and h <= 11 and 0 <= m and m <= 59:
                        # print(h, m)
                        result.append("%s:%02d" %(h, m))
        return result
        

s = Solution()
print (s.readBinaryWatch(8))