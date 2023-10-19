""" How to use pandas (simple way)"""
import pandas
import turtle


if __name__ == "__main__":
  
  screen = turtle.Screen()
  screen.title("U.S. States Game")
  image = "part6/blank_states_img.gif"
  screen.addshape(image)
  turtle.shape(image)

  data = pandas.read_csv("part6/50_states.csv")
  all_states = data.state.to_list() # data series in list []
  states_guessed = []

  while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 Guess the State", 
                                  prompt="What's another state's name?").title()
    #if answer_state is one of the states in all the 50_states_.csv
    #if they got it right:
    # write state in map with given coordinates
    if answer_state in all_states:
      states_guessed.append(answer_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = data[data.state == answer_state]
      t.goto(int(state_data.x), int(state_data.y))
      t.write(state_data.state.item())
      

  
  screen.exitonclick()