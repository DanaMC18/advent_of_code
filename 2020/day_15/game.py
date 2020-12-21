"""Game module."""

inputs = [9, 19, 1, 6, 0, 5, 4]


def play_game(last_turn=2020):
    """Get spoken number on specified turn."""
    spoken = dict()

    for i in range(len(inputs)):
        speak = inputs[i]
        if spoken.get(speak):
            spoken[speak].append(i + 1)
        else:
            spoken[speak] = [i + 1]

    turn = i + 2
    prev = inputs[-1]

    while turn <= last_turn:
        if not spoken.get(prev):
            prev = 0
        else:
            turns = spoken[prev][-2:]
            prev = turns[1] - turns[0] if len(turns) > 1 else 0

        if spoken.get(prev):
            spoken[prev].append(turn)
        else:
            spoken[prev] = [turn]
        turn += 1

    return prev


# SOUTION 1 | 1522
# print(play_game())

# SOULTION 2 | 18234
# print(play_game(30000000))
