from math import log
from math import log10
from math import pi

def eyring(sideLength,absorption):
    #inputs cube room size and absorption coefficient
    #outputs reverberation time for 60dB decrease
    print ((.161 * sideLength**3)/(-sideLength**2 * 6 * log(1 - absorption)))
print("eyring equation outout for reverberation time")
print(".1 abs coef")
eyring(5,.1)
print("\n.2 abs coef")
eyring(5,.2)
print("\n.3 abs coef")
eyring(5,.3)
print("\n.4 abs coef")
eyring(5,.4)
print("\n.5 abs coef")
eyring(5,.5)
print("\n.6 abs coef")
eyring(5,.6)
print("\n.7 abs coef")
eyring(5,.7)
print("\n.8 abs coef")
eyring(5,.8)
print("\n.9 abs coef")
eyring(5,.9) 

print("\n########################################################################")

def sabine(sideLength,absCoef):
    print (.161 * sideLength ** 3 / ((absCoef*sideLength ** 2)*6))


print("sabine equation's output for reverberation time")
print(".1 abs coef")
sabine(10,.13)
print("\n.2 abs coef")
sabine(5,.2)
print("\n.3 abs coef")
sabine(5,.3)
print("\n.4 abs coef")
sabine(5,.4)
print("\n.5 abs coef")
sabine(5,.5)
print("\n.6 abs coef")
sabine(5,.6)
print("\n.7 abs coef")
sabine(5,.7)
print("\n.8 abs coef")
sabine(5,.8)
print("\n.9 abs coef")
sabine(5,.9) 
print("########################################################################")



def intensity(watts,radius):
    #turns power and distance into decibels
    print (10 * log10((watts /(4 * pi * radius**2))/(10**-12)))
print("These are intensity values with no boundaries")
intensity(.01,2**.5)
intensity(.01,1.5)
intensity(.01,3**.5)
intensity(.01,2.06)
intensity(.01,6**.5)
intensity(.01,2.7)
print("########################################################################")

def revIntensity(watts, absorption, sideLength, radius):
    #gives intensity in a reverberant room in decibels
    Lw =  10 * log10(watts/10 ** -12)
    directField = 1/(4 * pi * radius**2) 
    revField = 4 / ((sideLength ** 2 * 6 * absorption)/ (1 - absorption))
    print( Lw + 10 * log10(directField + revField))
print("These are dB levels with absorption coefficient .5")
revIntensity(.01,.5,5, 2**.5)
revIntensity(.01,.5,5,1.5)
revIntensity(.01,.5,5,3**.5)
revIntensity(.01,.5,5,2.06)
revIntensity(.01,.5,5,6**.5)
revIntensity(.01,.5,5,2.7)
#off from I-SIMPA by ~.2dB
print("########################")
print("These are dB levels with absorption coefficient .1")
revIntensity(.01,.1,5, 2**.5)
revIntensity(.01,.1,5,1.5)
revIntensity(.01,.1,5,3**.5)
revIntensity(.01,.1,5,2.0615528128088303)
revIntensity(.01,.1,5,6**.5)
revIntensity(.01,.1,5,2.7)
print("########################")
revIntensity(.02,.5,5, 2**.5)
print("########################################################################")
def distanceFromSource(n):
    #n is the distance from where the receiver lies to the middle of the array
    n = (n**2 + 1**2)**.5
    n = (n**2 + 1**2)**.5
    print(n)
print("Distances from the sound source")
distanceFromSource(0)     
distanceFromSource(.5)
distanceFromSource(1)
distanceFromSource(1.5)
distanceFromSource(2)
distanceFromSource(2.3)
