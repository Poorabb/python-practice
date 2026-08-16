values={'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

s = 'IXL'
int = values[s[0]]
for i in range (1,len(s)):
    if values[s[i]] > values[s[i-1]]:
        int = (int + values[s[i]]) - (2 * values[s[i-1]])
    else: 
        int = int + values[s[i]]

print(int)

#    print(values[s[i]])
