import dash
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
################################################################################
# APP INITIALIZATION
################################################################################
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# this is needed by gunicorn command in procfile
server = app.server

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [7,3,7,4,3,8,4,8,3]
plt.title("Example")
plt.scatter(x = x, y = y)
plt.ylabel("Y")
plt.xlabel("X")
plt.show()
