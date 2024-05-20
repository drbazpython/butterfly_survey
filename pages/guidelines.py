import dash
from dash import html, dcc

dash.register_page(__name__,path='/Guidelines',name="Survey Guidelines")
layout = [
html.Br(),
dcc.Markdown('''
**When**

Conducted on the farm once a week from 1st April to 29th September

**Where**

There are 3 [transect routes](http://127.0.0.1:5500/Map) across the farm – please pick one.

You are welcome to do more if you like but they are quite long.

**Weather conditions**

Ideally between 10.45am & 3.45pm

Temperatures 13-17°C with at least 60% sunshine or 17°C if no sunshine.

Windspeed no more than 5 on Beaufort Scale (0 - no wind, 6 - very strong wind)

No rain

**Method**

Make a note of the temperature & % sunshine level at the beginning of the survey.

Walk the transect at a slow, steady pace counting all butterflies seen within a fixed distance - 2.5m either side of the transect line and 5m ahead.

Record butterfly species and numbers on the recording form.

In some habitats e.g. woodland rides, it is acceptable to record at a width of 5m along one side only of the transect line.

Always follow the transect route each time.

Do not stop walking and wait at favoured hotspots to improve your count, as this will bias results.

At the end of the transect record the time, the average temperature & sunshine level
                      '''),
]
# layout = html.Div([
#     html.H1('Butterfly Survey Information'),
#     html.Div(dcc.Markdown 'When
# Butterfly surveys at Bere Marsh Farm
# Conducted on the farm once a week from 1st April to 29th September
# Where
# There are 3 transect routes across the farm – please pick one You are welcome to do more if you like but they are quite long.
# Weather conditions
# Ideally between 10.45am & 3.45pm
# Temperatures 13-17°C with at least 60% sunshine or 17°C if no sunshine. Windspeed no more than 5 on Beaufort Scale (0 - no wind, 6 - very strong wind) No rain
# Method
# Make a note of the temperature & % sunshine level at the beginning of the survey
# Walk the transect at a slow, steady pace counting all butterflies seen within a fixed distance - 2.5m either side of the transect line and 5m ahead
# Record butterfly species and numbers on the recording form
# In some habitats e.g. woodland rides, it is acceptable to record at a width of 5m along one side only of the transect line
# Always follow the transect route each time
# Do not stop walking and wait at favoured hotspots to improve your count, as this will bias results.
# At the end of the transect record the time, the average temperature & sunshine level'),
# ])
