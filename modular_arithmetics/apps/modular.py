# modular.py
from functools import total_ordering


@total_ordering
class Mod:
    def __init__(self, value: int, modulus: int):
        if not isinstance(value, int):
            raise TypeError(
                "Unsupported type for value, it must be an integer, whole number."
            )
        if not isinstance(modulus, int):
            raise TypeError(
                "Unsupported type for modulus, it must be an integer, whole number."
            )
        if modulus <= 0:
            raise ValueError("Modulus must be greater than zero.")
        else:
            self._value = value
            self._modulus = modulus

    @property
    def value(self):
        """read-only property"""
        return self._value % self._modulus

    @property
    def modulus(self):
        """read-only property"""
        return self._modulus

    def __repr__(self):
        return f"Mod(value={self.value}, modulus={self.modulus})"

    def convert_integer_to_modular_and_check_mudulus_the_same(self, other):
        if isinstance(other, int):
            other = Mod(other, self.modulus)
        if isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError("Modulus in the objects must be the same.")
            return other
        #         return NotImplemented
        # Alternatively
        raise TypeError("Incompatable types")

    def __eq__(self, other):
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        return self.value == other.value

    def __lt__(self, other):
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        return self.value < other.value

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __add__(self, other):
        # print("__add__ called...")
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        added_value = self._value.__add__(other._value)
        return Mod(added_value, self.modulus)

    def __iadd__(self, other):
        # print("__iadd__ called...")
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        self._value = (self._value + other._value) % self.modulus
        return self

    def __sub__(self, other):
        # print("__sub__ called...")
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        substructed_value = self._value.__sub__(other._value)
        return Mod(substructed_value, self.modulus)

    def __isub__(self, other):
        # print("__isub__ called...")
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        self._value = (self._value - other._value) % self.modulus
        return self

    def __mul__(self, other):
        # print("__mul__ called...")
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        multiplied_value = self._value.__mul__(other._value)
        return Mod(multiplied_value, self.modulus)

    def __imul__(self, other):
        # print("__imul__ called...")
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        self._value = (self._value * other._value) % self.modulus
        return self

    def __pow__(self, other):
        # print("__pow__ called...")
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        powered_value = self._value**other._value
        return Mod(powered_value, self.modulus)

    def __ipow__(self, other):
        # print("__ipow__ called...")
        other = self.convert_integer_to_modular_and_check_mudulus_the_same(other)
        self._value = (self._value**other._value) % self.modulus
        return self

    def __int__(self):
        return self.value

    def __neg__(self):
        return Mod(-self.value, self.modulus)
