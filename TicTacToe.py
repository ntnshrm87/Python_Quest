from itertools import combinations

# Board for TicTacToe
#      1 |  2 |  3 |
#      4 |  5 |  6 |
#      7 |  8 |  9 |

# Variables for different functions defined globally
arr_pos = [1,2,3,4,5,6,7,8,9]
win_pos = [['1','4','7'], ['2','5','8'], ['3','6','9'], ['1','2','3'], ['4','5','6'], ['7','8','9'], ['1','5','9'], ['3','5','7']]
p1_pos = []
p2_pos = []
filled_up = []
dpos = {}
pt1_turn = 'X'
pt2_turn = 'O'


def board(dpos):
    '''Function to print the updated board after each turn...'''
    ks = dpos.keys()
    print "\n"
    for i in range(1,10):
        if i in (4,7):
            print "\t"
        if str(i) in ks:
            print " " + dpos[str(i)] + " " + "| ",
        else:
            print  " _ " + "| ",


def turn():
    '''Function to run each player's turn...'''
    while(len(filled_up)!=9):
        pt1 = raw_input("\n Player 1: Enter your position for X - ")
        while pt1 in filled_up:
            pt1 = raw_input("\n Player 1: Enter correct position for X - ")
        fillpos(pt1,pt1_turn)

        if len(p1_pos) >= 3:
            if chk_winr(p1_pos):
                print("\n Player 1 wins...")
                break

        if len(filled_up) == 9:
            print("Game over with a tie... ;)")
            break

        pt2 = raw_input("\n Player 2: Enter your position for O - ")
        while pt2 in filled_up:
            pt2 = raw_input("\n Player 2: Enter correct position for O - ")
        fillpos(pt2,pt2_turn)

        if len(p2_pos) >= 3:
            if chk_winr(p2_pos):
                print("\nPlayer 2 wins...")
                break

def chk_winr(p_pos):
    '''Function to check for the winning player'''
    p_pos = "".join(p_pos)
    c = combinations(p_pos, 3)
    lst = [value for value in c if sorted(value) in win_pos]
    if len(lst) > 0:
        return True
    else:
        return False

def fillpos(pos, pturn):
    '''Function to fill each position with a turn either 'X' or 'O'...'''
    filled_up.append(pos)
    if pturn == 'X':
        p1_pos.append(pos)
    if pturn == '0':
        p2_pos.append(pos)
    dpos[pos] = pturn
    board(dpos)


def main():
    '''Main function to call the turn...'''
    result = turn()


if __name__ == "__main__":
    main()
