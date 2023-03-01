print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:
def get_divisors(number):
    l = []
    for i in range(1,number+1):
        if number % i == 0:
            l.append(i)
    return l


print(get_divisors(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


# A1b:
def are_factors(n1,n2):
    return  n1 in get_divisors(n2)


print(are_factors(5,9))
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:
def alpha_pos(letter):
    return str(alphabet.index(letter))


print(alpha_pos('r'))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# A2b:
def name_to_id(name):
    return ''.join(map(alpha_pos,name))


print(name_to_id("alexander"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


# A2c:
def id_to_password(password):
    return int(password) - sum(map(int,password))


id_to_password("137123123123")
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
import math


def is_prime_bruteforce(n):
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            return False
    return True


is_prime_bruteforce(55)


def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True


print(is_prime(1231231923012931203))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:
def is_prime(n):
  try:
      n = int(n)
  except:
      print('Input was not a number, try again')
      return False

  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True


print(is_prime([1,2,3]))

print(is_prime('1'))

# -------------------------------------------------------------------------------------- #






