import Teleport

c = Teleport.Generate()

i = 0
while i<=100000:
    c.addAtom(Teleport.Atom.H,0,0,i)
    i+=1