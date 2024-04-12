# Leetcode 551 

# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

 

# Example 1:

# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:

# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.


def student_attendance(attendance):

    # Check if there are more than 2 absences
    if attendance.count('A') >= 2:
        return False
    
    # Check for 3 consecutive lates
    if 'LLL' in s:
        return False
    
    return True

# Example usage:
print(check_record("PPALLP"))  # Output: True
print(check_record("PPALLL"))  # Output: False
