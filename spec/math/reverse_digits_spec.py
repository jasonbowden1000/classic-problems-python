from mamba import description, it
from expects import expect, equal
from problems.math.reverse_digits import reverse_digits

with description('Reversing digits') as self:
    with it('should reverse positive numbers'):
        expect(reverse_digits(4242)).to(equal(2424))
    with it('should reverse negative numbers'):
        expect(reverse_digits(-413)).to(equal(-314))
    with it('should not return octals for numbers ending in zero'):
        expect(reverse_digits(3210)).to(equal(123))

