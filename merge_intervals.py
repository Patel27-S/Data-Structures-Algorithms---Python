# Leetcode 56

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        i = 0
        
        while i <= len(intervals)-2:
            
            # Overlapping condition
            if intervals[i][1] >= intervals[i+1][0]:
                # Overlapping has two ways, one of the ways is below
                # and otherwise the intervals[i] remains as it is.
                if intervals[i][1] <= intervals[i+1][1]:
                    intervals[i] = [intervals[i][0], intervals[i+1][1]]
                
                # After merging of the two arrays, we remove the next 
                # array.
                intervals.remove(intervals[i+1])
             
            else:
                # If there is no overlapping between the current and next array
                # then, the value of i is incremented or else it remains as it is.
                i += 1
        
        return intervals
