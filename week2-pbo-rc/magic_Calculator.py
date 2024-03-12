import math

class SimpleCalculator:
    def __init__(self, value=0):
        self.value = value

    def __repr__(self):
        return f"SimpleCalculator(value={self.value})"

    def __add__(self, other):
        return SimpleCalculator(self.value + other.value)

    def __sub__(self, other):
        return SimpleCalculator(self.value - other.value)

    def __mul__(self, other):
        return SimpleCalculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return SimpleCalculator(self.value / other.value)
        else:
            raise ValueError("Cannot divide by zero")

    def __pow__(self, exponent):
        return SimpleCalculator(self.value ** exponent.value)

    def log(self, base):
        if self.value > 0 and base.value > 0:
            return SimpleCalculator(math.log(self.value, base.value))
        else:
            raise ValueError("Both value and base must be greater than 0")

# Example usage:
# Creating instances of SimpleCalculator
calc1 = SimpleCalculator(8)
calc2 = SimpleCalculator(4)

# Performing operations using dunder methods
add_result = calc1 + calc2
sub_result = calc1 - calc2
mul_result = calc1 * calc2
div_result = calc1 / calc2
pow_result = calc1 ** SimpleCalculator(2)
log_result = calc1.log(SimpleCalculator(2))

# Displaying results
print(f"Addition: {add_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")
print(f"Exponentiation: {pow_result}")
print(f"Logarithm: {log_result}")
