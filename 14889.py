player_count = int(input())
stat_map = [list(map(int, input().split(" "))) for _ in range(player_count)]

team_start = []
team_link = []
mindiff_stat = 100000000

def calculate():
    global player_count, team_start, team_link, stat_map
    
    team_count = player_count // 2
    stat_start = 0
    stat_link = 0
    for i in range(team_count):
        for j in range(team_count):
            # 나 자신일 경우 제외
            if i==j:
                continue
            stat_start += stat_map[team_start[i]][team_start[j]]
            stat_link += stat_map[team_link[i]][team_link[j]]
    return abs(stat_start - stat_link)

def simulation(no_player):
    global player_count, team_start, team_link, mindiff_stat
    
    # 팀 결정 시 스코어 계산
    if no_player >= player_count:
        now_stat = calculate()
        if mindiff_stat > now_stat:
            mindiff_stat = now_stat
        return
    
    
    if len(team_start) < player_count // 2:
        team_start.append(no_player)
        simulation(no_player+1)
        team_start.pop()
    if len(team_link) < player_count // 2:
        team_link.append(no_player)
        simulation(no_player+1)
        team_link.pop()
    
simulation(0)

print(mindiff_stat)
    