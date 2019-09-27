global students_count

students_count, teams_count = list(map(int, input().split(" ")))

MIN_IN_TEAM = 1
MAX_IN_TEAM = 3


def get_teams():
    teams = []
    current_team = []

    while(True):
        if(len(current_team) == teams_count):
            teams.append(current_team)
            current_team.clear()
            break
        else:
            if(students_count % 3 == 0 and students_count >= MIN_IN_TEAM):
                current_team.append(3)
                students_count = students_count - 3
            elif(students_count % 2 == 0 and students_count >= MIN_IN_TEAM):
                current_team.append(2)
                students_count = students_count - 2
            else:
                current_team.append(1)
                students_count = students_count - 1

    if(len(teams)):
        return teams
    else:
        return "Impossible"


print(get_teams())
