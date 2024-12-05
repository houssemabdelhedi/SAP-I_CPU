# Example usage:
from components.bus import Bus


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