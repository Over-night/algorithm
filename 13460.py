import sys

sys.setrecursionlimit(1000000)  

# 공 위치 표현 클래스
class ball:
    def __init__(self, ver=0, hor=0, ball=None):
        if ball == None:
            self.ver = ver
            self.hor = hor
        else:
            self.ver = ball.ver
            self.hor = ball.hor
    def set(self, ver=0, hor=0, ball=None):
        if ball == None:
            self.ver = ver
            self.hor = hor
        else:
            self.ver = ball.ver
            self.hor = ball.hor


# 맵 크기 입력
verticalSize, horizontalSize = map(int, input().split())
# 맵 입력
board = [list(map(str, sys.stdin.readline().split())) for _ in range(verticalSize)]

red = None
blue = None
hole = None

# 맵 문자열 리스트 -> 문자 리스트 변환
for ver in range(verticalSize):
    board[ver] = list(board[ver][0])
    # 공 위치 파악
    for hor in range(horizontalSize):
        if board[ver][hor] == 'R':
            red = ball(ver=ver, hor=hor)
        if board[ver][hor] == 'B':
            blue = ball(ver=ver, hor=hor)

minStep = 11
# D R U L
# R D R U R D L U
moveDirection = [[1,0], [0,1], [-1,0], [0,-1]]

def swap(ball, verMoveTo, horMoveTo):
    tmp = board[ball.ver][ball.hor]
    board[ball.ver][ball.hor] = board[verMoveTo][horMoveTo]
    board[verMoveTo][horMoveTo] = tmp
    
def move(ball, dir):
    verMoveTo = ball.ver + dir[0]
    horMoveTo = ball.hor + dir[1]
            
    if board[verMoveTo][horMoveTo] != '.':
        if board[verMoveTo][horMoveTo] == 'O':
            return 'O'
        return "X"
    else:
        swap(ball, verMoveTo, horMoveTo)
        ball.set(ver=verMoveTo, hor=horMoveTo)
        return "."

def simulation(step, beforeAct):
    global red, blue, minStep, board

    # 최적 횟수 이상을 탐색할 경우 반환
    if step >= minStep:
        return
    
    # 공 위치 기억
    redSaveLoc = ball(ball=red)
    blueSaveLoc = ball(ball=blue)
    
    for i in range(len(moveDirection)):
        # 이전과 같은 동작이거나 반복(위-아래 / 좌-우) 동작 시 건너뛰기
        if beforeAct is not None and beforeAct % 2 == i % 2:
            continue
        
        # 위치 불러오기
        board[red.ver][red.hor] = '.'
        board[blue.ver][blue.hor] = '.'
        red.set(ball=redSaveLoc)
        blue.set(ball=blueSaveLoc)
        board[red.ver][red.hor] = 'R'
        board[blue.ver][blue.hor] = 'B'
        
        redCanMove = True
        blueCanMove = True
        redFinish = False
        blueFinish = False
        # 이동 시뮬레이션
        while redCanMove or blueCanMove:
            # 공 이동
            redResult = move(red, moveDirection[i])
            blueResult = move(blue, moveDirection[i])
            
            # 빨강공 골인 시
            if redResult == 'O':
                redFinish = True
                break
            # 파랑공 골인 시
            if blueResult == 'O':
                blueFinish = True
                break
            
            # 둘중에 하나라도 움직였을 경우 재귀 계속 
            redCanMove = True if redResult == '.' else False
            blueCanMove = True if blueResult == '.' else False
        
        # 파란공이 들어갈 경우 제외
        if blueFinish:
            continue
        # 빨간공이 들어갈 경우
        elif redFinish:
            # 파란공이 함께 들어갈 경우 제외
            moveRange = 1
            while board[blue.ver + moveDirection[i][0] * moveRange][blue.hor + moveDirection[i][1] * moveRange] != "#":
                if board[blue.ver + moveDirection[i][0] * moveRange][blue.hor + moveDirection[i][1] * moveRange] == 'O':
                    blueFinish = True
                    break
                moveRange += 1
            if blueFinish:
                continue
            
            # 재귀 종료
            if step < minStep:
                minStep = step
            break
        
        # 위치 변화가 없을 경우 제외 
        if not (red.ver == redSaveLoc.ver and red.hor == redSaveLoc.hor and \
            blue.ver == blueSaveLoc.ver and blue.hor == blueSaveLoc.hor):
            simulation(step+1, i)


simulation(1, None)
        
print(minStep if minStep<11 else -1)