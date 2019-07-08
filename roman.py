import random
from typing import Tuple


class Roman(object):

    _symbol = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 5000: 'V^', 10000: 'X^'}
    _convention = {0: [], 1: [0], 2: [0, 0], 3: [0, 0, 0], 4: [0, 1],
                   5: [1], 6: [1, 0], 7: [1, 0, 0], 8: [1, 0, 0, 0], 9: [0, 2]}
    _basic_romans = {'I': [1, 1], 'II': [1, 2], 'III': [1, 3], 'IV': [1, 4], 'V': [1, 5],
                     'VI': [1, 6], 'VII': [1, 7], 'VIII': [1, 8], 'IX': [1, 9],
                     'X': [10, 1], 'XX': [10, 2], 'XXX': [10, 3], 'XL': [10, 4], 'L': [10, 5],
                     'LX': [10, 6], 'LXX': [10, 7], 'LXXX': [10, 8], 'XC': [10, 9],
                     'C': [100, 1], 'CC': [100, 2], 'CCC': [100, 3], 'CD': [100, 4], 'D': [100, 5],
                     'DC': [100, 6], 'DCC': [100, 7], 'DCCC': [100, 8], 'CM': [100, 9],
                     'M': [1000, 1], 'MM': [1000, 2], 'MMM': [1000, 3], 'MV^': [1000, 4], 'V^': [1000, 5],
                     'V^M': [1000, 6], 'V^MM': [1000, 7], 'V^MMM': [1000, 8], 'MX^': [1000, 9]}
    _cache_decimal = {}
    _cache_roman = {}
    _CASH_LIMIT = 10000000  # prevent memory overflow

    @staticmethod
    def _get_symbol(level: int, digit: int) -> str:

        tags = ''
        while level > 1000:
            level //= 1000
            tags += '^'
        symbols = [Roman._symbol[level], Roman._symbol[5 * level], Roman._symbol[10 * level]]
        result = ''
        for idx in Roman._convention[digit]:
            result += symbols[idx] + tags
        return result

    @staticmethod
    def _get_digit(roman: str) -> Tuple[int, int, str]:

        # collect up to 4 symbols and count carets
        buffer = ''
        car_counters = [0, 0, 0, 0]
        remainders = [0, 0, 0, 0]
        rem = 0
        for character in roman:
            if character == '^':
                car_counters[len(buffer) - 1] += 1
            else:
                if len(buffer) > 0:
                    remainders[len(buffer) - 1] = rem
                if len(buffer) >= 4:
                    break
                buffer += character
            rem += 1
        remainders[len(buffer) - 1] = rem
        for size in range(len(buffer), 0, -1):
            deduct = min(car_counters[0:size])
            factor = 1
            for times in range(deduct):
                factor *= 1000
            symbol = ''
            for char_index in range(size):
                symbol += buffer[char_index] + (car_counters[char_index] - deduct) * '^'

            if symbol in Roman._basic_romans:
                level = Roman._basic_romans[symbol][0] * factor
                digit = Roman._basic_romans[symbol][1]
                reminder = roman[remainders[size - 1]:]
                return level, digit, reminder

        raise ValueError('Not found')

    @staticmethod
    def convert_to_roman(number: int) -> str:
        """
        Convert a decimal integer to a Roman numeral string

        :param number: a positive integer
        :return: the Roman numeral
        :raises ValueError: if the number is zero or negative
        """
        if number < 1:
            raise ValueError(
                'The ancient Romans did not recognize 0 as a number neither did they include negative numbers')
        if number in Roman._cache_decimal:
            return Roman._cache_decimal[number]
        else:
            result = ''
            level = 1
            for digit in reversed(str(number)):
                result = Roman._get_symbol(level=level, digit=int(digit)) + result
                level *= 10

            if len(Roman._cache_decimal) < Roman._CASH_LIMIT:
                Roman._cache_decimal[number] = result
                Roman._cache_roman[result] = number

            return result

    @staticmethod
    def convert_to_decimal(roman: str) -> int:
        """
        Convert a Roman numeral to a decimal

        :param roman: a Roman numeral
        :return: the resulting decimal
        :raises ValueError: if the string is not an extended Roman numeral
        """
        if not roman:
            return 0

        roman = roman.upper()
        if roman in Roman._cache_roman:
            return Roman._cache_roman[roman]

        if 'I^' in roman:
            raise ValueError('Not found')  # I^ is represented by M

        remainder = roman
        number = 0
        prev_level = -1
        while remainder:
            level, digit, remainder = Roman._get_digit(remainder)
            if prev_level < 0:
                prev_level = level
            else:
                if level >= prev_level:
                    raise ValueError('Wrong level')
                prev_level = level
            number += digit * level

        if len(Roman._cache_decimal) < Roman._CASH_LIMIT:
            Roman._cache_decimal[number] = roman
            Roman._cache_roman[roman] = number

        return number


def main() -> int:

    do_the_random = False
    if do_the_random:
        for idx in range(1, 1000):
            number = random.randint(1, 9999999)
            print('{} = {}'.format(number, Roman.convert_to_roman(number=number)))
    else:
        test_numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 14, 15, 16, 19, 20, 21, 29, 30, 40, 50, 60, 70, 90, 100,
                        110, 111, 119, 120, 140, 149, 150, 199, 200, 300, 400, 500, 600, 700, 900, 999, 1000,
                        1499, 1500, 1501, 1900, 1999, 2222, 2999, 3333, 3999, 4444, 4999, 5555, 5999, 6666,
                        6999, 7777, 7999, 8888, 8999, 9999, 10000, 10001, 10004, 10005, 10006, 10009, 10010,
                        10019, 10022, 10029, 10033, 10039,
                        10044, 10049, 10055, 10059, 10066, 10069, 10077, 10079, 10089, 10099, 10100, 10111, 10199,
                        10222, 10333, 10444, 10555, 10666, 10777, 10888, 10999, 11111, 12222, 13333, 14444, 15555,
                        16666, 17777, 18888, 19999, 20000, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999,
                        100000, 111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888, 999999, 1000000,
                        999999999]

        test_romans = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VIII', 'IX',
                       'X', 'XI', 'XIV', 'XV', 'XVI', 'XIX',
                       'XX', 'XXI', 'XXIX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'XC',
                       'C', 'CX', 'CXI', 'CXIX', 'CXX', 'CXL', 'CXLIX', 'CL', 'CXCIX', 'CC', 'CCC', 'CD',
                       'D', 'DC', 'DCC', 'CM', 'CMXCIX',
                       'M', 'MCDXCIX', 'MD', 'MDI', 'MCM', 'MCMXCIX', 'MMCCXXII', 'MMCMXCIX', 'MMMCCCXXXIII',
                       'MMMCMXCIX', 'MV^CDXLIV', 'MV^CMXCIX', 'V^DLV', 'V^CMXCIX', 'V^MDCLXVI', 'V^MCMXCIX',
                       'V^MMDCCLXXVII', 'V^MMCMXCIX', 'V^MMMDCCCLXXXVIII', 'V^MMMCMXCIX', 'MX^CMXCIX',
                       'X^', 'X^I', 'X^IV', 'X^V', 'X^VI', 'X^IX', 'X^X', 'X^XIX', 'X^XXII', 'X^XXIX', 'X^XXXIII',
                       'X^XXXIX', 'X^XLIV', 'X^XLIX', 'X^LV', 'X^LIX', 'X^LXVI', 'X^LXIX', 'X^LXXVII', 'X^LXXIX',
                       'X^LXXXIX', 'X^XCIX', 'X^C', 'X^CXI', 'X^CXCIX', 'X^CCXXII', 'X^CCCXXXIII', 'X^CDXLIV',
                       'X^DLV', 'X^DCLXVI', 'X^DCCLXXVII', 'X^DCCCLXXXVIII', 'X^CMXCIX', 'X^MCXI', 'X^MMCCXXII',
                       'X^MMMCCCXXXIII', 'X^MV^CDXLIV', 'X^V^DLV', 'X^V^MDCLXVI', 'X^V^MMDCCLXXVII',
                       'X^V^MMMDCCCLXXXVIII', 'X^MX^CMXCIX',
                       'X^X^', 'X^X^MMCCXXII', 'X^X^X^MMMCCCXXXIII', 'X^L^MV^CDXLIV',
                       'L^V^DLV', 'L^X^V^MDCLXVI', 'L^X^X^V^MMDCCLXXVII', 'L^X^X^X^V^MMMDCCCLXXXVIII',
                       'X^C^MX^CMXCIX',
                       'C^', 'C^X^MCXI', 'C^C^X^X^MMCCXXII', 'C^C^C^X^X^X^MMMCCCXXXIII', 'C^D^X^L^MV^CDXLIV',
                       'D^L^V^DLV', 'D^C^L^X^V^MDCLXVI', 'D^C^C^L^X^X^V^MMDCCLXXVII',
                       'D^C^C^C^L^X^X^X^V^MMMDCCCLXXXVIII', 'C^M^X^C^MX^CMXCIX',
                       'M^', 'C^^M^^X^^C^^M^X^^C^M^X^C^MX^CMXCIX']

        for roman_str in test_romans:
            print(Roman.convert_to_decimal(roman_str))

        print(Roman.convert_to_decimal('V^MMM'))
        print(Roman.convert_to_decimal('V^MMMDCCLXI'))
        try:
            print(Roman.convert_to_decimal('DCCMM'))
        except ValueError as ex:
            print(str(ex))
        try:
            print(Roman.convert_to_decimal('DCCDC'))
        except ValueError as ex:
            print(str(ex))
        try:
            print(Roman.convert_to_decimal('M^'))
        except ValueError as ex:
            print(str(ex))

        for idx in test_numbers:
            print('{} = {}'.format(idx, Roman.convert_to_roman(number=idx)))

    return 0


if __name__ == '__main__':
    exit(main())
