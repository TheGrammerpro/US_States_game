import turtle as tu
import pandas
from write_on_map import Writer

screen = tu.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(725,491)
screen.addshape(image)
writer = Writer()

tu.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
xcor_list = states_data["x"].to_list()
ycor_list = states_data["y"].to_list()

title = "U.S. States"
user_answer = tu.textinput(title, "Enter the name of a US state:").title()
user_answers = []
loop = 0

game_is_on = True
while game_is_on:
    total_answers = len(user_answers)
    if loop > 0:
        user_answer = tu.textinput(title, "Enter another name of a US state:").title()
    if user_answer in states_list:
        # The following is a sub loop that keeps asking if the user keeps entering an already given state name:
        while user_answer in user_answers:
            user_answer = tu.textinput(f"{total_answers}/50 States Correct",
                                       "You already entered this state, enter another:").title()
        if user_answer not in states_list:
            title = "Invalid answer"
            continue
        user_answers.append(user_answer)
        total_answers = len(user_answers)
        index = states_list.index(user_answer)
        writer.write_state(user_answer, xcor_list[index], ycor_list[index])
        title = f"{total_answers}/50 States Correct"
    # The following condition is a cheat code that writes all state names on the map:
    elif user_answer == "All States":
        for state in range(0, len(states_list)):
            if states_list[state] not in user_answers:
                writer.write_state(states_list[state], xcor_list[state], ycor_list[state])
        break
    # The following condition stops the loop and exports a CSV file of missing state names:
    elif user_answer == "Exit":
        states_not_guessed = [state for state in states_list if state not in user_answers]
        cheat_sheet = pandas.DataFrame(states_not_guessed)
        cheat_sheet.to_csv("States_not_guessed.csv")
        break
    else:
        title = "Invalid answer"
    loop += 1
tu.mainloop()
