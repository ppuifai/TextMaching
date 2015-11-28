def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1

  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]

    # split aList between lists
    for  i in aList:
      tmp = i // placement
##      print ("i is " , i)
##      print ("placement is " , placement)
##      print ("tmp is ", tmp)
##      print ("tmp % RADIX is ", tmp % RADIX)
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False

    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1

    # move to next digit
    placement *= RADIX
  return aList


def BoyerMooreHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return -1


if __name__ == '__main__':

    print "Product Search - Input your keyword (s):"
    pattern = raw_input()
    patternSP = pattern.split()
    #print patternSP[0]
    #print patternSP[1]
    
    sumX=[0]*1024   

    with open('product.txt')as f:
        text = f.readlines()
    
    
    num=0
    for a in range(0,len(text)):
        s = BoyerMooreHorspool(patternSP[0], text[a])
        s1 = BoyerMooreHorspool(patternSP[1], text[a])
        x1='0'
        x2='0'
        x3='0'
        x4='0'
        if( s > -1 or s1 > -1 ):
        #   print s
            num = a
            if(s > -1 and s1 == -1):
                x4=num
                x4=str(x4).zfill(4)
                x3='20000'
                x2=s*100
                x2=str(x2).zfill(4)
                x1=99
                x1=str(x1).zfill(2)
                sumX[a]=int(x3)+int(x2)+int(x1)
                sumX[a]=str(sumX[a])+x4
                sumX[a]=int(sumX[a])
                #print x3,x2,x1,x4,sumX[a]
                print text[a] 
            if(s1 > -1 and s == -1):
                x4=num
                x4=str(x4).zfill(4)
                x3='10000'
                x2=s1*100
                x2=str(x2).zfill(4)
                x1=99
                x1=str(x1).zfill(2)
                sumX[a]=int(x3)+int(x2)+int(x1)
                sumX[a]=str(sumX[a])+x4
                sumX[a]=int(sumX[a])
                #print x3,x2,x1,x4,sumX[a]
                print text[a] 
            if(s > -1 and s1 > -1):
                x4=num
                x4=str(x4).zfill(4)
                x3='30000'
                x2=s*100
                x2=str(x2).zfill(4)
                x1=abs(s1-s)
                x1=str(x1).zfill(2)
                sumX[a]=int(x3)+int(x2)+int(x1)
                sumX[a]=str(sumX[a])+x4
                sumX[a]=int(sumX[a])
                #print x3,x2,x1,x4,sumX[a]
                print text[a] 
        
    #print sumX

sumX = [x for x in sumX if x != 0]
#print sumX
re=radixsort(sumX)
#print radixsort(sumX)
re.reverse()
#print re
ii=input('Enter argument =')
for i in range(0,len(re)):
    if(i==ii or i==10):
        break
    index = re[i] % 1000
    print i+1,'-',text[index]



    

            
        
        


        
