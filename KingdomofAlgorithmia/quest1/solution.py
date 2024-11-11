POTIONS = {
    "x": 0,
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5
}

def solution_1():
    with open("input1", "r") as f:
        monsters = f.read()

    print("part 1: ", sum(POTIONS[m] for m in monsters))


def solution_2():
    with open("input2", "r") as f:
        monsters = f.read()

    total = 0
    for n in range(0, len(monsters), 2):
        left = monsters[n]
        right = monsters[n+1]

        total += POTIONS[left] + POTIONS[right]
        if "x" not in (left, right):
            total += 2

    print("part 2: ", total)

def solution_3():
    with open("input3", "r") as f:
         monsters = f.read()

    total = 0
    for n in range(0, len(monsters), 3):
        real_monster_count = len([m for m in monsters[n:n + 3] if m != "x"])
        total += sum(POTIONS[m] for m in monsters[n:n+3])
        if real_monster_count == 2:
            total+=2
        if real_monster_count == 3:
            total+=6
    print("part 3: ", total)



if __name__ == "__main__":
    solution_1()
    solution_2()
    solution_3()
