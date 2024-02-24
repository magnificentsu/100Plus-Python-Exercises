# Please write a program to compress and decompress the string
# "hello world!hello world!hello world!hello world!".

#My SOLUTION:
import zlib
string = "hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(string.encode())
decompressed_string = zlib.decompress(compressed_string)
print(compressed_string)
print(decompressed_string)

#COURSE SOLUTION:
s = 'hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))