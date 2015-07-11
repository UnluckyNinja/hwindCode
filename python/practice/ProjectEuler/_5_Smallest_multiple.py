from _3_Largest_prime_factor import gcd

cur = 1
for i in range(2, 21):
    cur = cur * i // gcd(cur, i)

print(cur)