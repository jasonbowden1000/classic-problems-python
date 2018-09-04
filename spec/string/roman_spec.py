from mamba import description, it
from expects import expect, equal, be_an, be_none
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
        expect(arabic_to_roman(1666)).to(equal('MDCLXVI'));
        expect(arabic_to_roman(91)).to(equal('XCI'));
with description('is_roman') as self:
    with it('should not accept more than three consecutive numerals') as self:
        expect(is_roman('XXXX')).to(be_none)
    with it('should reject any sequential repetition of V, L, or D') as self:
        expect(is_roman('LL')).to(be_none)
        expect(is_roman('DDC')).to(be_none)
        expect(is_roman('XVV')).to(be_none)
    with it('should allow valid exceptions of order') as self:
        expect(is_roman('IV')).to(be_an(object))
        expect(is_roman('IX')).to(be_an(object))
        expect(is_roman('XC')).to(be_an(object))
        expect(is_roman('XL')).to(be_an(object))
        expect(is_roman('CD')).to(be_an(object))
        expect(is_roman('CM')).to(be_an(object))
        expect(is_roman('IC')).to(be_none)
        expect(is_roman('LC')).to(be_none)
        expect(is_roman('VX')).to(be_none)
        expect(is_roman('DM')).to(be_none)
    with it('should disallow biconsecutive valid order exceptions') as self:
        expect(is_roman('CDM')).to(be_none)
        expect(is_roman('IXC')).to(be_none)
        expect(is_roman('IVX')).to(be_none)
        expect(is_roman('XIXIX')).to(be_none)
        expect(is_roman('XVIV')).to(be_none)
        expect(is_roman('XIIV')).to(be_none)
        expect(is_roman('VIX')).to(be_none)
        expect(is_roman('XXC')).to(be_none)
        expect(is_roman('CCCXCCC')).to(be_none)
        expect(is_roman('LXL')).to(be_none)
        expect(is_roman('IXI')).to(be_none)
        expect(is_roman('IXXXI')).to(be_none)
    with it('should accept valid Roman numerals') as self:
        expect(is_roman('XXX')).to(be_an(object))
        expect(is_roman('XIV')).to(be_an(object))
        expect(is_roman('CXC')).to(be_an(object))
        expect(is_roman('XIX')).to(be_an(object))
