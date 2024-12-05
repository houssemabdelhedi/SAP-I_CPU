class ALU:
    """
    An Arithmetic Logic Unit (ALU) that performs basic arithmetic operations: addition and subtraction.
    """

    def __init__(self, width):
        """
        Initialize the ALU.
        :param width: The number of bits the ALU can process (e.g., 8 for an 8-bit ALU).
        """
        self.width = width
        self.result = 0  # Stores the result of the last operation
        self.zero_flag = False  # True if the result is zero
        self.carry_flag = False  # True if the operation resulted in a carry or borrow

    def operate(self, operand1, operand2, subtract=False):
        """
        Perform addition or subtraction based on the subtract flag.
        :param operand1: The first operand.
        :param operand2: The second operand.
        :param subtract: If True, perform subtraction; otherwise, perform addition.
        :return: The result of the operation.
        """
        if subtract:
            result = operand1 - operand2
        else:
            result = operand1 + operand2

        max_value = (1 << self.width) - 1  # Maximum value for the given width

        # Set carry/borrow flag
        if subtract:
            self.carry_flag = result < 0  # Borrow occurred
        else:
            self.carry_flag = result > max_value  # Carry occurred

        self.result = result & max_value  # Mask to fit within the ALU width
        self.zero_flag = self.result == 0

        return self.result

# Example usage:
alu = ALU(width=8)  # Create an 8-bit ALU

# Perform some operations
print("Addition: ", alu.operate(10, 20))  # Output: 30
print("Subtraction: ", alu.operate(50, 20, subtract=True))  # Output: 30
