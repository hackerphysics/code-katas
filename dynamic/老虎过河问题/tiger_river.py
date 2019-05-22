import sys
import numpy as np

ABLE = ["A","B","a","C",]
TIGERS = ["A","a","B","b","C","c"]
NT = 6

'''
新的方法：

1. 找到所有可能的状态组合nodes （一侧，另一侧）
2. 找到所有可能的穿上老虎组合 boats（）
3. 从初始状态开始，查找可能的下一个状态【node之间的边】
4. 将所有连接的边存入一个stack，并以此进行下一轮搜索

直到构建完成graph

'''

# 查找所有可能状态，建立节点
def search_node():
    nodes = set()
    boats = set()
    nodes.add((tuple(TIGERS),()))
    for i in range(NT):
        it = TIGERS[i]
        t = TIGERS[:]
        t.remove(it)
        if is_ok_one([it]) and is_ok_one(t):
            nodes.add((tuple(t),(it,)))
            nodes.add(((it,),tuple(t)))
        if is_in_boat([it]):
                boats.add((it,))
        for j in range(i+1,NT):
            t = TIGERS[:]
            jt = TIGERS[j]
            t.remove(it)
            t.remove(jt)
            if is_ok_one([it,jt]) and is_ok_one(t):
                nodes.add((tuple(t),(it,jt)))
                nodes.add(((it,jt),tuple(t)))
            if is_in_boat([it,jt]):
                boats.add((it,jt))
            
            for k in range(j+1,NT):
                kt = TIGERS[k]
                t = TIGERS[:]
                t.remove(it)
                t.remove(jt)
                t.remove(kt)
                if is_ok_one([it,jt,kt]) and is_ok_one(t):
                    nodes.add((tuple(t),(it,jt,kt)))
                    nodes.add(((it,jt,kt),tuple(t)))
                    print(i,j,k)
                    print(t,(it,jt,kt))
    nodes.add(((),tuple(TIGERS)))
    return nodes,boats

def is_in_boat(tigers):
    if len(tigers) > 2 or not is_ok_one(tigers):
        return False
    for i in ABLE:
        if i in tigers:
            return True
    return False

def is_ok_one(tigers):
    is_big = False
    is_danger = False
    for tiger in tigers:
        if not tiger.islower():
            is_big = True
    if is_big: # 如果有大老虎
        for tiger in tigers:
            if tiger.islower() and tiger.upper() not in tigers and len(tigers) != 1:
                return False # 小老虎非单独相处且没有妈妈在身边,不安全
    return True  


nodes,boats = search_node()
print('nodes\n')
for n in nodes:
    print(n)
print('boats\n',boats)
nodes = list(nodes)
boats = [ list(b) for b in boats]
n_node = len(nodes)
graph = np.zeros([n_node,n_node]) # 存储从i到j的距离
end_id = nodes.index(((),tuple(TIGERS)))
print('end_id: ',end_id)
start_id = nodes.index((tuple(TIGERS),()))
print("start_id",start_id)
reached_ids = set()
state_stack = []
action_stack = []
state_stack.append(end_id)
action_stack.append(True) # True 表示 穿运到对岸， Go

def is_near(a,b,is_go):
    # 从a状态到b状态根据 is——go 的动作是否能达到
    sa = nodes[a]
    sb = nodes[b]

    if is_go:
        s1 = list(sa[0])
        s2 = list(sb[0])
    else:
        s2 = list(sa[0])
        s1 = list(sb[0])
    # print(s1,s2)
    if len(s2) != 0:
        for s in s2:
            try:
                s1.remove(s)
            except:
                return False
    boat = s1
    if boat in boats:
        return True
    return False

while state_stack:
    current_id = state_stack.pop()
    current_action = action_stack.pop()
    if (current_id,current_action) not in reached_ids: # 如果一个id已经被计算过，则不需要再对他进行连接
        for i in range(n_node):
            # 填充 end_id 所在的列
            # 如果一个id已经被计算过，则不需要再对他进行连接
            if (i,current_action) not in reached_ids and is_near(i,current_id,current_action):
                print(nodes[i],nodes[current_id],current_action)
                graph[i,current_id] += 1
                state_stack.append(i) 
                action_stack.append(not current_action)   
        reached_ids.add((current_id,current_action))

# print(graph[:,21])
# print(graph[:,25])
# print(graph)

'''
def is_ok(one_side,boat,other_side):
    if is_ok_one(one_side) and is_ok_one(boat) and is_ok_one(other_side):
        # print('is_ok',one_side,boat,other_side)
        return True
    return False

def is_ok_one(tigers):
    is_big = False
    is_danger = False
    for tiger in tigers:
        if not tiger.islower():
            is_big = True
    if is_big: # 如果有大老虎
        for tiger in tigers:
            if tiger.islower() and tiger.upper() not in tigers and len(tigers) != 1:
                return False # 小老虎非单独相处且没有妈妈在身边,不安全
    return True  


def all_move_options(one_side,other_side):
    for i in range(len(one_side)):
        ii = one_side[i]
        
        one_side_new = one_side[:]
        other_side_new = other_side[:]
        boat = []

        one_side_new.remove(ii)
        boat.append(ii)
        other_side_new = other_side + boat

        if ii in ABLE and is_ok(one_side_new,boat,other_side_new):
            yield [one_side_new,other_side_new,boat]

        for j in range(i+1,len(one_side)):
            jj = one_side[j]
            
            if ii not in ABLE and jj not in ABLE:
                continue    
            one_side_new = one_side[:]
            other_side_new = other_side[:]
            boat = []
            # print(jj)
            one_side_new.remove(ii)
            one_side_new.remove(jj)
            boat.append(ii)
            boat.append(jj)
            other_side_new = other_side + boat

            if is_ok(one_side_new,boat,other_side_new):
                # print(ii,jj)
                yield [one_side_new,other_side_new,boat]

def all_back_options(one_side,other_side):
    for i in range(len(other_side)):
        ii = other_side[i]

        one_side_new = one_side[:]
        other_side_new = other_side[:]
        boat = []

        other_side_new.remove(ii)
        boat.append(ii)
        one_side_new.append(ii)

        if ii in ABLE and is_ok(one_side_new,boat,other_side_new):
            yield one_side_new,other_side_new,boat
        for j in range(i+1,len(other_side)):
            jj = other_side[j]

            if ii not in ABLE and jj not in ABLE:
                continue    

            one_side_new = one_side[:]
            other_side_new = other_side[:]
            boat = []

            other_side_new.remove(ii)
            other_side_new.remove(jj)

            boat.append(ii)
            boat.append(jj)

            one_side_new = one_side_new + boat
            if is_ok(one_side_new,boat,other_side_new):
                yield one_side_new,other_side_new,boat

def search(one_side_0,other_side_0):
    for one_side,other_side,boat in all_move_options(one_side_0,other_side_0):
        print('move:',one_side,other_side)
        if len(one_side) == 0:
            print('last:',['&'.join(boat)])
            return ['&'.join(boat)]
        else:
            for one_side2,other_side2,boat2  in all_back_options(one_side,other_side):
                if boat != boat2:
                    print('back',one_side2,other_side2)
                    r =  search(one_side2,other_side2)
                    if r is not None:
                        rr = ['&'.join(boat),'&'.join(boat2), r]
                        # if len(other_side_0) == 0:
                        print('result:',rr)
                        # else:
                        return rr
    return None 

r = search(one_side,other_side)
print(r)

# for one_side_1,other_side_1,boat_1 in all_move_options(one_side,other_side):
#     print(one_side_1)
#     print(boat_1)
#     # print(other_side_1)

'''