# Example for creating Methods in Python
import numbers

class PS:
    def __init__(self):
        self.space = [i for i in range(20)]
    def usespace(self,vehtype):
        if(vehtype=='large'):
            for i in self.space:
                if((i,i+1,i+2)!=('x','x','x')):
                    self.space[i:i+3]=['x','x','x']
                    return i 
                else:print("Sorry, parking space is not available")    
        elif(vehtype=='medium'):
            for i in self.space:
                if((i,i+1)!=('x','x')):
                    self.space[i:i+2]=['x','x']
                    return i
                else:print("Sorry, parking space is not available")

        elif(vehtype=='small'):
            for i in self.space:
                if(i!='x'):
                    self.space[i]=['x']
                    return i    
                else:print("Sorry, parking space is not available")
        else:
            print("Wrong input!")

Park=PS()
spd=0
class User:
    
    # instance attributes
    def __init__(self, vehid, vehtype,sid):
        self.vehid = vehid
        self.vehtype = vehtype
        self.sid=sid

def spotid(Obj,vt):
    Obj.usespace(vt)

while (Park.space.count('x')!=20):
    vid=input("Enter the Vehicle ID: ")
    vtype=input("Enter the Vehicle Type: ")


    a=spotid(Park,vtype)
    if(isinstance(a,numbers.Number)==True):
        spd=a
    user=User(vid,vtype,spd)
    print("Spot ID: ",user.sid,"\n")
    print("Vehicle ID: ",user.vehid,"\n")    

print("You have either exited the system or there are no more parking spaces left")    



