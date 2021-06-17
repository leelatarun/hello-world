def computepay(hs, rt):
    if hs > 40 :
        pa =  (40 * rt) + 1.5 *rt * (hs - 40)
    else :
        pa = hs*rt
    return pa

hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)
