from time import sleep
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "/_<>[]!@#$%&()-:;.,?{}"
numbs = "0123456789"

def LenghtPassOSEM():
  lenght = 8
def LenghtPassDESAC():
  lenght = 10
def LenghtPassDVANASC():
  lenght = 12
def LenghtPassSESNAST():
  lenght = 16

lenght = 9
Pridavac = lower_case + UPPER_CASE + symbols + numbs
PSSWD = "".join(random.sample(Pridavac, lenght))
print("Vase nove heslo je:", PSSWD)
