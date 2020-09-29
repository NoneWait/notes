import numpy as np


emission_p = np.zeros((7, 5))
transition_p = np.zeros((8, 7))

ob = np.array([])

T = len(ob)
N = len(transition_p[0])

viterbi = np.zeros((len(ob), len(transition_p[0])))
backpointer = np.zeros((len(ob), len(transition_p[0])))

# 初始化
for s in range(1, len(transition_p[0]))
    viterbi[s, 1] = transition_p[0][s]
    backpointer[s, 1] = 0

# 迭代
for t in range(2, T):
    for s in range(1, N):
        viterbi[s, t] = max(
            [viterbi[s_, t-1]*transition_p[s_][s] for s_ in range(1, N)]
        )




