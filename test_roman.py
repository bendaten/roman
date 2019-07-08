from unittest import TestCase

from roman import Roman


class TestRoman(TestCase):

    def test_conversion(self):  # happy path

        try:
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
            for idx in range(len(test_numbers)):
                self.assertEqual(test_romans[idx], Roman.convert_to_roman(test_numbers[idx]))

            Roman._cache_decimal.clear()  # clear the caches to really test the back conversion
            Roman._cache_roman.clear()

            for idx in range(len(test_romans)):
                self.assertEqual(test_numbers[idx], Roman.convert_to_decimal(test_romans[idx]))

            for idx in range(len(test_numbers)):  # test cache
                self.assertEqual(test_romans[idx], Roman.convert_to_roman(test_numbers[idx]))

        except ValueError as ex:
            self.fail('Failed with - {}'.format(ex))

    def test_exceptions(self):

        ancient = 'The ancient Romans did not recognize 0 as a number neither did they include negative numbers'
        try:
            _ = Roman.convert_to_roman(0)
            self.fail('Should get an exception for non-positive values')
        except ValueError as ex:
            self.assertEqual(ancient, str(ex))
        try:
            _ = Roman.convert_to_roman(-22)
            self.fail('Should get an exception for non-positive values')
        except ValueError as ex:
            self.assertEqual(ancient, str(ex))

        try:
            _ = Roman.convert_to_decimal('T')  # T unknown
            self.fail('Should get an exception for unrecognized characters')
        except ValueError as ex:
            self.assertEqual('Not found', str(ex))

        try:
            _ = Roman.convert_to_decimal('IIII')  # III is 3 and cannot be followed by anything
            self.fail('Should get an exception for unrecognized characters')
        except ValueError as ex:
            self.assertEqual('Wrong level', str(ex))

        try:
            # not following the convention - XX is 20 and cannot be followed by 50
            _ = Roman.convert_to_decimal('XXL')
            self.fail('Should get an exception for unrecognized characters')
        except ValueError as ex:
            self.assertEqual('Wrong level', str(ex))

        try:
            _ = Roman.convert_to_decimal('MMCCXXC')  # 2220 cannot be followed by 100
            self.fail('Should get an exception for unrecognized characters')
        except ValueError as ex:
            self.assertEqual('Wrong level', str(ex))

        try:
            _ = Roman.convert_to_decimal('I^')  # with the current convention I can never be followed by a ^
            self.fail('Should get an exception for unrecognized characters')
        except ValueError as ex:
            self.assertEqual('Not found', str(ex))

        try:
            _ = Roman.convert_to_decimal('V^MMMDCCCLXXXVIIIR')  # R unknown
            self.fail('Should get an exception for unrecognized characters')
        except ValueError as ex:
            self.assertEqual('Not found', str(ex))
