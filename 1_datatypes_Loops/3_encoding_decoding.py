msg = "hello 🌍"
encoded_msg = msg.encode("utf-8")

print(msg) # this print will give error of no encoding
print(encoded_msg) # output : b'hello \xf0\x9f\x8c\x8d'

decoded_msg= encoded_msg.decode('utf-8')
print(decoded_msg) # now again error as print

# we encode so computer can understand and decode so we can understand