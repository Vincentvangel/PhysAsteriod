from visual import *
from visual.graph import *
win=550
L=3
#Current issue - force is not set to the right distance or strength

scene = display(title="Simulation", width=1.5*win, height=win, x=0, y=0,
                center=(L/2.,L/2.,L/2.))


#functions, marked by def then name and imputs
#funtions can be called and send back information
G=6.7e-11
alpha = 2
req = 1.1


def Islinked (n,amount):#defineing "linked" particals, much like a chemical bond.
    for l in range(0,active):
        for a in range(l+1,amount):
            j=mag(n[l].pos-n[a].pos)
            if(j<1.2):
                n[l].link[a]=true
                n[a].link[l]=true
            else:
                n[l].link[a]=false
                n[a].link[l]=false
                
            
def Forcelinked (l,a,j,dis):#the force that will be applied between two linked particals
    d=n[l].pos-n[a].pos
    x=mag(d)
    unitv=j/dis
    #f=(-x+1/x)*12

    arg = exp(-2*alpha*(dis-req))-exp(-alpha*(dis-req))#OLD MORSE
    Fgrav=(2*alpha*G*(n[l].mass*n[a].mass)/pow(1.1,2)*arg)*unitv



    n[l].p+=Fgrav
    n[a].p+=-Fgrav
    if(dis>1.2):#bond length
        n[l].link[a]=false
        n[a].link[l]=false
    print(d)          

def Forceunlinked (p1,p2,j,dis):#force applied to unlinked particals

    x=dis+1
    unitv=j/dis
    f=1/(x**2)
    p1.p+=f*unitv
    p2.p+=-f*unitv



active=7#total particals in the scene, this is important to have at the right number
n =[None]*active#the array for all particals
#the vectors for object 1
d= [ (0.7430002202,0.2647603899,-0.0468575389)#the vectors for object 1
     ,(-0.7430002647,-0.2647604843,0.0468569750)#needs to be moved out to a .py file
     ,(0.1977276118,-0.4447220146,0.6224700350)
     ,(-0.1977281310, 0.4447221826,-0.6224697723)
     ,(-0.1822009635, 0.5970484122,0.4844363476)
     ,(0.1822015272,-0.5970484858,-0.4844360463)]


for x in range(0,6):#buiiding object d
    n[x]=sphere(pos=d[x],color=(1,1,.5),make_trail=False,
            radius=.7,mass=900,p=vector(200,0,0),Potential=0,v=0,link =[bool]*active)
    n[x].v = n[x].p/n[x].mass
    n[x].pos+=(-10,0,.3)#starting point of objects
    n[x].make_trail=True



n[6]=sphere(pos=(2,1,0),color=(1,1,.5),make_trail=False,# just a single partical
            radius=.7,mass=900,p=vector(-200,0,0),Potential=0,v=0,link =[bool]*active)
n[6].v = n[6].p/n[6].mass


j=0
t=0  
dt=.1
Islinked(n,active)
while(t < 250):
    rate(60)
    for m in range(0,active):#changing postion
        n[m].v = 0.5*(n[m].v + n[m].p/n[m].mass)
        n[m].pos+=n[m].v*dt
    for l in range(0,active):#Calculations of force between all objects
        for a in range(l+1,active):
            j=n[l].pos-n[a].pos
            dis=mag(j)

            if(n[l].link[a]==true):Forcelinked(l,a,j,dis)#calling functions
            else: Forceunlinked(n[l],n[a],j,dis)
            

    t += dt

