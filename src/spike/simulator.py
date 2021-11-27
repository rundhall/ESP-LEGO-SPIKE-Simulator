import random,time

class Simulator:
    def remap(self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
      
    def get_new_value(self,
                      isdebug=True,
                      newreading=-1,
                      minvalue = 0,
                      maxvalue = 100,
                      minreading=0,
                      maxreading=200):

        actualvalue = newreading
        if(isdebug):print("actualvalue ",str(actualvalue)," minreading: "+str(minreading)," maxreading: "+str(maxreading)," minvalue: "+str(minvalue)," maxvalue: "+str(maxvalue))
        actualvalue = int(self.remap(actualvalue, minreading, maxreading, minvalue, maxvalue))
        return int(actualvalue)
