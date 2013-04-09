

import hashlib

i = 0

plop = "plop"
while (i < 20):
    plop = hashlib.sha256(plop).hexdigest()
    i+=1
print plop 

