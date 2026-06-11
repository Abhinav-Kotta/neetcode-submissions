class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.mapping[key]
        associated_pos = -1
        l, r = 0, len(values) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] < timestamp:
                associated_pos = mid
                l = mid + 1
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                return values[mid][0]

        return values[associated_pos][0] if associated_pos != -1 else ""
        
