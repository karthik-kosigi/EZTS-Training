s="wordzzuspay"
en=""
for i in s:
    no=ord(i.lower())+5
    if no>122:
        ex=no%122
        en+=(chr(96+ex))
    else:
        en+=(chr(no))
print(en)

