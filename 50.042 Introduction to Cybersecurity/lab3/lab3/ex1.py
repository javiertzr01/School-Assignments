import hashlib

plaintext = "Pancakes"

result = hashlib.md5(plaintext.encode())

print(result.hexdigest())

text = "foobardfadsfasdfasdfasdfsadfasdfasfdasfdadsfadsfasdfadsfads"

result1 = hashlib.md5(text.encode())

print(result1.hexdigest())