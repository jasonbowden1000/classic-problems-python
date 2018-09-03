from mamba import description, it
from expects import expect, equal
from problems.string.roman import roman_to_arabic, arabic_to_roman, is_roman

with description('roman_to_arabic') as self:
    with it('should return the Arabic representation of a Roman numeral') as self:
        expect(roman_to_arabic('MDCCCLXVI')).to(equal(1866))
        expect(roman_to_arabic('XIV')).to(equal(14))
        expect(roman_to_arabic('LXXXIX')).to(equal(89))
        expect(roman_to_arabic('XCI')).to(equal(91))
        expect(roman_to_arabic('DCCCXC')).to(equal(890))
        expect(roman_to_arabic('MCMLXXXIX')).to(equal(1989))
with description('arabic_to_roman') as self:
    with it('should return the Roman representation of an Arabic numeral') as self:
        pass
with description('is_roman') as self:
    with it('should not accept more than three consecutive numerals') as self:
        pass
    with it('should allow valid exceptions of order') as self:
        pass
    with it('should disallow biconsecutive valid order exceptions') as self:
        pass
    with it('should accept valid Roman numerals') as self:
        pass
