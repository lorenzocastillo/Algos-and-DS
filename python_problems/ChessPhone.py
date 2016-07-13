from collections import defaultdict

from DataStructures.LinkedList import LinkedList


def distribute(a_list, val):
    c = LinkedList()
    #print('distribute ', a_list, "| val ", val)
    for elem in a_list:
        c.append(val + elem.data)
    return c
def trace(f):
    f.indent = 0
    def g(x,y,z):
        print('|  ' * f.indent + '|--', f.__name__, x,z)
        f.indent += 1
        value = f(x,y,z)
        print('|  ' * f.indent + '|--', 'return', repr(value))
        f.indent -= 1
        return value
    return g

phone_board = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
ROOK = 1
moves = {ROOK : [(0,1),(-1,0),(1,0),(0,-1)]}
LENGTH_OF_NUMBER = 10
def is_valid_move(pos, move):
    x, y = (pos[0] + move[0], pos[1] + move[1])
    return ((x,y), (x >= 0 and y >= 0 and x < len(phone_board) and y < len(phone_board[0]) and phone_board[x][y] != -1))

result = set()
visited = set()
cache = defaultdict(list)

def dfs(start,piece, phone_num):
    temp_res = list()
    for move in moves[piece]:
        new_pos,is_valid = is_valid_move(start,move)
        if is_valid:
             r,c = new_pos
             number = phone_board[r][c]
             temp = phone_num + (number,)
             if temp not in visited:
                 #print("Start ",start, "phone_num ", phone_num, "number ", number, "temp_res ",temp_res)
                 visited.add(temp)                
                 if len(temp) == LENGTH_OF_NUMBER:
                     temp_res.append((number,))
                     cache[len(temp),number].append((number,))
                     #print("LON: ", temp_res, "num ", temp)
                 else:
                     if (len(temp),number) in cache:
                         #print('hit:', len(temp), number)
                         temp_res = temp_res + cache[(len(temp),number)]
                     else:
                         res = dfs(new_pos,piece,temp)
                         res = [ (number,) + elem for elem in res ]
                         #print('result from call: ', res)
                         temp_res = res + temp_res
                         updated_res = cache[len(temp),number] + res
                         cache[(len(temp),number)] = updated_res

               
    return temp_res

def dfs_brute(start,piece, phone_num):
    for move in moves[piece]:
        new_pos,is_valid = is_valid_move(start,move)
        if is_valid:
             r,c = new_pos
             number = phone_board[r][c]
             temp = phone_num + (number,)
             if temp not in visited:
                 visited.add(temp)
                 if len(temp) == LENGTH_OF_NUMBER:
                     result.add(temp)
                 else:
                     dfs_brute(new_pos,piece,temp)
    return []          

def solve():
    piece = ROOK
    
    for r,_ in enumerate(phone_board):
        for c,_ in enumerate(phone_board[r]):
            start = (r,c)
            phone_num = (phone_board[start[0]][start[1]],)
            if phone_num[0] == -1:
                continue
            visited.add(phone_num)
            res = dfs(start, piece, phone_num)
            res = [ phone_num + elem for elem in res ]
            cache[(len(phone_num),phone_num[0])] = res
    for k in cache:
        if k[0] == 1:
            for res in cache[k]:
                result.add(res)

#dfs2 = trace(dfs2)
solve()
#dfs = memoize(dfs)
##print(cache)
##
##print('solving...')
#t = timeit.Timer(solve).timeit(number = 1)
#print(t)
print(LENGTH_OF_NUMBER, len(result))







