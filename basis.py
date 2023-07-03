class Base():
    """Standart numerical class for every base length from 2 to 36."""
    __digits = {"0": 0,
              "1": 1,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "A": 10,
              "B": 11,
              "C": 12,
              "D": 13,
              "E": 14,
              "F": 15,
              "G": 16,
              "H": 17,
              "I": 18,
              "J": 19,
              "K": 20,
              "L": 21,
              "M": 22,
              "N": 23,
              "O": 24,
              "P": 25,
              "Q": 26,
              "R": 27,
              "S": 28,
              "T": 29,
              "U": 30,
              "V": 31,
              "W": 32,
              "X": 33,
              "Y": 34,
              "Z": 35
              } 
    __digits_inverse = {}

    def __init__(self, value: str, base: int = 10) -> None:
        self.__base = base
        if base > len(self.__digits):
            raise ValueError(f"The maximum value of base is {len(self.__digits)}.")
        if base < 2:
            raise ValueError("The minimum value of base is 2.")
        self.__value = str(value).upper()
        if self.__value.count(",.") > 1:
            raise ValueError("The number cannot have multiple commas.")
        for index, digit in enumerate(self.__value):
            if digit == "-" and index == 0:
                continue
            if digit not in ",." and (digit not in self.__digits or self.__digits[digit] >= self.__base):
                raise ValueError("The number have invalid __digits.")
        for digit in self.__digits:
            self.__digits_inverse[self.__digits[digit]] = digit

    def decimal_to_base(self, number, base: int = None, max_length_after_comma: int = 8) -> str:
        """Converts a decimal number to a new given base."""
        if number < 0:
            negative = True
            number *= -1
        else:
            negative = False
        if base is None:
            base = self.__base
        if base > 36:
            raise ValueError("The maximum value of base is 36.")
        if base < 2:
            raise ValueError("The minimum value of base is 2.")
        if base == 10:
            return "-" + str(number) if negative else str(number)
        exp = 0
        while (base**exp < number):
            exp += 1
        new_value = ""
        exp -= 1
        while (number > 0 or exp > 0):
            if exp == - 1:
                new_value += "."
            new_value += str(self.__digits_inverse[number//(base**exp)])
            number -= (number//(base**exp))*(base**exp)
            if exp == max_length_after_comma*(-1):
                break
            exp -= 1
        return "-" + new_value if negative else new_value

    def __value_check(self) -> float:
        """Gets the decimal value of the number."""
        negative = self.__value[0] == "-"
        if self.__value.count(",.") > 1:
            raise ValueError("The number cannot have multiple commas.")
        try:
            commas_loc = self.__value.index(",")
        except:
            try:
                commas_loc = self.__value.index(".")
            except:
                commas_loc = len(self.__value)
        value = self.__value[:commas_loc] + self.__value[commas_loc + 1:] if commas_loc != len(self.__value) else self.__value[:]
        if negative:
            value = value[1:]
            commas_loc -= 1
        decimal_value = sum([self.__digits[digit]*(self.__base**(commas_loc - index - 1)) for index, digit in enumerate(value)])
        return decimal_value*(-1) if negative else decimal_value

    def base_conv(self, base: int, max_length_after_comma: int = 8) -> str:
        """Converts the value to a new given base."""
        if int(max_length_after_comma) != max_length_after_comma or max_length_after_comma < 0:
            raise ValueError("Invalid maximum length after comma value.")
        self.__value = self.decimal_to_base(self.__value_check(), base, max_length_after_comma)
        self.__base = base

    def __eq__(self, number) -> bool:
        if isinstance(number, Base):
            return self.__value_check() == number.__value_check()
        return self.__value_check() == number
        
    def __gt__(self, number) -> bool:
        if isinstance(number, Base):
            return self.__value_check() > number.__value_check()
        return self.__value_check() > number
        
    def __ge__(self, number) -> bool:
        if isinstance(number, Base):
            return self.__value_check() >= number.__value_check()
        return self.__value_check() >= number
        
    def __lt__(self, number) -> bool:
        if isinstance(number, Base):
            return self.__value_check() < number.__value_check()
        return self.__value_check() < number
        
    def __le__(self, number) -> bool:
        if isinstance(number, Base):
            return self.__value_check() <= number.__value_check()
        return self.__value_check() <= number
    
    def __ne__(self, number) -> bool:
        return not self.__eq__(number)

    def __pow__(self, exp):
        value = self.__value_check()**exp
        value = self.decimal_to_base(value)
        return Base(self.decimal_to_base(value), self.__base)

    def __add__(self, other):
        value = self.__value_check()
        if isinstance(other, Base):
            value += other.__value_check()
        else:
            value += other
        return Base(self.decimal_to_base(value), self.__base)
    
    def __sub__(self, other):
        value = self.__value_check()
        if isinstance(other, Base):
            value -= other.__value_check()
        else:
            value -= other
        return Base(self.decimal_to_base(value), self.__base)
    
    def __mul__(self, other):
        value = self.__value_check()
        if isinstance(other, Base):
            value *= other.__value_check()
        else:
            value *= other
        return Base(self.decimal_to_base(value), self.__base)
    
    def __truediv__(self, other):
        value = self.__value_check()
        if isinstance(other, Base):
            value /= other.__value_check()
        else:
            value /= other
        return Base(self.decimal_to_base(value), self.__base)
    
    def __floordiv__(self, num):
        value = self.__value_check()
        if isinstance(num, Base):
            return value // num.__value_check()
        else:
            return value // num
        
    def __mod__(self, num):
        value = self.__value_check()
        if isinstance(num, Base):
            return value % num.__value_check()
        else:
            return value % num

    def __str__(self) -> str:
        return self.__value + " on base " + str(self.__base)
        
    def __repr__(self) -> str:
        return f'{self.__value}"{self.__base}'

if __name__ == "__main__":
    a = Base("-AB,C", 13)
    a.base_conv(10)
    a.base_conv(13)
    print(a)
    print((a,))
