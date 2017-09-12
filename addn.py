n=int(input('How many numbers you want to add?'))
a={}
def addn(n):
     print('enter numbers: ')
     sum=0
     for i in range(n):
          a[i]=int(input())
     for i in range(n):
          sum=sum+a[i]
     print('sum: ',sum)
addn(n)               
