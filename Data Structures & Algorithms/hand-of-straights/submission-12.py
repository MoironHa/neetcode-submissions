class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = defaultdict(int)
        for card in hand:
            freq[card] += 1
        groups = len(hand) // groupSize
        hand.sort()
        for _ in range(groups):
            for key in hand:
                if freq[key] > 0:
                    target = key
                    break
            for i in range(groupSize):
                if target in freq and freq[target] > 0:
                    freq[target] -= 1
                    target += 1
                    continue
                return False
        return True