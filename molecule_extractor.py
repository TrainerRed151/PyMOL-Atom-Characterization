# Copyright © 2020 Brian Pomerantz. All Rights Reserved.

import sys


def main():
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    f.close()

    data = {}
    for line in lines:
        if 'ATOM' not in line:
            continue

        ll = line.split()
        mol_desi = ll[16]
        nucleotide = len(ll[5]) == 1 and ll[5] in ['A', 'C', 'G', 'U']
        if mol_desi not in data:
            data[mol_desi] = [set(), nucleotide]
        data[mol_desi][0].add(int(ll[8]))

    for d in data:
        ll_out = list(data[d][0])
        ll_out.sort()
        print(f'{d}:\t{len(ll_out)}\t', end='')
        if data[d][1]:
            previous = -10
            in_dash = False
            first = True
            for n in ll_out:
                if n - previous == 1:
                    if in_dash:
                        previous = n
                        continue
                    else:
                        print('-', end='')
                        in_dash = True
                else:
                    if in_dash:
                        print(f'{previous}, {n}', end='')
                        in_dash = False
                    else:
                        if first:
                            print(f'{n}', end='')
                            first = False
                        else:
                            print(f', {n}', end='')
                previous = n
            if in_dash:
                print(previous)
            else:
                print()
        else:
            print()


if __name__ == '__main__':
    main()
