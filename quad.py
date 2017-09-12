import math
def quad(a,b,c):
     if a*b*c==0:
          print('invalid value')
          return
     dis=(b*b)-(4*a*c)
     if dis>0:
          print("roots are real and unequal\n")
          root1=(-b+math.sqrt(dis))/(2*a)
          root2=(-b-math.sqrt(dis))/(2*a)
          print('root1: ',root1,' root2: ',root2)
     if dis==0:
          print('roots are real and equal\n')
          root=(-b)/(2*a)
          print('root: ',root)
     if dis<0:
          rootreal=(-b)/(2*a)
          rootimg=(math.sqrt(-dis))
          print('root1: ',rootreal,"+i",rootimg)
          print('root2: ',rootreal,"-i",rootimg)
print('enter coefficients')
a=int(input('enter a: '))
b=int(input('enter b: '))
c=int(input('enter c: '))
quad(a,b,c)          
