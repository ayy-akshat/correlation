import numpy as np
import csv
import pandas as pd
import plotly.express as px

with open("sample_data/coffee.csv") as file:
    data = csv.DictReader(file)
    x = []
    y = []
    for i in data:
        x.append(float(i['Sleep']))
        y.append(float(i['Coffee']))

    c = np.corrcoef(x, y)
    print("Correlation between sleep and coffee taken: " + str(c[0, 1]))

    df = pd.read_csv("sample_data/coffee.csv")
    d = px.scatter(df, x="Sleep", y="Coffee", title="graph", color="Week", size="Coffee")
    d.show()

with open("sample_data/marks.csv") as file:
    data = csv.DictReader(file)
    x = []
    y = []
    for i in data:
        x.append(float(i['Days Present']))
        y.append(float(i['Marks']))

    c = np.corrcoef(x, y)
    print("Correlation between days present and marks: " + str(c[0, 1]))

    df = pd.read_csv("sample_data/marks.csv")
    d = px.scatter(df, x="Days Present", y="Marks", title="graph", color="Roll No", size="Marks")
    d.show()
