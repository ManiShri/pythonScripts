s = ("enter the size of groups:")
list1 = ["1","2","3","4","1","2","3","4","1","2","3","4"]
def group(x,l):
        li=len(x)/l+len(x)%l
        gl=[]
        g=[]
        i=0
        while i<len(x):
                if(len(gl)<l):
                        gl.append(x[i])
                        i=i+1
                else:
                        g.append(gl)
                        gl=[]
        g.append(gl)
        return g
print (group([1,3,2,2,9,7,2,4],3))
print (group(list1,3))
