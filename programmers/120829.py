def solution(angle):
    return (2 if angle > 90 else 0) + (2 if angle % 90 == 0 else 1) 