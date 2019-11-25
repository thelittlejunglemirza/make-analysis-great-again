import plotly.express as px

tips = px.data.tips()

a = tips['total_bill']

print(a)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

fig = px.box(arr, y=0)
fig = px.box(arr, y=0)
fig = px.box(arr, y=0)
fig = px.box(arr, y=0)
fig.show()
