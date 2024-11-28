from register import Register

# Create a register
reg_a = Register("A")

# Test enabling and disabling load
reg_a.enable_load()
reg_a.load(10)  # Load a value when load is enabled
print(reg_a)  # Expected: A: 00001010 | Output Disabled | Load Enabled | No Overflow

reg_a.disable_load()
reg_a.load(20)  # Attempt to load when load is disabled
print(reg_a)  # Expected: A: 00001010 (unchanged) | Output Disabled | Load Disabled | No Overflow

# Test enabling and disabling output
reg_a.enable_output()
print(f"Output Enabled: {reg_a.get()}")  # Expected: 10
reg_a.disable_output()
print(f"Output Disabled: {reg_a.get()}")  # Expected: None
