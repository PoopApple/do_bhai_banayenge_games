from collections import defaultdict

WIN_PATTERNS = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def main():
    board = "---------"
    
    a = "012345678"
    corners = [0,2,6,8]
    middle = [1,3,5,7]
    center = 4
    
    first_move = "corner or middle or center"
    
    if first_move in corners:
        next_move = center
    elif first_move in center:
        next_move = corners
    elif first_move in middle:
        next_move = corners

    #cornerx  centero
    
    
if __name__ == "__main__":
    main()