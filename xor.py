import binascii

'''
file = open("output.txt","r")

for line in file.readlines():
	line = line.replace("\n","")
	encoded = binascii.unhexlify(str(line))
	for xor_key in range(256):
    		decoded = ''.join(chr(b ^ xor_key) for b in encoded)
    		if (decoded.isprintable() and "CHTB{" in decoded):
        		print(xor_key, decoded)

'''

encoded = binascii.unhexlify("2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904")

for xor_key in range(256):
	key = chr(xor_key)*5
	xored = []
	decoded = ""
	#decoded = ''.join(chr(b) ^ key for b in encoded)
	for i in range(max(len(encoded), len(key))):
		xored_value = ord(encoded.decode("utf-8")[i%len(encoded)]) ^ ord(key[i%len(key)])
		#xored.append(chr(xored_value)[2:])
		decoded = decoded + chr(xored_value)
	if (decoded.isprintable() and "known_plaintext" in decoded):
		print(decoded)
