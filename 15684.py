
def solution(line_ver, line_hor, setup_perline):
    print(line_ver, line_hor, setup_perline)
    if line_hor == 0:
        return 0

    return -1


line_ver, line_hor, setup_perline = map(int, input().split())
print(solution(line_ver, line_hor, setup_perline))