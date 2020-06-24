print('i\t\t\tm(i)')
i=1
while(i<1000):
    m = 0
    count = 1
    while(i>=count):
        if(count%2 == 1):
            m = m + 1/(2*count-1)
        else:
            m = m - 1/(2*count-1)
        count = count + 1
    m = m*4
    print(i,'\t\t\t',m)

    i=i+100
