from collections import Counter

class B:
    @staticmethod
    def solution(a: list[int]) -> int:
        if not a:
            return -1

        edge = len(a) // 2
        frequency = Counter()
        dominator = None

        for i, num in enumerate(a):
            frequency[num] += 1
            if frequency[num] > edge:
                dominator = num
                break

        if dominator is not None:
            # Find the first occurrence of the dominator
            return a.index(dominator)
        return -1
