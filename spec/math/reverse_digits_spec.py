from mamba import description, context, it
from expects import expect, equal
from problems.math.reverse_digits import reverse_digits

with description('Math') as self:
    with context('when reversing digits'):
        with it('should reverse the digits'):
            expect(reverse_digits(4242)).to(equal(2424))
        with it('should reverse negative digits'):
            expect(reverse_digits(-413)).to(equal(-314))
            pass
        with it('should not return octals'):
            expect(reverse_digits(3210)).to(equal(123))
            pass

