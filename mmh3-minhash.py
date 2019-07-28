# Let's use MurmurHash3.
import mmh3

doc =  set(['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
             'estimating', 'the', 'similarity', 'between', 'documents'])

# We need to define a new hash function that outputs an integer that
# can be encoded in 32 bits.

def _hash_func(doc):
    return mmh3.hash64(doc)

# Use this function in MinHash constructor.
m = MinHash(hashfunc=_hash_func)

print(m)

m.hashvalues