strin="a=b;c=d;e=f;g=h"
strin=strin.split(';')
for i in range(len(strin)):
    strin[i]=strin[i].split('=')
strin=dict(strin)
print(strin)

