import string
from collections import defaultdict
import copy


letters_unset = list(string.ascii_uppercase[:25])
letters_set = []
numbers_unfilled = range(25)
numbers_filled = []
positions = {}
letters_adj = defaultdict(set)


def print_grid():
    grid_line = ['-']*25
    for letter in letters_set:
        pos = positions[letter]
        grid_line[pos] = letter
    grid_box = [' '.join(grid_line[j:j+5]) for j in range(0, 25, 5)]
    print '\n'.join(grid_box)
    print ''

def place_letter(l, i):
    positions[l] = i
    letters_unset.remove(l)
    letters_set.append(l)
    numbers_unfilled.remove(i)
    numbers_filled.append(i)
#    print l, i


def get_input(n):
    grid = ''.join(open('inputs/input{}/grid.txt'.format(str(n))).read().split())
    words = open('inputs/input{}/words.txt'.format(str(n))).read().split('\n')

    for i in range(25):
        if grid[i].isalpha():
            place_letter(grid[i], i)

    for word in words:
        for j in range(len(word)-1):
            letters_adj[word[j]].add(word[j+1])
            letters_adj[word[j+1]].add(word[j])


def in_range(n):
    if n < 0:
        return 0
    elif n > 4:
        return 4
    else:
        return n

def neighbours(n):
    assert n in range(25)
    x = n % 5
    y = n / 5
    x_min, x_max = in_range(x-1), in_range(x+1)
    y_min, y_max = in_range(y-1), in_range(y+1)
    neighbourhood = set()
    for j in range(y_min, y_max+1):
        for i in range(x_min, x_max+1):
            m = j*5 + i
            if m != n and m not in numbers_filled:
                neighbourhood.add(m)
    return neighbourhood

def common_neighbours(pos_list):
    neighbourhoods = [neighbours(i) for i in pos_list]
    if len(neighbourhoods) != 0:
        return list(set.intersection(*neighbourhoods))

def possible_positions(l):
    if l in letters_set:
        return positions[l]
    else:
        pos_adj = []
        for l_adj in letters_adj[l]:
            if l_adj in letters_set:
                pos_adj.append(positions[l_adj])
        return common_neighbours(pos_adj)

def all_possible():
    all_pos = {}
    for letter in list(string.ascii_uppercase[:25]):
#        if letter in letters_set:
#            all_pos[letter] = [positions[letter]]
#        else:
        all_pos[letter] = possible_positions(letter)
    return all_pos


def set_unique(l):
    if l in letters_set:
        pass
    else:
        pos_pos = possible_positions(l)
        if pos_pos == 0:
            pass
        elif len(pos_pos) == 1:
            place_letter(l, list(pos_pos)[0])


def set_all_unique():
    unset_queue = copy.deepcopy(letters_unset)
    for l in unset_queue:
        set_unique(l)
    set_count = len(unset_queue) - len(letters_unset)
    return set_count


def possible_letters():
    pos_let = defaultdict(list)
    for l in letters_unset:
        pos_pos = possible_positions(l)
#        print l, pos_pos
        if pos_pos != 0:
            for pos in pos_pos:
                pos_let[pos].append(l)
    return pos_let


def fill_first_unique():
    pos_let = possible_letters()
    print pos_let
    print_grid()
    for pos in pos_let.keys():
        if len(pos_let[pos]) == 1:
            place_letter(pos_let[pos][0], pos)
            return True
    return False

def fill_all_unique():
    start_tot = len(numbers_filled)
    while True:
        return fill_first_unique()
    end_tot = len(numbers_filled)
    return end_tot - start_tot


def set_unique_cycle():
    while True:
        if len(letters_unset) == 0:
            return False
        else:
            count = set_all_unique()
            if count == 0:
                return False

def set_cycle_fill_first():
    set_unique_cycle()
    fill_first_unique()

get_input(1)

print positions
print all_possible()