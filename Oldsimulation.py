from visual import *
from visual.graph import *
win=550
L=3
scene = display(title="Simulation", width=1.5*win, height=win, x=0, y=0,
                center=(L/2.,L/2.,L/2.))
scene2 = gdisplay(x=0, y=win,xmax=3,
             width=1.5*win, height=0.6*win, xtitle='Time', ytitle=('J    Kinetic=Blue         Potential=Red         Total=Green'))



s=2
KineticGraph = gcurve(color=color.blue)
PotentialGraph = gcurve(color=color.red)
TotalGraph = gcurve(color=color.green)
#arrows
A1=arrow(pos=(-10,4,1),axis=(5,0,0), shaftwidth=0.3,color=(1,1,.5),opacity=.5)
A2=arrow(pos=(10,4,1),axis=(5,0,0), shaftwidth=0.3,color=(1,.2,.5),opacity=.5)
Atot=arrow(pos=(0,4,1),axis=(5,0,0), shaftwidth=0.3,color=color.green)


# these are points that will form the lines on the graph
g=sphere(pos=(0,0,0),color=(0.1,0.1,1),make_trail=True,radius=.0)
g2=sphere(pos=(0,0,0),color=(1,0.1,.1),make_trail=True,radius=.0)
g3=sphere(pos=(0,0,0),color=(0.1,1,.1),make_trail=True,radius=.0)

#the vectors for object d
d= [ (0.7430002202,0.2647603899,-0.0468575389)
     ,(-0.7430002647,-0.2647604843,0.0468569750)
       ,(0.1977276118,-0.4447220146,0.6224700350)
        ,(-0.1977281310, 0.4447221826,-0.6224697723)
         ,(-0.1822009635, 0.5970484122,0.4844363476)
          ,(0.1822015272,-0.5970484858,-0.4844360463)]

# Energys for the graphs/Kinetic/Potential/Total
Tk=float(0)
Tp=float(0)
Te=float(0)


G=25# parts for morse potential
alpha = 3
req = pow(2.,1/6)
dt=.03



b= [( 1.337186  ,  -0.247535  ,  -0.590086)
   ,( 0.452622  ,  -0.395476  ,   1.351409)
   ,(-0.567401  ,   0.416724  ,  -1.300758)
   ,(-0.576618  ,  -0.627045  ,   1.029231)
   ,(-1.195775  ,  -0.134036  ,  -0.580644)
   ,(-0.911954  ,   0.902604  ,  -0.372340)
   ,(-0.292797  ,   0.409596  ,   1.237535)
   ,( 0.275199  ,  -1.125840  ,   0.552620)
   ,( 0.736425  ,   0.558761  ,   0.891125)
   ,(-0.346279  ,  -0.630983  ,  -1.063292)
   ,( 0.114946  ,   1.053617  ,  -0.724787)
   ,( 1.075732  ,  -0.384762  ,   0.449081)
   ,( 0.468255  ,   0.098945  ,  -1.130425)
   ,(-0.910084  ,   0.168471  ,   0.401610)
   ,(-0.573574  ,  -0.784406  ,  -0.019620)
   ,(-0.109433  ,   0.910842  ,   0.321024)
   ,( 0.424179  ,  -0.662217  ,  -0.365937)
   ,( 0.728380  ,   0.448860  ,  -0.142676)
   ,(-0.223940  ,   0.138893  ,  -0.386086)
   ,( 0.094932  ,  -0.115012  ,   0.443016) ]
n=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,
   1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1
   ,1,1,1,1,1,1,1,1]#the array all partical fall in
x=0
while (x<6):#buiiding object d
    n[x]=sphere(pos=d[x],color=(1,1,.5),make_trail=False,
            radius=.7,mass=9e3,p=vector(2000,0,0),Potential=0)

    
    n[x].v = n[x].p/n[x].mass
    n[x].pos+=(-10,0,1)#starting point of objects
    n[x].make_trail=True
    
    x+=1
c=0
while (x<26):#buiiding object b
    n[x]=sphere(pos=b[c],color=(1,.2,.5),make_trail=False,
            radius=.7,mass=9e3,p=vector(-500,0,0),Potential=0)
    n[x].pos+=(10,0,0)#starting point of objects
    n[x].v = n[x].p/n[x].mass
    n[x].make_trail=True
    c+=1
    x+=1
l=0#just values
a=1
i=0
eq=.5
t = 0.
o=0
#arrow defintions, momentum, center of mass
P1=vector(0,0,0)
P2=vector(0,0,0)
Pt=vector(0,0,0)
C1=vector(0,0,0)
C2=vector(0,0,0)
Ct=vector(0,0,0)
while(t < 250):
    rate(260)
    for m in range(0,26):
        n[m].v = 0.5*(n[m].v + n[m].p/n[m].mass)
        n[m].pos+=n[m].v*dt


    o+=.01*dt
    Tk=0#reseting energy so I can get ten new total at given point
    Tp=0
    Te=0

    #arrows
    P1=vector(0,0,0)
    P2=vector(0,0,0)
    Pt=vector(0,0,0)
    C1=vector(0,0,0)
    C2=vector(0,0,0)
    Ct=vector(0,0,0)
    for f in range(0,26):
       
        vmag=abs(mag(n[f].v))
        Tk+=n[f].mass*pow(vmag,2)
        
        Tp+=n[f].Potential
    Te=Tp+Tk


    #arrows
    for f in range(0,6):
        P1+=n[f].p
        C1+=n[f].pos

    for f in range(6,26):
        P2+=n[f].p
        C2+=n[f].pos
    Ct=(C1+C2)/26
    C1=C1/6
    C2=C2/20
        

    Pt=P1+P2
    A1.axis=P1*.0009
    A1.pos=C1
    A2.pos=C2
    A2.axis=P2*.0009
    Atot.axis=Pt*.0009
    #Atot.pos=Ct


   # for f in range(0,26):#adding potential
   #     pmag=mag(n[f].p)
    #    Te+=n[f].Potential


    KineticGraph.plot(pos=(o,Tk,0))#graphing
    PotentialGraph.plot(pos=(o,Tp,0))#graphing
    TotalGraph.plot(pos=(o,Te,0))#graphing


    for l in range(0,26):#resetting potential energey so it can be recalculated
        n[l].Potential=0

    for l in range(0,26):#Calculations of force between all objects
        for a in range(l+1,26):
            
            r=n[l].pos-n[a].pos #equations
            rmag=mag(r)
            #print(rmag)
            UnitV=r/rmag
            #if (rmag>1):
            #Morse potential
            PE=G*pow((1-exp(-alpha*(rmag-req))),2)
            n[l].Potential+=PE
            n[a].Potential+=PE
            #Morse potential derivitive
            arg = exp(-2*alpha*(rmag-req))-exp(-alpha*(rmag-req))
            Fgrav=(2*alpha*G*arg)*UnitV
            n[l].p+=Fgrav*dt
            n[a].p+=-Fgrav*dt
    t += dt

            

