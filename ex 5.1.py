num = 0
tot = 0.0
while True :
    val1 = input('Enter a number: ')
    if val1 == 'done' :
        break
    try:
        val2 = float(val1)
    except:
        print('Invalid Input')
        continue
    #print(val2)
    num = num + 1
    tot = tot + val2

#print('All Done')
print(tot,num,tot/num)