# Bokeh library demo
# Author: Pranav Sahasrabudhe
# Email: pranav.sahasrabudhe@gmail.com
# (C)0 2024 - 2025 Pranav Sahasrabudhe

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a ColumnDataSource object
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a figure object
f = figure()

# Add a line renderer to the figure
f.line(x='x', y='y', source=source)

# Save the figure to an HTML file
output_file("line.html")

# Show the figure
show(f)