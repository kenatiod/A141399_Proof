"""Exact per-order classification of y >= 2 with y^3 - 1 or y^3 + 1  p_r-smooth.

y^3 -/+ 1 = d w^3 with d cube-free p_r-smooth  <=>  (x,Y) = (+/-y, +/-w) solves x^3 - d Y^3 = 1.
By Bennett (2001) [also Delone-Nagell for n = 3] each d gives at most one solution with Y != 0.
Run PARI's Thue solver for every cube-free p_r-smooth d > 1 (3^r - 1 equations).
flag=1 in thueinit makes the result unconditional; flag=0 assumes GRH."""
import sys, time, itertools, cypari2
pari=cypari2.Pari(); pari.allocatemem(2*10**9, silent=True)
from sympy import prime, factorint
R=int(sys.argv[1]); FLAG=int(sys.argv[2]) if len(sys.argv)>2 else 1
ps=[prime(i) for i in range(1,R+1)]
def smooth_order(n):
    """return (is p_R-smooth, set of primes) """
    f=factorint(n)
    return all(p<=ps[-1] for p in f), set(f)
t=time.time(); found=[]
for exps in itertools.product(range(3), repeat=R):
    d=1
    for p,e in zip(ps,exps): d*=p**e
    if d==1: continue
    sols=pari(f"thue(thueinit(x^3-{d},{FLAG}),1)")
    for s in sols:
        x,Y=int(s[0]),int(s[1])
        if Y==0 or abs(x)<2: continue
        y=abs(x); form="y^3-1" if x>0 else "y^3+1"
        N=y**3-1 if x>0 else y**3+1
        ok,sup=smooth_order(N)
        if ok:
            r=max(ps.index(p)+1 for p in sup)
            pc = sup==set(ps[:r])
            found.append((y,form,d,r,pc))
el=time.time()-t
found=sorted(set(found))
print(f"r<={R} (flag={FLAG}): {3**R-1} Thue equations in {el:.0f}s; {len(found)} values y>=2 with y^3-/+1 p_{R}-smooth")
for y,form,d,r,pc in found:
    print(f"  y={y:>12d}  {form}  d={d}  gpf-order={r}  prime-complete={pc}")
