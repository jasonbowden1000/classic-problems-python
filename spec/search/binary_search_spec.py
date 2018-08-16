from mamba import description, context, it
from expects import expect, equal, raise_error
from problems.search.binary_search import binary_search

with description('Binary Search') as self:
    with before.all:
        self.sorted_array = [ -13, -7, -7, 8, 8, 8, 8, 8, 8, 23, 33, 54, 91, 144, 1984, 1984, 2001 ]
    with context('when searching a sorted array'):
        with it('should return the index of an element'):
            expect(binary_search(self.sorted_array, 54)).to(equal(11))
            expect(binary_search(self.sorted_array, 2001)).to(equal(16))
            expect(binary_search(self.sorted_array, -13)).to(equal(0))
    with context('when searching a sorted array with duplicates'):
        with it('should return the index of the first element'):
            expect(binary_search(self.sorted_array, -7)).to(equal(1))
            expect(binary_search(self.sorted_array, 8)).to(equal(3))
            expect(binary_search(self.sorted_array, 1984)).to(equal(14))
    with context('when an element is not found'):
        with it('should throw a ValueError for the missing element'):
            expect(lambda: binary_search(self.sorted_array, 1)).to(raise_error(ValueError, '1 is not in list'))
            expect(lambda: binary_search(self.sorted_array, -20)).to(raise_error(ValueError, '-20 is not in list'))
            expect(lambda: binary_search(self.sorted_array, 3000)).to(raise_error(ValueError, '3000 is not in list'))
    with context('when searching an empty array'):
        with it('should throw a ValueError for the missing element'):
            expect(lambda: binary_search([], 3000)).to(raise_error(ValueError, '3000 is not in list'))
