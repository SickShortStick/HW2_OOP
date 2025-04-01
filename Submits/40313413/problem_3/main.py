from math import gcd, lcm

def find_denominator(number):
    denominator = 1
    while not number.is_integer():
        number *= 10
        denominator *= 10
    return denominator


class Fraction:
    
    numerator = 0
    denominator = 1
    
    in_float = 0

    def __init__(self, numerator = 0, denominator = 1):
        common_divisor = gcd(int(numerator), int(denominator))
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        self.in_float = numerator / denominator

    def set_value(self, number):
        denominator = find_denominator(number)
        common_divisor = gcd(int(number * denominator), denominator)
        self.numerator = (number * denominator) // common_divisor
        self.denominator = denominator // common_divisor
        self.in_float = number / denominator
        
    def __call__(self, *args, **kwds):
        return self.in_float

    def __mul__(self, number):
        if type(number) != Fraction:
            number = Fraction(number)
        common_divisor = gcd(self.numerator * number.numerator, self.denominator * number.denominator)
        return f'{(self.numerator * number.numerator) // common_divisor} / {((self.denominator * number.denominator) // common_divisor)}'

    def __truediv__(self, other_number):

        if type(other_number) != Fraction:
            number = Fraction()
            number.set_value(other_number)
        else:
            number = other_number

        new_number = Fraction(self.numerator * number.denominator, self.denominator * number.numerator)
        return f'{new_number.numerator} / {new_number.denominator}'

    def __sub__(self, other_number):

        if type(other_number) != Fraction:
            number = Fraction()
            number.set_value(other_number)
        else:
            number = other_number

        common_multiple = lcm(self.denominator, number.denominator)
        first_number_multiplier = common_multiple // self.denominator
        second_number_multiplier = common_multiple // number.denominator
        new_numerator = int(self.numerator * first_number_multiplier - number.numerator * second_number_multiplier)
        new_denominator = int(self.denominator * first_number_multiplier)
        new_fraction = Fraction(new_numerator, new_denominator)
        return f'{new_fraction.numerator} / {new_fraction.denominator}'

    def __add__(self, other_number):

        if type(other_number) != Fraction:
            number = Fraction()
            number.set_value(other_number)
        else:
            number = other_number
        common_multiple = lcm(self.denominator, number.denominator)
        first_number_multiplier = common_multiple // self.denominator
        second_number_multiplier = common_multiple // number.denominator
        new_numerator = int(self.numerator * first_number_multiplier + number.numerator * second_number_multiplier)
        new_denominator = int(self.denominator * first_number_multiplier)
        new_fraction = Fraction(new_numerator, new_denominator)
        return f'{new_fraction.numerator} / {new_fraction.denominator}'

    def __ne__(self, number):
        if type(number) != Fraction:
            number = Fraction(number)
        return True if self.in_float != number.in_float else False

    def __eq__(self, number):
        if type(number) != Fraction:
            number = Fraction(number)
        return True if self.in_float == number.in_float else False

    def __lt__(self, number):
        if type(number) != Fraction:
            number = Fraction(number)
        return True if self.in_float < number.in_float else False

    def __gt__(self, number):
        if type(number) != Fraction:
            number = Fraction(number)
        return True if self.in_float > number.in_float else False
    
    def __le__(self, number):
        if type(number) != Fraction:
            number = Fraction(number)
        return True if self.in_float <= number.in_float else False

    def __ge__(self, number):
        if type(number) != Fraction:
            number = Fraction(number)
        return True if self.in_float >= number.in_float else False

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'
f1 = Fraction() # Default value: 0 / 1
f2 = Fraction(12, 5)
f3 = Fraction(12, 9) # Simplified to: 4 / 3

print(f1) # Output: "0 / 1"
print(f2)
print(f3) # Output: "4 / 3"
print(f2 >= 2.4)