from mamba import description, it
from expects import expect, be_true, be_false
from problems.string.is_palindrome import is_palindrome

with description('Palindrome') as self:
    with it('should accept a basic palindromic word'):
        expect(is_palindrome('')).to(be_true)
        expect(is_palindrome('a')).to(be_true)
        expect(is_palindrome('rotator')).to(be_true)
        expect(is_palindrome('redder')).to(be_true)
    with it('should accept a capitalized palindromic word'):
        expect(is_palindrome('Madam')).to(be_true)
    with it('should accept a palindromic sentence with non-alphabetic characters'):
        expect(is_palindrome('A car, a man, a maraca')).to(be_true)
    with it('should reject non-palindromic strings'):
        expect(is_palindrome('jason')).to(be_false)
        expect(is_palindrome('dude')).to(be_false)
        expect(is_palindrome('axyza')).to(be_false)
