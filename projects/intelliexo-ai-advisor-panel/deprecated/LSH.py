import re
import math
import hashlib

### LSH to get a similarity score of two or more paragraphs/sentences

class shingler:
    def __init__(self, k):
        if k > 0:
            self.k = int(k)
        else:
            self.k = 10   
    #inner class utility
    def process_doc(self, document):
        return re.sub("( )+|(\n)+"," ",document).lower()

    def get_shingles(self, document):
        shingles = set()
        document= self.process_doc(document)
        for i in range(0, len(document)-self.k+1 ):
            shingles.add(document[i:i+self.k])
        return shingles

# the family of hash functions, in this case, is the same function (sha1) applied with a different salt.
class hashFamily:
    def __init__(self, i):
        self.resultSize = 8 # how many bytes we want back
        self.maxLen = 20 # how long can our salt be (in decimal)
        self.salt = str(i).zfill(self.maxLen)[-self.maxLen:]

    def get_hash_value(self, el_to_hash):
        return int(hashlib.sha1(str(el_to_hash).encode('utf-8') + self.salt.encode('utf-8')).hexdigest()[-self.resultSize:], 16)

# NOTE: we use sha1 to avoid installing and importing an external library, sacrificing performances. No crypto-hash is required for this use case.

import random
from random import randint, seed
class minhashSigner:
    def __init__(self, sig_size):
        self.sig_size=sig_size
        # Init the hash family of functions using a random salt
        random.seed(8)
        self.hash_functions = [hashFamily(randint(0,10000000000)) for i in range(0,sig_size)]
        # print("Hash functions: ", (self.hash_functions))

    def compute_set_signature(self, set_):
        set_sig = []
        for h_funct in self.hash_functions:
            min_hash = math.inf
            for el in set_:
                h = h_funct.get_hash_value(el)
                if h < min_hash:
                    min_hash = h

            set_sig.append(min_hash)

        return set_sig
    #return a list of lists that can be seen as the signature matrix
    def compute_signature_matrix(self, set_list):
        signatures = []
        for s in set_list:
            signatures.append( self.compute_set_signature(s) )
        return signatures


if __name__ == "__main__":
    doc = """serene because she meditated everyday and he gave me a video of her in her 
    last few weeks completely composed completely relaxed  and she and him had 
    been meditating for years.  Well, I said to him, you teach me.  He is a devout 
    Christian.  He was taught  by a man called La urence  Freeman ,   a Catholic.  His 
    guru was John Main a devout Catholic .   When I was in London, Ng Kok Song 
    introduced me to Laurence Freeman.   In fact , he is coming on Saturday to visit 
    Singapore, and we will do a meditation session.  T he problem  is to keep the 
    monkey mind from running off into all kinds of thoughts.  It is most difficult  to stay 
    focus ed on the mantra .  The discipline is to have a mantra which you keep 
    repeat ing in your innermost heart, no need to voice it over and over again 
    throughout the whole period  of meditation.  T he mantra they recommended was 
    a religious one.  Ma Ra Na Ta, four syllables.  Come To Me Oh Lord Jesus.  So I """

    doc2 = """grown older. It's a way to calm the mind, to focus on the present moment, and to find a sense of tranquility. 
    I've been meditating for about three years now, and I must say, it's been a game-changer for me.
    I was introduced to meditation by my friend Ng Kok Song, who's a devout Christian. He's been meditating for many years, 
    and he's taught me the basics. I've found that it's not just about sitting quietly and focusing on your breath, 
    but it's also about discipline. You need to be disciplined to sit still, to focus on your mantra, and to quiet the mind.
    I've chosen a mantra that's meaningful to me, "Ma Ra Na Ta," which is a Catholic prayer. It's not about the specific words, 
    but about the act of repeating them to yourself, to calm the mind and to focus on the present moment."""

    shingler_inst = shingler(2)
    shinglings = shingler_inst.get_shingles(doc)
    shinglings2 = shingler_inst.get_shingles(doc2)
    minhash_sig = minhashSigner(20).compute_signature_matrix([shinglings,shinglings2])
    set_sig_1 = set(minhash_sig[0])
    set_sig_2 = set(minhash_sig[1])
    jaccard_similarity_sig = len(set_sig_1.intersection(set_sig_2))/len(set_sig_1.union(set_sig_2))
    print(jaccard_similarity_sig)