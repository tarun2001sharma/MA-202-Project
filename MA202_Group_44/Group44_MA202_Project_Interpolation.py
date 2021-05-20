from matplotlib import pyplot
wavelength=[302,312,318,325,333,342,353,364,380,394,410,432,468,509,530,535]
Intensity_Io=[780,1316,1200,1238,1430,1334,1249,1285,1513,979,1969,1902,2069,1988,2005,1999]

pyplot.xlabel("Wavelength (in nanometer)")
pyplot.ylabel("Intensity (in microwatts per square centimeter per 10 millimicrons)")
pyplot.title("Plot using Linear Interpolation")
pyplot.grid()
pyplot.plot(wavelength,Intensity_Io)
pyplot.show()
print("Interpolation using nth order lagrange polynomial")

#Lagrange Polynomial of order 16
print("Input Wavelength:",end="")
inwavelength=int(input())
answer=0
k=0
L=[]
for i in range(0,len(wavelength)):
    ans=1
    for j in range(0,len(wavelength)):
        if(j!=i):
            ans=ans*(inwavelength-wavelength[j])
            ans=ans/(wavelength[i]-wavelength[j])
    L.append(ans)
answer=0
for i in range(len(L)):
    answer=answer+(L[i]*Intensity_Io[i])
print("Value of Intensity of radiation at",inwavelength,"is:",answer)
#print(L)   L0,L1,L2 terms....


initial=0
x=[]
y=[]
while(initial<600):
    L=[]
    for i in range(0,len(wavelength)):
        ans=1
        for j in range(0,len(wavelength)):
            if(j!=i):
                ans=ans*(initial-wavelength[j])
                ans=ans/(wavelength[i]-wavelength[j])
        L.append(ans)
    answer=0
    for i in range(len(L)):
        answer=answer+(L[i]*Intensity_Io[i])
    y.append(answer)
    x.append(initial)
    initial+=0.01
#Plot of wavelength from range 0 to 600 nano meter 
pyplot.plot(x,y,label="Plot",color="Blue")
pyplot.xlabel("Wavelength (in micrometer)")
pyplot.ylabel("Intensity (in microwatts per square centimeter per 10 millimicrons)")
pyplot.title("Wavlength Vs Initensity (range 0-600 micro meter)")
pyplot.legend()
pyplot.grid()
pyplot.show()
    
#Zoomed plot of wavelngth in range 300 to 400
pyplot.plot(x[30200:100*(inwavelength+50)],y[30200:100*(inwavelength+50)],label="Plot",color="Blue")
pyplot.xlabel("Wavelength (in micrometer)")
pyplot.ylabel("Intensity (in microwatts per square centimeter per 10 millimicrons)")
pyplot.title("Wavlength Vs Initensity (zoomed plot)")
pyplot.legend()
pyplot.grid()
pyplot.show()
# variation are observed if we zoom our Plot as we have considered the data sets to follow lagrange nth order polynomial
