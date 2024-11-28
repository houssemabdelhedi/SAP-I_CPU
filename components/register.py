class Register:
    def __init__(self, name, size=8):
        """
        Initialize the register.
        :param name: Name of the register (e.g., 'A', 'B').
        :param size: Size of the register in bits.
        """
        self.name = name
        self.size = size
        self.value = 0  # Initial value of the register
        self.output_enabled = False  # Output enable flag
        self.load_enabled = False  # Load enable flag
        self.overflow_flag = False  # Overflow flag

    def load(self, value, clock_signal=True):
        """
        Load a value into the register if load is enabled and synchronized with a clock signal.
        :param value: The integer value to load.
        :param clock_signal: Simulate synchronization with a clock pulse.
        """
        if self.load_enabled and clock_signal:
            max_value = (1 << self.size) - 1
            self.overflow_flag = value > max_value
            self.value = value & max_value  # Ensure value fits the register size

 #   def clear(self, clock_signal=True):
        #"""Clear the register (set value to 0), synchronized with a clock signal."""
        #if clock_signal:
            #self.value = 0
            #self.overflow_flag = False

    def enable_output(self):
        """Enable the register's output."""
        self.output_enabled = True

    def disable_output(self):
        """Disable the register's output."""
        self.output_enabled = False

    def enable_load(self):
        """Enable the register's load functionality."""
        self.load_enabled = True

    def disable_load(self):
        """Disable the register's load functionality."""
        self.load_enabled = False

    def get(self):
        """
        Return the current value of the register if output is enabled.
        :return: The register's value or None if output is disabled.
        """
        if self.output_enabled:
            return self.value
        else:
            return None

    def __str__(self):
        """
        String representation of the register's state.
        :return: The binary representation of the value and flags.
        """
        output_status = "Output Enabled" if self.output_enabled else "Output Disabled"
        load_status = "Load Enabled" if self.load_enabled else "Load Disabled"
        overflow_status = "Overflow" if self.overflow_flag else "No Overflow"
        return (f"{self.name}: {bin(self.value)[2:].zfill(self.size)} | "
                f"{output_status} | {load_status} | {overflow_status}")
