# import numpy
# from scipy.special import comb
import matplotlib.pyplot as plt

GRID_SIZE = 16
TOTAL_POINT = GRID_SIZE*GRID_SIZE
TOTAL_LEI = 40
ROI = 15
OUT_ROI = TOTAL_POINT - ROI
TOTAL_LEI = OUT_ROI + 3 # test
TWO_PRO = [0.0, 1.0/3, 1.0/5]
THREE_PRO = [1.0/5, 0.0, 2.0/5]

# 不需要使用组合数，可以提前化简
# C2 = comb(TOTAL_POINT-ROI,TOTAL_LEI-2)
# print(C2)
# C3 = comb(TOTAL_POINT-ROI,TOTAL_LEI-3)
# print(C3)

def prob_ABC(total_mine):
    t1 = (OUT_ROI - total_mine + 3)
    t2 = (total_mine - 2)
    P2 = t1/(t1 + t2)
    P3 = t2/(t1 + t2)
    # print(P2,P3)
    P = [P2*TWO_PRO[i] + P3*THREE_PRO[i] for i in range(3)]
    # print(P)
    P.append(P2)
    P.append(P3)
    return P

nn = list(range(2,OUT_ROI + 3))
PA = []
PB = []
PC = []
P2 = []
P3 = []
for i in nn:
    pa, pb, pc,p2,p3 = prob_ABC(i)
    PA.append(pa)
    PB.append(pb)
    PC.append(pc)
    P2.append(p2)
    P3.append(p3)

plt.plot(nn,PA)
plt.plot(nn,PB)
plt.plot(nn,PC)
plt.plot(nn,P2)
plt.plot(nn,P3)
plt.xlabel('Number of Mines')
plt.ylabel('Probability')
plt.legend(['P(A)','P(B)','P(C)','P(n=2)','P(n=3)'])
plt.savefig('probability.png')
plt.show()