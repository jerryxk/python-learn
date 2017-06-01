#casesarTest.py

cipher = "iodj{fe1e684g8944d92ei134g3g2f42gf27f}"

def decoding(cipher):
    '''try to decoding cipher and show all result'''
    def transform(key):
        for alpha in key:
            beta = key[alpha]
            beta = chr(ord(beta) + 1)
            if ord(beta) > ord('~'):
                beta = '!'
            key[alpha] = beta
        return key

    key = {}
    cipherTest = ''
    for alpha in range(ord('!'), ord('!')+94):
        key[chr(alpha)] = chr(alpha)
        #print 
    for i in range(94):
        cipherTest = ''
        for j in range(len(cipher)):
            #print len(cipher)
            cipherTest += key[cipher[j]]
        key = transform(key)
        print('{0:2} : {1}'.format(i, cipherTest))

decoding(cipher)
print ord('!')