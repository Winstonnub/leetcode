class TimeMap:

    def __init__(self):
        self.hashmap = dict() # key, Value = array [(time, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(timestamp, value)]
        else:
            self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if not self.hashmap: return res
        if key not in self.hashmap: return res
        arr = sorted(self.hashmap[key])
        # Now we want to find the timestamp_prev that is closest to timestamp and before
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if timestamp < arr[mid][0]: # if what we picked is larger than the given time, we search the left side
                r = mid - 1
            elif timestamp > arr[mid][0]: # if what we picked is smaller than the given time, we save our result and search the right side
                res = arr[mid][1]
                l = mid + 1
            else:
                return arr[mid][1]
        return res
            
            

        
