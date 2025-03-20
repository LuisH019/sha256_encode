k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

def rightRotate(n, rot):
    return (n >> rot) | ((n & ((1 << rot) - 1)) << (32 - rot))

def encodeChunk(chunk):
    i, j = 0, 0
    w = []
    w.append(0)
    shift = 24

    for i in range (64):
        w[j] = (chunk[i] << shift | w[j])
        shift -= 8

        if (i + 1) % 4 == 0:
            j += 1
            w.append(0)
            shift = 24

    while len (w) % 64 != 0:
        w.append(0)

    # print(w)

    i, j, k = 1, 14, 16
    deviations = [0] * 2

    while k < 64:
        deviations[0] = (rightRotate (w[i], 7) ^ rightRotate (w[i], 18) ^ (w[i] >> 3))
        deviations[1] = (rightRotate (w[j], 17) ^ rightRotate (w[j], 19) ^ (w[j] >> 10))

        # print(deviations)

        w[k] = (w[i - 1] + deviations[0] + w[j - 5] + deviations[1]) & 0xFFFFFFFF

        # print(k, ": ", w[k])

        i += 1
        j += 1
        k += 1

    # print(w)
    return w

def updateHash(hash, w):
    a = hash[0]
    b = hash[1]
    c = hash[2]
    d = hash[3]
    e = hash[4]
    f = hash[5]
    g = hash[6]
    h = hash[7]

    summmations = [0] * 2

    for i in range(64):
        maj = (a & b) ^ (a & c) ^ (b & c)

        summmations [0] = (rightRotate (a, 2) ^ rightRotate (a, 13) ^ rightRotate (a, 22))
        summmations [1] = (rightRotate (e, 6) ^ rightRotate (e, 11) ^ rightRotate (e, 25))

        ch = (e & f) ^ ((~e) & g)

        temp1 = (h + summmations[1] + ch + k[i] + w[i]) & 0xFFFFFFFF
        temp2 = (summmations[0] + maj) & 0xFFFFFFFF

        h = g & 0xFFFFFFFF
        g = f & 0xFFFFFFFF
        f = e & 0xFFFFFFFF
        e = (d + temp1) & 0xFFFFFFFF
        d = c & 0xFFFFFFFF
        c = b & 0xFFFFFFFF
        b = a & 0xFFFFFFFF
        a = (temp1 + temp2) & 0xFFFFFFFF

    # print ((h + hash[7]) & 0xFFFFFFFF)

    hash[0] = (a + hash[0]) & 0xFFFFFFFF
    hash[1] = (b + hash[1]) & 0xFFFFFFFF 
    hash[2] = (c + hash[2]) & 0xFFFFFFFF
    hash[3] = (d + hash[3]) & 0xFFFFFFFF
    hash[4] = (e + hash[4]) & 0xFFFFFFFF
    hash[5] = (f + hash[5]) & 0xFFFFFFFF
    hash[6] = (g + hash[6]) & 0xFFFFFFFF
    hash[7] = (h + hash[7]) & 0xFFFFFFFF

    return hash

def encode(original):
    messageBlock = [byte for char in original for byte in char.encode('utf-8')]

    size = (len (messageBlock)) * 8 

    messageBlock.append(128)

    while (len (messageBlock) * 8 + 64) % 512 != 0:
        messageBlock.append(0)

      
    sizeBlock = []

    while size > 0:
        sizeBlock.append((size % 256))
        size >>= 8 

    sizeBlock.reverse()

    while len (sizeBlock) % 8 != 0:
        sizeBlock = [0] + sizeBlock

    messageBlock += sizeBlock

    # print(messageBlock)

    i = 0
    hash = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

    while i < len (messageBlock):
        # print (i)

        chunk = messageBlock[i:i + 64]

        hash = updateHash(hash, encodeChunk(chunk)) 

        i += 64

    encoded = ''.join([f'{i:08x}' for i in hash])

    return encoded

# encode("í")