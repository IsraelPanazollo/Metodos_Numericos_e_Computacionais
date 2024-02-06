import math
w=-0.2
k=1
x=0.
erro=1.

while(erro>0.0000001):
    x = x + (((-1)**(k-1))*(w**k))/k
    k = k + 1
    print k,  "esima tentativa = " , x
    erro =  math.fabs((x-math.log(0.8))/math.log(0.8))
      
  



    
   

