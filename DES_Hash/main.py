

def hash(text, key):
    blocklen = 64
    result = key
    textInBits = extractBitsFromText(text)
    c = math.ceil(len(textInBits) / blocklen)
    for blockNumber in range(c):
        rc5 = RC5(blocklen, 20, result)
        Mi = extractBytesFromBits(extractSubBits(textInBits, blocklen, blockNumber * blocklen))
        XoredArg = int.from_bytes(Mi, byteorder='little') ^ int.from_bytes(result, byteorder='little')
        ByteXoredArg = XoredArg.to_bytes(XoredArg.bit_length(), byteorder='little')
        data = rc5.encryptBlock(ByteXoredArg)
        prevHash = int.from_bytes(data, byteorder='little') ^ int.from_bytes(Mi, byteorder='little')

        result = prevHash.to_bytes(prevHash.bit_length(), byteorder='little')

    return result