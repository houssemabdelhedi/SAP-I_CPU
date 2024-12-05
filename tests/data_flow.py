# Initialize components
from components.bus import Bus
from components.register import Register


bus = Bus(width=8)
reg_a = Register(name="A")
reg_b = Register(name="B")

# Step 1: Load a value into RegA
reg_a.enable_load()
reg_a.load(42)  # Load the value 42 into register A
print(f"RegA value after load: {reg_a.value}")  # Expect 42

# Step 2: Output RegA's value to the bus
reg_a.enable_output()  # Place RegA's value on the bus
print(f"Bus value after RegA output: {bus.read()}")  # Expect 42

# Step 3: Load the value from the bus into RegB
reg_b.load(bus.read())  # RegB loads the value from the bus
print(f"RegB value after loading from bus: {reg_b.value}")  # Expect 42

# Step 4: Cleanup (disable RegA output)
reg_a.disable_output()
print(f"Bus value after RegA output disabled: {bus.read()}")  # Expect 0
