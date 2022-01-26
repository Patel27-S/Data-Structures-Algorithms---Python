
def sortedSquaredArray(array):
  output_array = []
  for element in array:
	  output_array.append(element*element)
  return sorted(output_array)

# Testing
print(sortedSquaredArray([1,2,3]))
print(sortedSquaredArray([7,4,5]))
