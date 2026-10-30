class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = False
        second = False
        third = False
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                if triplets[i][0] == target[0]:
                    first = True
                if triplets[i][1] == target[1]:
                    second = True
                if triplets[i][2] == target[2]:
                    third = True
        return first and second and third