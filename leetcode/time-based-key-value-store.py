class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # run binary search here to find the closest value based on what the timestamp provided
        possible_vals = self.map[key]
        l, r = 0, len(possible_vals) - 1
        answer = ""

        while l <= r:
            m = (l + r) // 2

            # m is at the timestamp we're searching for
            if possible_vals[m][1] == timestamp:
                return possible_vals[m][0]
            
            if possible_vals[m][1] < timestamp:
                answer = possible_vals[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return answer

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)