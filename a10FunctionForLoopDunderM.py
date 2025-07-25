
class Homes:
    def __init__(self, name, city):
        self.name = name
        self.city = city

N = ["RPS Home", "SatyaSai Home", "Navodaya Home"]
C = ["Delhi", "Whitefield", "BrookBond"]

print("My homes have been:")
for name, city in zip(N, C):
    v1 = Homes(name, city)
    print(v1.name, "-", v1.city)
# built-in Python function zip() to pair up 
# elements from two lists — N (names) and C (cities) — and then loops through those pairs.
# if the 2 lists are of different lengths,The zip() function stops at the shortest list. 
# So even if N has 3 items and C has only 2 (no BrookeBond), zip() will only pair the first two items. 
# The third item in N ("Navodaya Home") is ignored.