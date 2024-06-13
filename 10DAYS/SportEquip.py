with open("Equipments.txt",'r') as f:
    equip = f.readlines()
    s=equip[0]
    f.close()

s=s.replace("unavailable","avail")
with open("Equipments.txt",'w') as f:
    f.write(s)
    f.close()