""" How to use pandas (simple way)"""
import pandas
import turtle

def print_state_on_map(state, x, y):
  new_turtle = turtle.Turtle()
  new_turtle.shape("circle")
  new_turtle.shapesize(0.2,0.2)
  new_turtle.penup()
  new_turtle.color("black")
  new_turtle.goto(x, y)
  new_turtle.write(state, align="center", font=("Courier", 11, "normal"))
  
  

if __name__ == "__main__":
  
  screen = turtle.Screen()
  screen.title("U.S. States Game")
  image = "part6/blank_states_img.gif"
  screen.addshape(image)
  
  turtle.shape(image)
  states_guessed = 0
  game_is_on = True
  
  states_data = pandas.read_csv("part6/50_states.csv")
  #print(states_data)
  states = states_data.state
  states_list = states.to_list()
  states_lower = list(map(str.lower,states_list))
  #print()
  #if "Alabama" in states_list:
  #  print("yes")
#  print(states.to_list())
  
  while game_is_on:
    answer_state = screen.textinput(title=f"{states_guessed}/50 Guess the State", 
                                  prompt="What's another state's name?")
    lower_answer = answer_state.lower()
    
    if lower_answer in states_lower:
      state_df = states_data[states_data.state.apply(lambda x: x.lower() if isinstance(x, str) else x) == lower_answer]
      state = state_df.state.to_string(index=False)
      x = int(state_df.x)
      y = int(state_df.y)
      print_state_on_map(state, x, y)
      states_guessed += 1
      states_lower.remove(lower_answer)

    if states_guessed == 50:
      game_is_on = False
      print_state_on_map("Finish, you win!", 0, 0)

    if lower_answer == "cancel" or lower_answer == "quit":
      game_is_on = False
      print_state_on_map("Loser! Go study!", 0, 0)

  
  screen.exitonclick()