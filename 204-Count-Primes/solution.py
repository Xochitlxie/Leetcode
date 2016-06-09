class Solution:
        # @param {integer} n
        # @return {integer}
        def countPrimes(self, n):
            primes=range(2,n)
            for i in primes:
                for j in xrange(i*i,n,i):
                    primes[j-2]=0
            return len(primes)-primes.count(0)