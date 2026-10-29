class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            curr = people[r] + people[l]
            if people[r] == limit or curr > limit:
                count += 1
                r -= 1
                continue
            # while l <= r and curr <= limit:
            #     l += 1
            #     curr += people[l]
            count += 1
            r -= 1
            l += 1
        return count