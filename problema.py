with open("Sirul.txt","r") as f:
    sir=f.readline()
q=0 
r=0 
n=0   
m=0   
for i in sir:
    if ord(i) in range(65,91):
        q+=1
with open("Majucsule.txt","w") as f:
    f.write(str(q))
for i in sir:
    if ord(i) in range(97,123):
        r+=1
with open("Minuscule.txt","w") as f:
    f.write(str(r))
for i in sir:
    if ord(i) in range(49,58):
        n+=1
with open("Cifre.txt","w") as f:
    f.write(str(n))
for i in sir:
    if ord(i) in range(33,42):
        m+=1
with open("Simboluri.txt","w") as f:
    f.write(str(m))