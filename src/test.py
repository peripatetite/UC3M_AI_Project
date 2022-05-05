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

    n_totals = np.delete(n_totals, 0, 0)
    n_counts = np.delete(n_counts, 0, 0)

    e_totals = np.delete(e_totals, 0, 0)
    e_counts = np.delete(e_counts, 0, 0)

    w_totals = np.delete(w_totals, 0, 0)
    w_counts = np.delete(w_counts, 0, 0)

    n_prob = np.zeros((7, 8))
    e_prob = np.zeros((7, 8))
    w_prob = np.zeros((7, 8))


    for i in range(7):
        n_prob[i] = n_counts[i] / n_totals[i]
        e_prob[i] = e_counts[i] / e_totals[i]
        w_prob[i] = w_counts[i] / w_totals[i]

    values = np.zeros(8)
    temp_vals = values.copy()

    # Calculate the Bellman Equations
    for iterations in range(500):
        for v in range(len(values) - 1):
            v_n = 1 + sum(n_prob[v] * values)
            v_e = 1 + sum(e_prob[v] * values)
            v_w = 1 + sum(w_prob[v] * values)

            e = (min(v_n, v_e, v_w))
            temp_vals[v + 1] = e
        values = temp_vals.copy()
    print(values)

    # values now holds accurate values for each V(s)
    # Now we can calculate the optimal policy for each state
    optimals = []
    for v in range(len(values) - 1):
        v_n = 1 + sum(n_prob[v] * values)
        v_e = 1 + sum(e_prob[v] * values)
        v_w = 1 + sum(w_prob[v] * values)

        e = (min(v_n, v_e, v_w))
        if e == v_n:
            optimals.append('n')
        elif e == v_e:
            optimals.append('e')
        else:
            optimals.append('w')
    print(optimals)

    print(e_prob)


