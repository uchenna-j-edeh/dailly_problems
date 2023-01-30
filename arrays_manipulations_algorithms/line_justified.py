    """Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

    """


class Solution:
    def line_justified(self, wordlist, k):
        count = 0
        newtext = ''
        nwt = list()
        for tx in wordlist:
            # count  = len(tx) + count + 1 # add one to take for space
            if count + len(tx) > k: # false, false, false,  true
                # new function to distribute spaces
                newtext = self.distribute_space(nwt, k, count) + newtext
                nwt =  list()
                if len(tx) + 1 > k:
                    nwt.append(tx + " ") # ToDo check it's less than k
                    count = k
                    continue
                else:
                    nwt.append(tx)
            else:
                nwt.append(tx + " ") # 'the ','quick ','brown'

            count  = len(tx) + count + 1 # add one to take for space # 4,6, 6

        return newtext

    def distribute_space(nwt, k, len_nwt): #
        if not len(nwt):
            return ""

        diff = len_nwt - k  % len(nwt)

        for i in range(len(diff)):
            nwt[i] = nwt[i] + " "

        return "".join(nwt)


solution = Solution()
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
print(solution.line_justified(words, k))

        




                
