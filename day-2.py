distance = 0
depth = 0
totalinput = 0
input = "forward 5 down 5 forward 8 up 3 down 8 forward 2"
tokens = input.split(" ")
print(tokens)

for index, reading in enumerate(tokens):
    totalmoved = totalmoved + 1
    tokensforward = tokens[index + 1]
    if reading == 'forward':




print(totalmoved)