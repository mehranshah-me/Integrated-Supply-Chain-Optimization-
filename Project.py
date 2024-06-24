# -*- coding: utf-8 -*-

!pip install pulp
!pip install plotly

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_image(image_path, width, height):
    try:

        img = mpimg.imread(image_path)
        plt.figure(figsize=(width, height))
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    except Exception as e:
        print("An error occurred:", e)

image_path = "/download1.png"

width = 10
height = 8

image_path = "/download1.png"

show_image(image_path, width, height)

image_path = "/download2.png"

show_image(image_path, width, height)

import folium

# Sample array of places (latitude, longitude, place name)
places = [
    (12.739603017267669, 77.78666550917728, "Hosur Main Plant"),
    (13.06486, 80.26754, "Chennai"),
    (11.6489, 78.1591, "Salem"),
    (9.8784, 78.1149, "Madurai"),
    (11.3323, 77.7037, "Erode"),
    (10.8606, 78.7121, "Trichy"),
    (8.7555, 77.6883, "Tirunelveli"),
    (11.925, 79.4836, "Villupuram"),
    (10.998, 76.99, "Coimbatore")
]

# Creates a map centered at a specific location
mymap = folium.Map(location=[places[0][0], places[0][1]], zoom_start=7)

# Adding markers for each place
for place in places:
    if place[2] == "Hosur Main Plant":
        folium.Marker(location=[place[0], place[1]], popup=place[2], icon=folium.Icon(color='red')).add_to(mymap)
    else:
        folium.Marker(location=[place[0], place[1]], popup=place[2]).add_to(mymap)

# Displaying the map
mymap

import pulp
from pulp import *

# Defining the problem as a minimization problem
prob = LpProblem("Distribution_and_Transportation_Optimization", LpMinimize)

# Definig parameters
parts = ['part1', 'part2', 'part3', 'part4', 'part5']
distribution_centers = range(1)

weeks = ['week1', 'week2', 'week3', 'week4']
companies = ['comp1', 'comp2', 'comp3', 'comp4', 'comp5']

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_image(image_path, title, figsize=(8, 8)):
    try:
        img = mpimg.imread(image_path)
        plt.figure(figsize=figsize)
        plt.imshow(img)
        plt.axis('off')
        plt.title(title, fontsize=16)
        plt.show()
    except Exception as e:
        print("An error occurred:", e)
image_path = "/download3.png"
title = "Demand data of distribution centre 1"
show_image(image_path, title, figsize=(10, 10))

demand = {}
cost_price = {}
prod_price={}
inventory_holding_cost1={}
inventory_holding_cost={}
# Defining parameters
demand[('center_0', 'part1', 'week1')] = 16
demand[('center_0', 'part1', 'week2')] = 16
demand[('center_0', 'part1', 'week3')] = 15
demand[('center_0', 'part1', 'week4')] = 15

demand[('center_0', 'part2', 'week1')] = 249
demand[('center_0', 'part2', 'week2')] = 263
demand[('center_0', 'part2', 'week3')] = 248
demand[('center_0', 'part2', 'week4')] = 300

demand[('center_0', 'part3', 'week1')] = 226
demand[('center_0', 'part3', 'week2')] = 246
demand[('center_0', 'part3', 'week3')] = 226
demand[('center_0', 'part3', 'week4')] = 290

demand[('center_0', 'part4', 'week1')] = 376
demand[('center_0', 'part4', 'week2')] = 418
demand[('center_0', 'part4', 'week3')] = 350
demand[('center_0', 'part4', 'week4')] = 459

demand[('center_0', 'part5', 'week1')] = 28
demand[('center_0', 'part5', 'week2')] = 28
demand[('center_0', 'part5', 'week3')] = 23
demand[('center_0', 'part5', 'week4')] = 25

inventory_capacity ={'part1':967,'part2':725,'part3':258,'part4':645,'part5':226 }
inventory_capacity2={'part1':3600,'part2':2700,'part3':1800,'part4':2400,'part5':840 }



inventory_min ={'part1':120,'part2':100,'part3':50,'part4':90,'part5':200 }
inventory_min2 ={'part1':0,'part2':0,'part3':0,'part4':0,'part5':0 }




inventory_holding_cost1[('part1')] =91
inventory_holding_cost1[('part2')] =84
inventory_holding_cost1[( 'part3')] =6
inventory_holding_cost1[('part4')] =41
inventory_holding_cost1[('part5')] = 7

inventory_holding_cost[('part1')] =86
inventory_holding_cost[('part2')] =80
inventory_holding_cost[( 'part3')] =4
inventory_holding_cost[('part4')] =38
inventory_holding_cost[('part5')] = 6

transport_capacity = {'comp1': 2, 'comp2': 5, 'comp3': 4, 'comp4': 3, 'comp5': 3}
truck_capacity = 7000
production_capacity = {'part1': 4934, 'part2': 4934, 'part3': 1149, 'part4': 6990, 'part5': 11983}

image_path = "/download4.png"
title = "Transport"
show_image(image_path, title, figsize=(10, 10))

cost_price[('part1','comp1')] = 19.67
cost_price[('part1','comp2')] = 17.18
cost_price[('part1','comp3')] = 19.13
cost_price[('part1','comp4')] = 9.89
cost_price[('part1','comp5')] = 38.6

cost_price[('part2','comp1')] = 18.2
cost_price[('part2','comp2')] = 15.89
cost_price[('part2','comp3')] = 17.7
cost_price[('part2','comp4')] = 9.15
cost_price[('part2','comp5')] = 35.73

cost_price[('part3','comp1')] = 2.19
cost_price[('part3','comp2')] = 1.91
cost_price[('part3','comp3')] = 2.13
cost_price[('part3','comp4')] = 1.1
cost_price[('part3','comp5')] = 4.31

cost_price[('part4','comp1')] = 7.1
cost_price[('part4','comp2')] = 6.2
cost_price[('part4','comp3')] = 6.9
cost_price[('part4','comp4')] = 3.57
cost_price[('part4','comp5')] = 13.94

cost_price[('part5','comp1')] = 2.06
cost_price[('part5','comp2')] = 1.8
cost_price[('part5','comp3')] = 2.01
cost_price[('part5','comp4')] = 1.04
cost_price[('part5','comp5')] = 4.05

prod_price[('part1')] = 1.295
prod_price[('part2')] = 1.295
prod_price[('part3')] = 1.39
prod_price[('part4')] = 0.229
prod_price[('part5')] = 0.133

weight_per_unit = {}

weight_per_unit['part1'] = 2.575
weight_per_unit['part2']= 2.382
weight_per_unit['part3']= 0.287
weight_per_unit['part4']= 0.929
weight_per_unit['part5']= 0.51

# Defining decision variables
transport_vars = LpVariable.dicts("Transport", [(i, j, k, t, w) for i in distribution_centers
                                                  for j in ['plant']
                                                  for k in parts
                                                  for t in companies
                                                  for w in weeks], lowBound=0, cat='Integer')

# Defining the number of parts stored in each distribution center for each part type and each week
inventory_dist = pulp.LpVariable.dicts("Inventory", ((i, j, k) for i in distribution_centers for j in parts for k in weeks), lowBound=0, cat='integer')

inventory_dist2 = pulp.LpVariable.dicts("Inventory", (('plant', j, k)  for j in parts for k in weeks), lowBound=0, cat='integer')

prod_plant = LpVariable.dicts("production", [(i, j, w)
                                                  for i in ['plant']
                                                  for j in parts

                                                  for w in weeks], lowBound=0, cat='Integer')

# Defining objective function

prob += lpSum(transport_vars[(i, 'plant', k, t, w)] * (cost_price[(k, t)] )+(inventory_dist[(i, k, w)] * (inventory_holding_cost1[k])\
                                                                             +prod_plant['plant',k,w]*prod_price[(k)]\
                                                                             +(inventory_dist2[('plant', k, w)] * (inventory_holding_cost[k])))\
               for i in distribution_centers
                                                                 for k in parts
                                                                 for t in companies
                                                                 for w in weeks)

# Defining demand constraints
for i in distribution_centers:
    for k in range(len(parts)):
        for w in range(len(weeks)):
            prob += lpSum(transport_vars[(i, 'plant', parts[k], t,weeks[w])] for t in companies) >= demand[('center_'+str(i), parts[k],weeks[w])]

initial_inventory = {
    'part1': 0,
    'part2': 0,
    'part3': 0,
    'part4': 0,
    'part5': 0,
}
for i in distribution_centers:
    for j in range(len(parts)):
        for w in range(len(weeks)):

            if w == 0:

                prob += inventory_dist[(i, parts[j], weeks[w])] == initial_inventory[( parts[j])]
            else:

                prob += inventory_dist[(i, parts[j], weeks[w])] == \
                        inventory_dist[(i, parts[j], weeks[w - 1])] \
                        - demand[('center_' + str(i), parts[j], weeks[w])] \
                        + lpSum(transport_vars[(i, 'plant', parts[j], t, weeks[w])] for t in companies)

            prob += inventory_dist[(i, parts[j], weeks[w])] >= 0

for i in distribution_centers:
    for j in range(len(parts)):
      for w in range(len(weeks)):

          if w == 0:

              prob += inventory_dist2[('plant', parts[j], weeks[w])] == initial_inventory[( parts[j])]
          else:

              prob += inventory_dist2[('plant', parts[j], weeks[w])] == \
                      inventory_dist2[('plant', parts[j], weeks[w - 1])] \
                      + prod_plant[('plant' , parts[j], weeks[w])] \
                      - lpSum(transport_vars[(i, 'plant', parts[j], t, weeks[w])] for t in companies)

          prob += inventory_dist2[('plant', parts[j], weeks[w])] >= 0

for i in distribution_centers:
    for j in range(len(parts)):
      for w in range(len(weeks)):
        prob+=lpSum(transport_vars[(i, 'plant', parts[j], t, weeks[w])] for t in companies)==prod_plant[('plant' , parts[j], weeks[w])]

for k in parts:
    prob += lpSum(inventory_dist[(i, k, w)] for i in distribution_centers

                                                      for w in weeks) <= inventory_capacity[k]
for k in parts:
    prob += lpSum(inventory_dist2[('plant', k, w)]

                                                      for w in weeks) <= inventory_capacity2[k]



for k in parts:
      prob += lpSum(inventory_dist[(i, k, w)] for i in distribution_centers
                                               for w in weeks
                                                        ) >= inventory_min[k]
for k in parts:
      prob += lpSum(inventory_dist2[('plant', k, w)] for i in distribution_centers
                                               for w in weeks
                                                        ) >= inventory_min2[k]

# Defining transportation capacity constraints
for t in companies:
    prob += lpSum(transport_vars[(i, 'plant', k, t, w)] * weight_per_unit[k] for i in distribution_centers
                                                                               for k in parts
                                                                               for w in weeks) <= transport_capacity[t] * truck_capacity

# Defining production capacity constraints
for k in parts:
    prob += lpSum(transport_vars[(i, 'plant', k, t, w)] for i in distribution_centers
                                                        for t in companies
                                                        for w in weeks) <= production_capacity[k]

# Solving the problem
prob.solve()

# Printing the optimal solution
print("Total cost:", value(prob.objective))
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)

print(f"Status:{LpStatus[prob.status]}\n")

for name,  c in prob.constraints.items():
   print(f"{name}:slack ={c.slack:.2f}, shadow price ={c.pi:.2f}")

#curves for  decsion variables and optimal solution

import plotly.graph_objects as go


x = []
y = []
for v in prob.variables():
    if v.varValue > 0:
        x.append(v.name)
        y.append(v.varValue)

# Creating the plot
fig = go.Figure(data=go.Scatter(x=x, y=y))

# Update the plot layout
fig.update_layout(
    title="Optimal Solution",
    xaxis_title="Decision Variables",
    yaxis_title="Optimal Value",
)


fig.show()

# Creating the plot
fig = go.Figure()

# Adding the slack variable curve
slack_x = []
slack_y = []
for name, c in prob.constraints.items():
    slack_x.append(name)
    slack_y.append(c.slack)
fig.add_trace(go.Scatter(x=slack_x, y=slack_y, name="Slack Variable"))

# Updating the plot layout
fig.update_layout(
    title="Slack Values",
    xaxis_title="Variables",
    yaxis_title="Value",
)

fig.show()

shadow_x = []
shadow_y = []
for name, c in prob.constraints.items():
    shadow_x.append(name)
    shadow_y.append(c.pi)
fig = go.Figure(data=go.Scatter(x=shadow_x, y=shadow_y, name="Shadow Price"))

# Updating the plot layout
fig.update_layout(
    title="Shadow Price Values",
    xaxis_title="Variables",
    yaxis_title="Value",
)

fig.show()

x = []
y = []
for v in prob.variables():
    if v.varValue > 0:
        x.append(v.name)
        y.append(v.varValue)

shadow_price_x = []
shadow_price_y = []
for name, c in prob.constraints.items():
    shadow_price_x.append(name)
    shadow_price_y.append(c.pi)

# Creating the figure
fig = go.Figure()

# Adding traces
fig.add_trace(go.Scatter(x=x, y=y, name="Optimal Solution"))
fig.add_trace(go.Scatter(x=shadow_price_x, y=shadow_price_y, name="Shadow Price"))

# Updating layout
fig.update_layout(
    title="Correlation between Shadow Price and Optimal Solution",
    xaxis_title="Variables",
    yaxis_title="Value",
)


fig.show()

