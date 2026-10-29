class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rights = []
        for one in asteroids:
            if one > 0:
                rights.append(one)
                continue
            while rights and rights[len(rights) - 1] > 0:
                right = rights[len(rights) - 1]
                left = abs(one)
                if right == left:
                    rights.pop()
                    break
                elif right > left:
                    break
                else:
                    rights.pop()
            else:
                print(f"here for: {one}")
                rights.append(one)
        return rights