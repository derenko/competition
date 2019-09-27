cost = int(input())

notes = [1, 2, 5, 10, 20, 50, 100, 200, 500]

number_of_notes = 0
current_sum = 0

i = len(notes) - 1

while(True):
    if(current_sum == cost):
        break
    else:
        if(current_sum + notes[i] > cost):
            i = i - 1
        else:
            current_sum = current_sum + notes[i]
            i = len(notes) - 1
            number_of_notes = number_of_notes + 1


print(number_of_notes)
