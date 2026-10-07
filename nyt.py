""" def spaces (n, Y, T):
    x = 0
    for i in range (n):
        if Y[i] == "C" and T[i] == Y[i]:
            x+=1
    return x
print(spaces (5, "CC..C", ".C.C..")) """\


def engfr (text):
    s=0
    t=0
    text==text.lower
    print(len(text(s)))
    s += 1
    for i in range (len(text)):
        if s > t:
            print("french")
        elif s < t:
            print("english")
        else:
            print("french")
engfr ("The cat is mad")