"""Cubic floor: least y>1 with y^3 == 1 (mod P_r) and least y>1 with y^3 == -1 (mod P_r).
y == +-1 (mod Q), Q = product of q <= p_r with q != 1 (mod 3);  y == +-rho (mod M),
M = product of q == 1 (mod 3), rho running over the 3^pi1 cube roots of 1 mod M."""
import math, sys
from sympy import prime
R=int(sys.argv[1])
def cube_roots_one(q):
    return [y for y in range(1,q) if pow(y,3,q)==1]
for r in range(1,R+1):
    ps=[prime(i) for i in range(1,r+1)]; P=math.prod(ps)
    Q=math.prod(q for q in ps if q%3!=1); Ms=[q for q in ps if q%3==1]; M=math.prod(Ms)
    # roots of rho^3 == 1 mod M by incremental CRT
    roots=[1]; mod=1
    for q in Ms:
        rq=cube_roots_one(q); new=[]
        inv=pow(mod,-1,q)
        for a in roots:
            for b in rq:
                new.append(a+mod*(((b-a)*inv)%q))
        roots=new; mod*=q
    invQ=pow(Q,-1,M) if M>1 else 0
    best={}
    for s in (1,-1):
        b=None
        for rho in roots:
            y=(s + Q*(((s*rho - s)*invQ) % M)) % (Q*M) if M>1 else s % Q
            if y<=1: y+=Q*M
            if b is None or y<b: b=y
        best[s]=b
    lg=math.log(P)
    print(f"{r:2d} {ps[-1]:4d} {len(roots):8d} {best[1]} {best[-1]} {math.log(best[1])/lg:.3f} {math.log(best[-1])/lg:.3f} {math.log(Q)/lg:.3f}")
