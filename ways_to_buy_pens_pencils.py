# Leetcode 2240

def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        # While understanding the solution in future :-
        # Consider this as Step 1
        def no_of_ways_for_a_particular_number_of_pens(total_): 
            diff = total_ - cost2
            count = 0
        
            while diff >= 0:
                count += 1
                diff -= cost2
            return count+1
        
        # Consider this as Step3
        # Now, finding the range of total number of pens possible with the amount
        # of money we have. Remember, no_of_pens below is indicative of not exactly
        # what it says.
        
        no_of_pens = []
        while total >= 0:
            no_of_pens.append(total)
            total -= cost1
        
        # Consider this as Step2
        # Now, finding total number of ways.
        total_no_of_ways = 0
        
        for total in no_of_pens:
            total_no_of_ways += no_of_ways_for_a_particular_number_of_pens(total)
            
        return total_no_of_ways
        
