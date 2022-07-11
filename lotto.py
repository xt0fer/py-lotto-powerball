# lotto picker by manny juan  (juanm@wellsfargo.com or manny@bdt.com)

from random import randint


def pick_lotto():
    maxm = 53
    maxj = 6
    m = maxm
    r = list(range(m + 1))
    v = []
    for j in range(maxj):
        i = randint(1, m)
        n = r[i]
        r[i:i + 1] = []
        m = m - 1
        v.append(n)
    return v


def run():
    done = 0
    while not done:
        try:
            x = input('\npress Enter for Lotto picks (Q to quit). ')
        except EOFError:
            x = 'q'
        if x and (x[0] == 'q' or x[0] == 'Q'):
            done = 1
            print('done')
        else:
            print(pick_lotto())


# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    run()
else:
    print("Module lotto imported.")
    print("To run, type: lotto.run()")
    print("To reload after changes to the source, type: reload(lotto)")
# end of lotto.py
