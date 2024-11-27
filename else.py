#for else: loop is terminated control will not enter into the else block
for i in range(1,25):
    if i==12:
        continue
    print(i)
else:
    print('loop is not terminated')

# loop is not terminated control will enter into the else block
for i in range(1,25,2):
    if i==32:
        continue
    print(i)
else:
    print('loop is not terminated')




# while else: loop is terminated control will not enter into the else block
i=1
while(i<22):
    if i==15:
        break
    print(i)
    i+=1
else:
    print('loop is not terminated')

#loop is not terminated control will enter into the else block
i=1
while(i<25):
    if i==30:
        break
    print(i)
    i+=1
else:
    print('loop is not terminated')
