from sage.all import *


def Gen():
    # Set the desired length for p
    p_length = 2048 # Example length, adjust as needed

    # Generate a prime number p of the specified length
    p = next_prime(2**p_length)

    # Define the multiplicative groups GG1 and GG2
    GG1 = Integers(p)  # Group GG1 of order p
    # GG2 = MultiplicativeAbelianGroup(p)  # Group GG2 of order p

    # Generate a random element form the group 
    g = GG1.random_element() # come back here later to make this a generator

    # Define the bilinear map e~
    def bilinear_map(x, y):
        return power_mod(g, x, p) * power_mod(g, y, p)

    # Generate the system parameters (g, e, ~GG1, ~GG2, p)
    e = bilinear_map
    # ~GG1 = GG1
    # ~GG2 = GG2

    # Return the system parameters
    return g, e, GG1, p


x,y,z,w=Gen()



# import random

# def Gen(lambda_val):
#     # Generate a prime number p of length lambda
#     p = generate_prime(lambda_val)

#     # Generate a generator g for G1
#     g = generate_generator(p)

#     # Generate random elements in G1 and G2
#     a = random.randint(1, p - 1)
#     b = random.randint(1, p - 1)
#     c = random.randint(1, p - 1)

#     # Compute the elements in G1 and G2
#     G1 = pow(g, a, p)
#     G2 = pow(g, b, p)
#     e = pow(G1, c, p)

#     return g, e, G1, G2, p


# def generate_prime(lambda_val):
#     while True:
#         # Generate a random number of length lambda
#         candidate = random.getrandbits(lambda_val)

#         # Set the two highest bits to 1 to ensure the length is lambda
#         candidate |= (1 << lambda_val - 1) | 1

#         # Check if the number is prime
#         if is_prime(candidate):
#             return candidate


# def is_prime(n, k=10):
#     if n == 2 or n == 3:
#         return True
#     if n <= 1 or n % 2 == 0:
#         return False

#     r, s = 0, n - 1
#     while s % 2 == 0:
#         r += 1
#         s //= 2

#     for _ in range(k):
#         a = random.randint(2, n - 1)
#         x = pow(a, s, n)

#         if x == 1 or x == n - 1:
#             continue

#         for _ in range(r - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 break
#         else:
#             return False

#     return True


# def generate_generator(p):
#     # Check every number from 2 to p - 1
#     for g in range(2, p):
#         # Check if g is a generator of the group G1
#         if is_generator(g, p):
#             return g

#     # If no generator is found, raise an error
#     raise ValueError("No generator found for the group G1")


# def is_generator(g, p):
#     # Check if g is a generator of the group G1
#     for i in range(1, p - 1):
#         if pow(g, i, p) == 1:
#             return False
#     return True


# # Example usage
# lambda_val = 256  # Length of prime p
# g, e, G1, G2, p = Gen(lambda_val)

# print("g:", g)
# print("e:", e)
# print("G1:", G1)
# print("G2:", G2)
# print("p:", p)