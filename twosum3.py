class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.numbers = []
    def add(self, number):
        # write your code here
        self.numbers.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        seen = set()
        for num in self.numbers:
            diff = value - num
            if diff in seen:
                return True
            seen.add(num)
        return False
# Create an instance of the TwoSum class
two_sum_instance = TwoSum()

# Add numbers to the instance
two_sum_instance.add(1)
two_sum_instance.add(3)
two_sum_instance.add(5)

# Check if there exists a pair of numbers that sum to 4
result1 = two_sum_instance.find(4)
print(result1)  # Should print True, because 1 + 3 = 4

# Check if there exists a pair of numbers that sum to 7
result2 = two_sum_instance.find(7)
print(result2)  # Should print False, as there's no pair that sums to 7

                