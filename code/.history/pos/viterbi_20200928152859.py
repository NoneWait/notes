import numpy as np


emission_p = np.zeros((7, 5))
transition_p = np.zeros((8, 7))

ob = np.array([])


viterbi = np.zeros((len(ob), len(transition_p[0])))
backpointer = np.zeros((len(ob), len(transition_p[0])))

for s in range(len(transition_p[0]))
    viterbi[s, 1] = transition_p[0][s]
    




