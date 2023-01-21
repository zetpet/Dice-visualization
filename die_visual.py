import pygal
from die import Die

#Creating a D6 Die
die = Die()

#Modeling a series of throws with saving the results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analysis of results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualization of results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_titile = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
