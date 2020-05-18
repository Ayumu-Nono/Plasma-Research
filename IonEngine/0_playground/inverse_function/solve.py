Vs = 100
Vv = 100
Ls = 0.5
Lv = Ls

import numpy as np

def f(phi): 
    x = (1-phi/Vs)**(1/2)
    x = x * Ls
    x *= Lv
    return x

y = np.linspace(0,2)
x = f(y)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

x_column = x.reshape(-1, 1)
y_column = y.reshape(-1, 1)

model_poly = make_pipeline(PolynomialFeatures(degree=10), LinearRegression())
model_poly.fit(x_column, y_column)
model_poly.score(x_column, y_column)

y_pred = model_poly.predict(x_column).flatten()
fig = plt.figure()
# fig.scatter(x, np.degrees(y), size=1, legend='真値')
# fig.line(x, np.degrees(y_pred), line_color='orange', legend='推定値')
# fig.xaxis.axis_label = 'f'
# fig.yaxis.axis_l


# plt.plot(y_pred, label="test")
plt.plot(x )
plt.show()