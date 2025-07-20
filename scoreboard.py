from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
      def __init__(self):
          super().__init__()
          self.level=1
          self.hideturtle()
          self.penup()
          self.color("white")
          self.goto(-280,240)
          self.write(f"level:{self.level}",align="left",font=FONT)
      def update_score(self):
          self.clear()
          self.write(f"level:{self.level}", align="left", font=FONT)

      def increase_level(self):
          self.level+=1
          self.update_score()
      def gameover(self):
          self.goto(0,0)
          self.write("Game over","center",font=FONT)