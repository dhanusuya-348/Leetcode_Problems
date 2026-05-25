# class Solution(object):
#     def totalFruit(self, fruits):
#         maxcount = 0
#         for i in range(len(fruits)):
#             count = 0
#             set1 = set()
#             for j in range(i, len(fruits)):
#                 if fruits[j] in set1 or len(set1) < 2:
#                     set1.add(fruits[j])
#                     count += 1
#                 else:
#                     break
#             maxcount = max(maxcount, count)
#         return maxcount
        
class Solution(object):

    def totalFruit(self, fruits):

        left = 0
        basket = {}
        maxcount = 0

        for right in range(len(fruits)):

            # add current fruit
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # shrink window if invalid
            while len(basket) > 2:

                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            # valid window length
            maxcount = max(maxcount, right - left + 1)

        return maxcount