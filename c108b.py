import random
import plotly.express as px
import plotly.figure_factory as ff

count = []
diceresult = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1 + dice2)
    count.append(i)

fig = ff.create_distplot([diceresult],['result'],show_hist=False)

fig.show()