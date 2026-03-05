"""
Given two strings representing your army and an opposing army, each character from 
your army battles the character at the same position from the opposing army using the 
following rules:

Characters a-z have a strength of 1-26, respectively.
Characters A-Z have a strength of 27-52, respectively.
Digits 0-9 have a strength of their face value.
All other characters have a value of zero.
Each character can only fight one battle.
For each battle, the stronger character wins. The army with more victories, wins the war. 
Return the following values:

"Opponent retreated" if your army has more characters than the opposing army.
"We retreated" if the opposing army has more characters than yours.
"We won" if your army won more battles.
"We lost" if the opposing army won more battles.
"It was a tie" if both armies won the same number of battles.
"""

def battle(my_army, opposing_army):
    """
    Simulates a battle between two armies.
    Args:
        my_army (str): Our army string
        opposing_army (str): Opposing army string
    Returns:
        str: Battle result - "Opponent retreated", "We retreated", 
        "We won", "We lost", or "It was a tie"

    """
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(opposing_army) > len(my_army):
        return "We retreated"

    my_wins = 0
    opponent_wins = 0

    def get_strength(char):
        if 'a' <= char <= 'z':
            return ord(char) - ord('a') + 1
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 27
        elif '0' <= char <= '9':
            return int(char)
        else:
            return 0

    #enumerate is better choice
    for i in range(len(my_army)):
        my_strength = get_strength(my_army[i])
        opponent_strength = get_strength(opposing_army[i])

        if my_strength > opponent_strength:
            my_wins += 1
        elif opponent_strength > my_strength:
            opponent_wins += 1

    if my_wins > opponent_wins:
        return "We won"
    elif opponent_wins > my_wins:
        return "We lost"
    else:
        return "It was a tie"
