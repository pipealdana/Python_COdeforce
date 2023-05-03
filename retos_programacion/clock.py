tc = (int(input()))
n = 12

while tc > 0:
    line = input()
    st = line.split(" ")
    s = st[0]
    x = int(st[1])
    h, m=map(int, s.split(":"))
    ans=0

    while n:
        m += x
        if m >= 60:
            h += m // 60
            m = m % 60
        if h >= 24:
            h = h % 24
        ss = f"{h:02d}:{m:02d}"
        hh = str(f"{h:02d}")
        mm = str(m)
        sr = hh[::-1] +":"+ mm[::-1]
        stop = hh +":"+ mm
        print("ss =", ss, "sr =", sr, "stop =", stop)

        if (s==sr):
            ans += 1
            print(ans)
        #if (s==stop): break
        n -= 1

    print(ans)
    tt -= 1

""" TEST CASE
03:12 360
1
"""