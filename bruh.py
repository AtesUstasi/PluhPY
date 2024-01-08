characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Passwordlength = int(input("How long Shall ur password be?"))
import random
Password = ""
for i in range(Passwordlength):
    Password += random.choice(characters)
print(Password)
