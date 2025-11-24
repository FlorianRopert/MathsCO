from pylab import *
#Triangle matplotlib
"""xlim(0,10)
ylim(0,10)
x=[2,5,8,2]
y=[2,8,2,2] 
plot(x,y,linewidth=3,*"r")
show()"""
#Carre matplotlib
"""xlim(0,10)
ylim(0,10)
x=[3,3,7,7,3]
y=[3,7,7,3,3]
plot(x,y,linewidth=3,*"r")
show()"""
#Exercice 3
"""xlim(0,20)
ylim(2,4)
y=3
for i in range(10):
    x=5+i
    plot(x,y,"ob")
show()"""
#Exercice 4
"""xlim(0,20)
ylim(2,6)
y=3
for i in range(10):
    x=5+i
    plot(x,y,"ob")
y=5
for i in range(10):
    x=5+i
    plot(x,y,"ob")
show()"""
#Exercice 5
"""xlim(0,20)
ylim(0,30)
y=10
for i in range(9):
    y+=1
    for i in range(10):
        x=5+i
        plot(x,y,"ob")
show()"""
#Exercice 6
"""from pylab import *
xlim(0,20)
ylim(2,50,10)
for i in range(31):
    x=10+i
    y=x
    plot(x,y,'ob')
show()"""
#Exercice 7
"""from pylab import *
xlim(0,25,5)
ylim(0,45,5)
for i in range(21):
    x=i
    y_1=2*x
    y_2=x
    y_3=0.5*x
    plot(x,y_1,'dr')
    plot(x,y_2,'ob')
    plot(x,y_3,'*r')
show()"""
#Exercice 8 - 1
"""from pylab import *
xlim(-3,5,1)
ylim(-30,30,5)
liste_x=[]
liste_y=[]
for i in range(100):
    x=-3+0.06*i
    y=x**3
    liste_x.append(x)
    liste_y.append(y)
plot(liste_x,liste_y,'k')
show()"""
#Exercice 8 - 2
"""from pylab import *
xlim(-5,5,1)
ylim(-50,50,1)
liste_x=[]
liste_y=[]
for i in range(250):
    x=-5+0.02*i
    y=1/x
    liste_x.append(x)
    liste_y.append(y)
for i in range(250):
    x=0.02+0.02*i
    y=1/x
    liste_x.append(x)
    liste_y.append(y)
plot(liste_x,liste_y,'k')
show()"""