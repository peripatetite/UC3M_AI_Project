import csv
import numpy as np

n_counts = np.zeros((8, 8))
e_counts = np.zeros((8, 8))
w_counts = np.zeros((8, 8))

lights = {'N': n_counts, 'E': e_counts, 'W': w_counts}

states = {
    "LowLowLow": 0,
    "HighLowLow": 1,
    "LowHighLow": 2,
    "LowLowHigh": 3,
    "HighHighLow": 4,
    "HighLowHigh": 5,
    "LowHighHigh": 6,
    "HighHighHigh": 7
}

with open('../resources/TrafficData.txt') as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    next(data)

    for row in data:
        old_state = row[0] + row[1] + row[2]
        action = row[3]
        new_state = row[4] + row[5] + row[6]

        i = states[old_state]
        j = states[new_state]

        l = lights[action]
        l[i][j] = l[i][j] + 1

    n_totals = np.sum(n_counts, axis=1)
    e_totals = np.sum(e_counts, axis=1)
    w_totals = np.sum(w_counts, axis=1)

    n_totals.reshape(1, 8)[:, 1:]

    n_totals = n_totals
    n_prob = n_counts/n_totals

    n_prob = np.nan_to_num(n_prob, nan=0, posinf=0)
    e_prob = e_counts/e_totals
    e_prob = np.nan_to_num(e_prob, nan=0, posinf=0)
    w_prob = w_counts/w_totals
    w_prob = np.nan_to_num(w_prob, nan=0, posinf=0)

    values = np.zeros(8)

    for iterations in range(500):
        for v in range(len(values)):
            v_n = 1 + sum(n_prob[v] * values)
            v_e = 1 + sum(e_prob[v] * values)
            v_w = 1 + sum(w_prob[v] * values)

            e = (min(v_n, v_e, v_w))
            if e == v_n:
                print("n")
            elif e == v_e:
                print("e")
            else:
                print("w")

            values[v] = e
        #print(values)
