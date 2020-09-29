import numpy as np


emission_p = np.zeros((7, 5))
transition_p = np.zeros((8, 7))

transition_p = ["0.2767 0.0006 0.0031 0.0453 0.0449 0.0510 0.2026",
"0.3777 0.0110 0.0009 0.0084 0.0584 0.0090 0.0025",
"0.0008 0.0002 0.7968 0.0005 0.0008 0.1698 0.0041",
"0.0322 0.0005 0.0050 0.0837 0.0615 0.0514 0.2231",
"0.0366 0.0004 0.0001 0.0733 0.4509 0.0036 0.0036",
"0.0096 0.0176 0.0014 0.0086 0.1216 0.0177 0.0068",
"0.0068 0.0102 0.1011 0.1012 0.0120 0.0728 0.0479",
"0.1147 0.0021 0.0002 0.2157 0.4744 0.0102 0.0017"]
transition_p = [v.split(" ") for v in transition_p]
# print(transition_p)
transition_p = np.array(transition_p, dtype=float)

emission_p = [
"0.000032 0 0 0.000048 0",
"0 0.308431 0 0 0",
"0 0.000028 0.000672 0 0.000028",
"0 0 0.000340 0 0",
"0 0.000200 0.000223 0 0.002337",
"0 0 0.010446 0 0",
"0 0 0 0.506099 0"]

emission_p = [v.split(" ") for v in emission_p]
emission_p = np.array(emission_p, dtype=float)

ob = np.array([0, 1, 2, 3, 4])

T = len(ob)
N = len(transition_p[0])

viterbi = np.zeros((N, T))
backpointer = np.zeros((N, T))

# 初始化
for s in range(1, N):
    viterbi[s, 1] = transition_p[0][s]
    backpointer[s, 1] = 0

print(viterbi)

# 迭代
for t in range(2, T+1):
    for s in range(1, N):
        seq_score = [viterbi[s_, t-1]*transition_p[s_][s]*emission_p[s][ob[t]] for s_ in range(1, N)]
        
        viterbi[s, t] = max(seq_score)
        backpointer = np.argmax(seq_score)

print(viterbi)

bestpathprob = max([viterbi[s][T-1] for s in range(1, N)])

print(bestpathprob)




