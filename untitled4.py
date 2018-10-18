def timeConversion(s):
    #
    # Write your code here.
    b = s.split(':')
    if b[2][2].lower() == 'p':
        b[0] = str(int(b[0]) + 12)
    b[2] = b[2][:2]
    ans = b[0] + ':' + b[1] + ':' + b[2]
    print(ans)
    
timeConversion('07:05:45PM')
timeConversion('03:05:45AM')
timeConversion('12:05:45PM')
timeConversion('12:05:45AM')
timeConversion('07:05:45PM')