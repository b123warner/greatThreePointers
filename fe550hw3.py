# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:23:14 2017

@author: bwarner
"""
##Determining the greatest shooter in NBA history

import pandas as pd
from bokeh.models.sources import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.plotting import figure,output_file, show
#from bokeh.io import output_file, show
from bokeh.models.widgets import Panel,Tabs
from bokeh.models.formatters import NumeralTickFormatter



df = pd.read_csv('3pointData.csv')
df2 = df.sort_values(by = '3ppercent')
names = list(df2['name'])
threePointPercent = list(df2['3ppercent'])
source = ColumnDataSource(df2)




p1 = figure(title = "Who is the greatest shooter in NBA History",x_axis_label = 'Games Played',y_axis_label = '3 Pointers Made',tools = 'box_select')

#tooltips=[
 #   ('Player', '@name'),
  #  ('3 point %', '@3ppercent'),
#]

#p2 = Scatter(df, x='3pa', y='3perGame', title="HP vs MPG",
 #           xlabel="Miles Per Gallon", ylabel="Horsepower",
  #          tooltips=tooltips)

# Add circle glyphs to the figure p
p1.circle('gms','3pm',source = source,size =15)


# Create a HoverTool object: hover
hover = HoverTool(tooltips = [('Player','@name')])

# Add the HoverTool object to figure p
p1.add_tools(hover)


####EXAMPLEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE######
#output_notebook()
#p = figure()
#p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
#show(p)


p2 = figure(title = "Who is the greatest shooter in NBA History",x_axis_label = '3 point attempts per game',y_axis_label = '3 pointers made per game',tools = 'box_select')

p2.circle('3pa','3perGame', source = source, color = 'firebrick',size = 15, alpha = .8)

hover = HoverTool(tooltips = [('Player','@name')])
p2.add_tools(hover)

p3 = figure(title = "Greatest 3 point shooting %",x_axis_label = 'Name',y_axis_label = '3 pointer %',y_range = [0,.6], x_range = names)
p3.rect(x =[1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],y = [val/2.0 for val in threePointPercent], width = 0.4,height = threePointPercent, color = "#CAB2D6")
p3.xaxis.major_label_orientation = "vertical"
p3.yaxis[0].formatter = NumeralTickFormatter(format='0%')
hover = HoverTool(tooltips = [('Player','values')])

p3.add_tools(hover)

#p3 = Bar(df2,label=CatAttr(columns=['name'], sort=True),values = '3ppercent', title = "Greatest 3 point percentage", color = 'firebrick', bar_width = 0.4)

tab1 = Panel(child = p1, title = "3 pointers vs games playesxd")
tab2 = Panel(child = p2, title = "3 pointers attempted per game vs made per game")
tab3 = Panel(child = p3, title = "3 point % bar chart")
layout = Tabs(tabs = [tab1,tab2,tab3])

output_file('numpy.html')
show(layout)