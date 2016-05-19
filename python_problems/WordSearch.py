deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

board = [

    "swingh",
    "abcdef",
    "rettel",
    "ayzgfd",
    "cmwing"

    ]

ROWS = len(board)
COLS = len(board[0])

dictionary = ["swing","wing",'letter']
dictionary.sort()

print(dictionary)

def inDictionary(dictionary, word):
    return word in dictionary

#(x,y) -> (r,c)
def inBounds(point):
    return adj[0] >= 0 and adj[1] >= 0 and adj[0] < ROWS and adj[1] < COLS
#append to string in C
results = set()
for delta in deltas:
    for i, row in enumerate(board): # for int i = 0; i < ROWS; i++ -> row = board[i]
        for j, letter in enumerate(row): # for int j = 0 ; j < ROWS; j++ -> letter = row[j]
            adj = (i,j)
            string = "" # char word [COLS] 
            while inBounds(adj):
                string += board[adj[0]][adj[1]]
                if inDictionary(dictionary,string):
                    print(string)
                adj = (adj[0] + delta[0], adj[1] + delta[1]) #0,6
            
#print(sorted(list(results)))
