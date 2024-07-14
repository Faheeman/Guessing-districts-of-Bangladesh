import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("Bangladesh Districts Game")
image = "bangla10.gif"
screen.addshape(image)

turtle.shape(image)

# Load the district data
data = pandas.read_csv("cleaned_datas.csv")
all_districts = data.bd_district.to_list()
guessed_districts = []

# Game loop
while len(guessed_districts) < 64:
    answer_districts = screen.textinput(
        title=f"{len(guessed_districts)}/64 Districts Correct",
        prompt="What's another district?"
    ).title()

    if answer_districts == "Exit":
        missing_districts=[]
        for districts in all_districts:
            if districts not in guessed_districts:
                missing_districts.append(districts)
        new_data=pandas.DataFrame(missing_districts)
        new_data.to_csv("districts to learn.csv")

        break
    if answer_districts in all_districts and answer_districts not in guessed_districts:
        guessed_districts.append(answer_districts)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.bd_district == answer_districts]
        x_coord = float(district_data.VALUES1.item())
        y_coord = float(district_data.VALUES2.item())
        t.goto(x_coord, y_coord)
        t.write(district_data.bd_district.item())

screen.exitonclick()
