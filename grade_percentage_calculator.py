# a tool that lets you calculate your average percentage for your courses
# code adapted from https://realpython.com/pysimplegui-python/

import PySimpleGUI as sg
sg.theme('BrightColors')

# Helper function for computing average
def get_avg_grade(list_of_grades):
    sum = 0
    for i in range(len(list_of_grades)):
        sum += int(list_of_grades[i])

    percentage = sum / len(list_of_grades)
    percentage = str(percentage) + '%'

    return percentage

# First the window layout in 2 columns

grade_input_column = [
    [sg.Text("Please input your grades separated by commas with no spaces:")],
    [sg.In(size=(30, 20), key="-GRADES-"),
    sg.Button(button_text="Calculate Average Grade", enable_events=True, key="-CALCULATE-")
    ]
]

percentage_column = [
    [sg.Text("Your average percentage is:")],
    [sg.Text(size=(30,2), key="-TOUT-")]
    ]

# Final layout
final_layout = [
    [
        sg.Column(grade_input_column),
        sg.VSeperator(),
        sg.Column(percentage_column),
    ]
]

# Create the window
window = sg.Window(
    title="Grade Percentage Calculator", layout=final_layout, margins=(50, 80), font="Calibri 15"
)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-CALCULATE-":
        try:
            grades = values["-GRADES-"]
            grades = grades.split(',')
            average = get_avg_grade(grades)
            window["-TOUT-"].update(average)
        
        except:
            window["-TOUT-"].update("An error occurred. Please check your inputs and try again")

window.close()