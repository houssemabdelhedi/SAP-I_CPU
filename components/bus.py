class Bus:
    """
    A Bus class to simulate a shared communication path between components.
    - Only one component can write to the bus at any given time.
    - Multiple components can read from the bus.
    """

    def __init__(self, width):
        """
        Initialize the Bus.
        :param width: The number of bits the Bus can handle (e.g., 8 for an 8-bit bus).
        """
        self.width = width
        self.value = 0  # The value currently on the Bus
        self.writer = None  # Keeps track of which component is writing to the Bus

    def write(self, component_name, value):
        """
        Write a value to the Bus.
        :param component_name: The name of the component writing to the Bus.
        :param value: The value to write.
        :raises Exception: If another component is already writing to the Bus.
        """
        if self.writer is not None and self.writer != component_name:
            raise Exception(f"Bus conflict! {self.writer} is already writing to the Bus.")

        if value >= 2 ** self.width:
            raise ValueError(f"Value {value} exceeds the bus width of {self.width} bits.")

        self.value = value
        self.writer = component_name

    def read(self):
        """
        Read the current value on the Bus.
        :return: The value on the Bus.
        """
        return self.value

    def release(self, component_name):
        """
        Release control of the Bus from a writing component.
        :param component_name: The name of the component releasing the Bus.
        :raises Exception: If the component trying to release is not the current writer.
        """
        if self.writer != component_name:
            raise Exception(f"{component_name} cannot release the Bus because it is not the writer.")

        self.writer = None

# Example usage:
bus = Bus(width=8)  # Create an 8-bit Bus

# Component A writes to the Bus
bus.write("ComponentA", 42)
print(f"Bus Value: {bus.read()}")  # Output: Bus Value: 42

# Component A releases the Bus
bus.release("ComponentA")

# Component B tries to write
bus.write("ComponentB", 85)
print(f"Bus Value: {bus.read()}")  # Output: Bus Value: 85

# Component B releases the Bus
bus.release("ComponentB")
