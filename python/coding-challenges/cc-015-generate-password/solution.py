# solution-1 using numpy library
# import numpy as np

# def password(name:str):
#     number = np.random.randint(1000,10000)
#     name_index = np.random.randint(len(name),size=3)
#     name_pass = [name.lower()[i] for i in name_index]
#     name_pass.append(str(number))
#     return "".join(name_pass)

# print(password("STEPHENCLARKSON"))

# solution-2 using random module
import random

def random_password(name:str):
    letters = random.sample(name.lower(),3)
    number = random.randint(1000,10000)
    letters.append(str(number))
    return "".join(letters)

print(random_password("STEPHENCLARKSON"))


