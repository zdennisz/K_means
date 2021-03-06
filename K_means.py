from random import randint
from math import sqrt
import simpleplot
import time


class Point:
    def __init__(self):
        self.x = randint(1, 100)
        self.y = randint(1, 100)

    def __str__(self):
        f = "X: %s Y: %s" % (self.x, self.y)
        return f


start = time.time()
NumOfPoints = 50
total_elapsed = 0
flag = 0
i1 = 0
i2 = 0
i3 = 0
i4=0
m1 = Point()  # create 3 new random centers, in order to begin the loop and make one rotation to start the algorithem
m2 = Point()
m3 = Point()
om1 = Point()
om2 = Point()
om3= Point()
counter = 0
dataset1 = []
dataset2 = []
dataset5=[]
l2 = []
l3 = []
l4 = []
l5 = []
l6=[]
l7=[]
dataset3 = []
dataset4 = []
dataset6=[]
k0 = []
k1 = []
k2 = []
k3 = []
k0 = [Point() for i in range(NumOfPoints)]  # use of list comprehension

m1.x = k0[randint(0, NumOfPoints - 1)].x  # select the initial mean of the aviliable points
m1.y = k0[randint(0, NumOfPoints - 1)].y
m2.x = k0[randint(0, NumOfPoints - 1)].x
m2.y = k0[randint(0, NumOfPoints - 1)].y
m3.x = k0[randint(0, NumOfPoints - 1)].x
m3.y = k0[randint(0, NumOfPoints - 1)].y

while (counter<12):

    counter = counter + 1
    i2 = -1  # since we empty the lists we should reset the counters
    i3 = -1
    i4 = -1
    del k1[:]  # empty out the lists for new entry
    del k2[:]
    del k3[:]
    om1.x = m1.x
    om1.y = m1.y

    om2.x = m2.x
    om2.y = m2.y
    
    om3.x = m3.x
    om3.y = m3.y

    
    for i1 in range(0, NumOfPoints):
        # euclidian distance calculation of x && y from
        t1x = k0[i1].x - m1.x
        t1x = t1x ** 2

        t1y = k0[i1].y - m1.y
        t1y = t1y ** 2

        t1Dist = t1y + t1x
        t1Dist = sqrt(t1Dist)

        t2x = k0[i1].x - m2.x
        t2x = t2x ** 2

        t2y = k0[i1].y - m2.y
        t2y = t2y ** 2

        t2Dist = t2y + t2x
        t2Dist = sqrt(t2Dist)
        
        t3x = k0[i1].x - m3.x
        t3x = t3x ** 2

        t3y = k0[i1].y - m3.y
        t3y = t3y ** 2

        t3Dist = t3y + t3x
        t3Dist = sqrt(t3Dist)       

        # check if the distance is smaller add to one list otherwise add to second list
        if (int(t1Dist) < int(t2Dist)):
            if(int(t3Dist)<int(t1Dist)):
                k3.append(k0[i1])
                i4=i4+1
            else:
                k1.append(k0[i1])
                i2 = i2 + 1
        else:
            if(int(t3Dist)<int(t2Dist)):
                k3.append(k0[i1])
                i4=i4+1
            else:
                k2.append(k0[i1])
                i3 = i3+1

    t2 = Point()
    t2.x = 0
    t2.y = 0
    # calculate the first new center for the points
    for element in k1:
        t2.x = element.x + t2.x
    # prevent division by zero if the list is empty
    if (i2 == 0):
        m1.x = int(t2.x)
    else:
        m1.x = int(t2.x / i2)

    for element in k1:
        t2.y = element.y + t2.y
    # prevent division by zero if the list is empty
    if (i2 == 0):
        m1.y = int(t2.y)
    else:
        m1.y = int(t2.y / i2)

    # calculate the second new center for the points
    t2.x = 0
    t2.y = 0

    for element in k2:
        t2.x = element.x + t2.x
    # prevent division by zero if the list is empty
    if (i3 == 0):
        m2.x = int(t2.x)
    else:
        m2.x = int(t2.x / i3)

    for element in k2:
        t2.y = element.y + t2.y
    # prevent division by zero if the list is empty
    if (i3 == 0):
        m2.y = int(t2.y)
    else:
        m2.y = int(t2.y / i3)
    
    # calculate the third new center for the points
    t2.x = 0
    t2.y = 0

    for element in k3:
        t2.x = element.x + t2.x
    # prevent division by zero if the list is empty
    if (i4 == 0):
        m3.x = int(t2.x)
    else:
         m3.x = int(t2.x / i4)

    for element in k3:
        t2.y = element.y + t2.y
    # prevent division by zero if the list is empty
    if (i4 == 0):
        m3.y = int(t2.y) 
    else:
        m3.y = int(t2.y / i4)                  
                  
    print('----------------------')
    print("Cluster 1")
    print("Current Center ")
    print('--------')
    print(m1)
    print('--------')
    if(i2>=0):
          for i9 in range(i2):
                 print(k1[i9])

    print(' ')
    print("Cluster 2")
    print("Current Center ")
    print('--------')
    print(m2)
    print('--------')
    if(i3>=0):
           for i9 in range(i3):
                  print(k2[i9])
        
            

    print('----------------------')
    print(' ')
    print("Cluster 3")
    print("Current Center ")
    print('--------')
    print(m3)
    print('--------')
    if(i4>=0):
         for i9 in range(i4):
                print(k3[i9])
                  
                  
    if (m1.x == om1.x):
        flag = 1
    if ((m2.y == om2.y) & flag == 1):
        flag=2
    if ((m3.y == om3.y) & flag == 2):     
        break
                  
total_elapsed += time.time() - start
print('The algorithem took %8.3f seconds' % (total_elapsed))
print("Number of iteration is :", counter)
# print the end result of the algorithem
for element in k1:
    dataset1.append(element.x)

for element in k1:
    dataset2.append(element.y)
z = zip(dataset1, dataset2)

for element in k2:
    dataset3.append(element.x)

for element in k2:
    dataset4.append(element.y)
y = zip(dataset3, dataset4)
                  
for element in k3:
    dataset5.append(element.x)

for element in k3:
    dataset6.append(element.y)
u = zip(dataset5, dataset6)                  
                  
l2.append(m1.x)
l3.append(m1.y)
dataset1_center = zip(l2, l3)

l4.append(m2.x)
l5.append(m2.y)
dataset2_center = zip(l4, l5)
                  
l6.append(m3.x)
l7.append(m3.y)
dataset3_center = zip(l6, l7)                  
simpleplot.plot_scatter('K Means', 1280, 780, 'x', 'y', [z, y,u, dataset1_center, dataset2_center,dataset3_center],
                        ['dataset1', 'dataset2','dataset3','center 1', 'center 2','center3'])
