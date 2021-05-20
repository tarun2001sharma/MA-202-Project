import math
import random
from matplotlib import pyplot
pi = math.pi
e = math.e
tan = math.tan
Hr = 8000
Hm = 1200
print("Input Wavelength in nm( range  300 to 700): ",end="")
lamda=int(input())
wavelength=[302,312,318,325,333,342,353,364,380,394,410,432,468,509,530,535]
Intensity_Io=[780,1316,1200,1238,1430,1334,1249,1285,1513,979,1969,1902,2069,1988,2005,1999]
answer=0
k=0
L=[]
for i in range(0,len(wavelength)):
    ans=1
    for j in range(0,len(wavelength)):
        if(j!=i):
            ans=ans*(lamda-wavelength[j])
            ans=ans/(wavelength[i]-wavelength[j])
    L.append(ans)
answer=0
for i in range(len(L)):
    answer=answer+(L[i]*Intensity_Io[i])
print("Value of Intensity of radiation at",lamda,"nm is:",answer)
Io=answer
lamda = lamda*(10**-9) #wavelength
N =  2.7*(10**25) #molecular density at sea level
u = random.uniform(0.7,0.85)#random number in range 0.7 to 0.85
x = (5*u/9) + (125*((u)**3)/729) + ((64/27) - ((325*(u**2))/243) + ((1250*(u**4))/2187))**(0.5)
g = (5*u/9) + ((4/3)-(25*(u**2)/81))*(x**(-1/3)) + x**(1/3) 
'''print(u)
print(x)
print(g)'''


n=1.0003



Height=[]
print("Input point height (range 15-15000): ",end="")   #input y
P=int(input())
print("Input Angle at which Pa-Pb segment is from horizontal  (type n if angle required is pi/n where n is an integer): ",end="")
alpha = int(input())
alpha = pi/alpha
print("Input Angle at which Pc-P segment is from horizontal  (type n if angle required is pi/n where n is an integer): ",end="")
theta = int(input())
theta = pi/theta
xo=-10*Hm
distance=[]
'''Xaxis=[]
Yaxis=[]'''
while(abs(xo)<=10*Hm):
    yo=P-(tan(alpha))*(-xo)
    distance.append((yo**2+xo**2)**0.5)
    '''Xaxis.append(xo)
    Yaxis.append(yo)'''
    xo+=100
'''pyplot.plot(Xaxis,distance)
pyplot.plot(Xaxis,Yaxis)
pyplot.show()'''
#print(distance)
#print(len(distance))            
            

    
step=100

def cos(theta):
    return math.cos(theta)
def Fr(theta):
    answer = 3*(1+((cos(theta))**2))/(16*pi)
    return answer
def Fm(theta):
    g = random.uniform(-1,1)
    answer = (3*(1-(g**2))*(1+(cos(theta))**2))/((2+(g**2))*(1+(g**2)-(2*g*cos(theta)))**(1.5))
    return answer
def Br(lamda):
    answer = (8*(pi)*((n**2)-1)**2)/(3*N*(lamda**4))
    return answer
def Bm(lamda):
    answer = (8*(pi**3)*(((n**2)-1)**2))/(3*N)
    return answer
def ROr(h):
    answer = e**(-(h/Hr))
    return answer
def ROm(h):
    answer = e**(-(h/Hm))
    return answer

print()
print("Fr is",Fr(theta))
print("Br is",Br(lamda))
print("Fm is",Fm(theta))
print("Bm is",Bm(lamda))
print("angle is",theta+alpha,"in radians")



opticaldensityarray=[]
for i in range(len(distance)):#Calculating Optical depth for a particular point (in Path Pa to Pb) from Pa
    j=0
    answer=0
    while(j<i):
        if(i==1):
            answer+=(ROr(distance[j])+ROr(distance[j+1]))*(step/2)
            j+=2
        else:
            if(i%2==0):
                term1=ROr(distance[j])
                term2=ROr(distance[j+1])
                term3=ROr(distance[j+2])
                answer+=(term1+4*term2+term3)*(step/3)
                j+=2
            else:
                if(i-j==1):
                    answer+=(ROr(distance[j])+ROr(distance[j+1]))*(step/2)
                    j+=2
                elif(i-j==2):
                    term1=ROr(distance[j])
                    term2=ROr(distance[j+1])
                    term3=ROr(distance[j+2])
                    answer+=(term1+4*term2+term3)*(step/3)
                    j+=2
                else:
                    term1=ROr(distance[j])
                    term2=ROr(distance[j+1])
                    term3=ROr(distance[j+2])
                    term4=ROr(distance[j+3])
                    answer+=(term1+3*term2+3*term3+term4)*(3*step/8)
                    j+=3
    opticaldensityarray.append(answer*Br(lamda))
#print(opticaldensityarray)
#print(len(opticaldensityarray))

distancefromPc=[]
xo=-10*Hm
while(abs(xo)<=10*Hm):
    yo=P+(tan(theta))*(0-xo)
    distancefromPc.append((yo**2+xo**2)**0.5)
    xo+=100
'''print(distancefromPc)
print(len(distancefromPc))'''
opticaldensityarrayPc=[]
for i in range(len(distance)):#Calculating Optical depth for a particular point (in Path Pa to Pb) from Pc
    j=0
    answer=0
    distancefromPc=[]
    xo=-10*Hm
    while(abs(xo)<=10*Hm):
        yo=P+(tan(theta))*(-xo)
        distancefromPc.append((yo**2+xo**2)**0.5)
        xo+=100
    while(j<i):
        if(i==1):
            answer+=(ROr(distancefromPc[j])+ROr(distancefromPc[j+1]))*(step/2)
            j+=2
        else:
            if(i%2==0):
                term1=ROr(distancefromPc[j])
                term2=ROr(distancefromPc[j+1])
                term3=ROr(distancefromPc[j+2])
                answer+=(term1+4*term2+term3)*(step/3)
                j+=2
            else:
                if(i-j==1):
                    answer+=(ROr(distancefromPc[j])+ROr(distancefromPc[j+1]))*(step/2)
                    j+=2
                elif(i-j==2):
                    term1=ROr(distancefromPc[j])
                    term2=ROr(distancefromPc[j+1])
                    term3=ROr(distancefromPc[j+2])
                    answer+=(term1+4*term2+term3)*(step/3)
                    j+=2
                else:
                    term1=ROr(distancefromPc[j])
                    term2=ROr(distancefromPc[j+1])
                    term3=ROr(distancefromPc[j+2])
                    term4=ROr(distancefromPc[j+3])
                    answer+=(term1+3*term2+3*term3+term4)*(3*step/8)
                    j+=3
    opticaldensityarrayPc.append(answer*Br(lamda))
#print(opticaldensityarrayPc)
#print(len(opticaldensityarrayPc))

ans=0
def I(lamda):
    return Io
j=0
k=len(distance)-1
while(j<k):
    if(k%2==0):
        term1=ROr(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))
        term2=ROr(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1]))
        term3=ROr(distance[j+2])*(e**(-opticaldensityarrayPc[j+2]-opticaldensityarray[j+2]))
        ans+=(term1+4*term2+term3)*(step/3)
        j+=2
    else:
        if(k-j==1):
            answer+=(ROr(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))+ROr(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1])))*(step/2)
            j+=2
        elif(k-j==2):
            term1=ROr(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))
            term2=ROr(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1]))
            term3=ROr(distance[j+2])*(e**(-opticaldensityarrayPc[j+2]-opticaldensityarray[j+2]))
            answer+=(term1+4*term2+term3)*(step/3)
            j+=2
        else:
            term1=ROr(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))
            term2=ROr(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1]))
            term3=ROr(distance[j+2])*(e**(-opticaldensityarrayPc[j+2]-opticaldensityarray[j+2]))
            term4=ROr(distance[j+3])*(e**(-opticaldensityarrayPc[j+3]-opticaldensityarray[j+3]))
            answer+=(term1+3*term2+3*term3+term4)*(3*step/8)
            j+=3

ans=ans*(I(lamda)*Br(lamda)*Fr(alpha+theta))
Is=ans
print()
print("Using Simpson model")
print("Rayleigh Scattering:",ans)



#Mie scattering

opticaldensityarray=[]
for i in range(len(distance)):#Calculating Optical depth for a particular point (in Path Pa to Pb) from Pa
    j=0
    answer=0
    while(j<i):
        if(i==1):
            answer+=(ROr(distance[j])+ROr(distance[j+1]))*(step/2)
            j+=2
        else:
            if(i%2==0):
                term1=ROr(distance[j])
                term2=ROr(distance[j+1])
                term3=ROr(distance[j+2])
                answer+=(term1+4*term2+term3)*(step/3)
                j+=2
            else:
                if(i-j==1):
                    answer+=(ROr(distance[j])+ROr(distance[j+1]))*(step/2)
                    j+=2
                elif(i-j==2):
                    term1=ROr(distance[j])
                    term2=ROr(distance[j+1])
                    term3=ROr(distance[j+2])
                    answer+=(term1+4*term2+term3)*(step/3)
                    j+=2
                else:
                    term1=ROr(distance[j])
                    term2=ROr(distance[j+1])
                    term3=ROr(distance[j+2])
                    term4=ROr(distance[j+3])
                    answer+=(term1+3*term2+3*term3+term4)*(3*step/8)
                    j+=3
    opticaldensityarray.append(answer*Bm(lamda))


opticaldensityarrayPc=[]
for i in range(len(distance)):#Calculating Optical depth for a particular point (in Path Pa to Pb) from Pc
    j=0
    answer=0
    distancefromPc=[]
    xo=-10*Hm
    while(abs(xo)<=10*Hm):
        yo=P+(tan(theta))*(-xo)
        distancefromPc.append((yo**2+xo**2)**0.5)
        xo+=100
    while(j<i):
        if(i==1):
            answer+=(ROr(distancefromPc[j])+ROr(distancefromPc[j+1]))*(step/2)
            j+=2
        else:
            if(i%2==0):
                term1=ROr(distancefromPc[j])
                term2=ROr(distancefromPc[j+1])
                term3=ROr(distancefromPc[j+2])
                answer+=(term1+4*term2+term3)*(step/3)
                j+=2
            else:
                if(i-j==1):
                    answer+=(ROr(distancefromPc[j])+ROr(distancefromPc[j+1]))*(step/2)
                    j+=2
                elif(i-j==2):
                    term1=ROr(distancefromPc[j])
                    term2=ROr(distancefromPc[j+1])
                    term3=ROr(distancefromPc[j+2])
                    answer+=(term1+4*term2+term3)*(step/3)
                    j+=2
                else:
                    term1=ROr(distancefromPc[j])
                    term2=ROr(distancefromPc[j+1])
                    term3=ROr(distancefromPc[j+2])
                    term4=ROr(distancefromPc[j+3])
                    answer+=(term1+3*term2+3*term3+term4)*(3*step/8)
                    j+=3
    opticaldensityarrayPc.append(answer*Bm(lamda))


j=0
k=len(distance)-1
ans=0
while(j<k):
    if(k%2==0):
        term1=ROm(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))
        term2=ROm(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1]))
        term3=ROm(distance[j+2])*(e**(-opticaldensityarrayPc[j+2]-opticaldensityarray[j+2]))
        ans+=(term1+4*term2+term3)*(step/3)
        j+=2
    else:
        if(k-j==1):
            answer+=(ROm(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))+ROm(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1])))*(step/2)
            j+=2
        elif(k-j==2):
            term1=ROm(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))
            term2=ROm(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1]))
            term3=ROm(distance[j+2])*(e**(-opticaldensityarrayPc[j+2]-opticaldensityarray[j+2]))
            answer+=(term1+4*term2+term3)*(step/3)
            j+=2
        else:
            term1=ROm(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))
            term2=ROm(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1]))
            term3=ROm(distance[j+2])*(e**(-opticaldensityarrayPc[j+2]-opticaldensityarray[j+2]))
            term4=ROm(distance[j+3])*(e**(-opticaldensityarrayPc[j+3]-opticaldensityarray[j+3]))
            answer+=(term1+3*term2+3*term3+term4)*(3*step/8)
            j+=3

ans=ans*(I(lamda)*Bm(lamda)*Fm(alpha+theta))    
print("Mie Scattering:",ans)
Im=ans
print("Final Answer:",Is+Im)
print("Percent of total intensity",(Is+Im)*100/I(lamda),"%")
print()
print("Using Trapezoidal method")

k=len(distance)-1
j=0
ans=0
while(j<k):
    answer+=(ROr(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))+ROr(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1])))*(step/2)
    j+=2
ans=answer*(I(lamda)*Br(lamda)*Fr(alpha+theta))
Is=ans
print("Rayleigh Scattering:",ans)
while(j<k):
    answer+=(ROm(distance[j])*(e**(-opticaldensityarrayPc[j]-opticaldensityarray[j]))+ROm(distance[j+1])*(e**(-opticaldensityarrayPc[j+1]-opticaldensityarray[j+1])))*(step/2)
    j+=2
ans=answer*(I(lamda)*Bm(lamda)*Fm(alpha+theta))
Im=ans
print("Mie Scattering:",ans)
print("Final answer:",Is+Im)
print("Percent of total intensity",(Is+Im)*100/I(lamda),"%")


