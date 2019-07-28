import xxhash

maxint = 4611686018427387904

def MinHash(signature, n_hash=100, ix=0):
    minhash_value = maxint
    for el in signature:
            
            minhash_temp = xxhash.xxh32(el, ix).intdigest()
            if minhash_value > minhash_temp:
                minhash_value = minhash_temp
    return minhash_value


def MinHash_set(signature, n_hash=100):
    minhash_set = set()
    for i in range(n_hash):
        minhash_value = MinHash(signature, n_hash=100, ix=i)
        minhash_set.add(minhash_value)
    return minhash_set


def jaccard_sim(minhash1, minhash2):
    return len(minhash1.intersection(minhash2))*1.0/len(minhash1.union(minhash2))
