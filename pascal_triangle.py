# Leetcode 118

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        resultant_list = []
        
        for idx in range(numRows):
            no_of_elements = idx + 1
            list_to_append = []
            
            for elementh in range(no_of_elements):
                if elementh == 0:
                    list_to_append.append(1)
                elif elementh == no_of_elements-1:
                    list_to_append.append(1)
                else:
                    list_to_append.append(resultant_list[idx-1][elementh-1]
                                         +resultant_list[idx-1][elementh])
                    
            resultant_list.append(list_to_append)
            
        return resultant_list
                    
