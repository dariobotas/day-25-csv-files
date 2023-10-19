""" How to use pandas (simple way)"""
import pandas
import turtle


if __name__ == "__main__":
  screen = turtle.Screen()
  screen.title("U.S. States Game")
  image = "part5/blank_states_img.gif"
  screen.addshape(image)
  
  turtle.shape(image)

  #Get coordinates on screen turtle to get states coordinates
  #def get_mouse_click_coor(x,y):
  #  print(x, y)

  #turtle.onscreenclick(get_mouse_click_coor)
  
  #turtle.mainloop()

  answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

  screen.exitonclick()