from ipywidgets import interact, GridspecLayout, Layout
import ipywidgets as widgets
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from plotly.offline import iplot

# Fetch and prep the data
# read in the data from the prepared CSV file.
co2_data_source = "./data/monthly_in_situ_co2_mlo.csv"
co2_data_full = pd.read_csv(
    co2_data_source, skiprows=np.arange(0, 56), na_values="-99.99"
)

co2_data_full.columns = [
    "year", "month", "date_int", "date", "raw_co2", "seasonally_adjusted",
    "fit", "seasonally_adjusted_fit", "co2 filled", "seasonally_adjusted_filled"
]

# for handling NaN's see https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
co2_data = co2_data_full.dropna()


# A linear model with slope and intercept to predict CO2
def predict_co2(slope, intercept, initial_date, prediction_date):
    a = slope * (prediction_date - initial_date) + intercept
    return a


# Setting up the widgets
# slope1_slider = widgets.FloatSlider(value = 2, min=0, max=3, step=0.05)
# slope2_slider = widgets.FloatSlider(value = 1.65, min=0, max=3, step=0.05)
# intercept1_slider = widgets.FloatSlider(value=312, min=250, max=320, step=0.25)
# intercept2_slider = widgets.FloatSlider(value=312, min=250, max=320, step=0.25)
slope1_slider = widgets.FloatSlider(value=1.4, min=0.5, max=2.0, step=0.05)
slope2_slider = widgets.FloatSlider(value=2.4, min=2.0, max=3.0, step=0.01)
intercept1_slider = widgets.FloatSlider(value=300, min=290, max=340, step=0.25)
intercept2_slider = widgets.FloatSlider(value=290, min=220, max=300, step=0.25)
signal_type_radiobuttons = widgets.RadioButtons(value='Seasonally adjusted data',
                                                options=['Seasonally adjusted data', 'Raw data'])
years_radiobuttons = widgets.RadioButtons(value='All data', options=['first 5 years', 'last 5 years', 'All data'])
slope1_label = widgets.Label("Slope (for first 5 years):")
slope2_label = widgets.Label("Slope (for last 5 years):")
intercept1_label = widgets.Label("Intercept (for first 5 years):")
intercept2_label = widgets.Label("Intercept (for last 5 years):")
signal_type_label = widgets.Label("Signal type:")


def update_graph(line_slope_1st, line_intcpt_1st, line_slope_last, line_intcpt_last, Data_type, zone):
    with plot.batch_update():
        l1 = line_slope_1st * (co2_data.date - np.min(co2_data.date)) + line_intcpt_1st
        l2 = line_slope_last * (co2_data.date - np.min(co2_data.date)) + line_intcpt_last

        if Data_type == 'Raw data':
            plot.data[0].x = co2_data.date
            plot.data[0].y = co2_data.raw_co2
        if Data_type == 'Seasonally adjusted data':
            plot.data[0].x = co2_data.date
            plot.data[0].y = co2_data.seasonally_adjusted

        plot.data[1].x = co2_data.date
        plot.data[1].y = l1

        plot.data[2].x = co2_data.date
        plot.data[2].y = l2

        if zone == 'first 5 years':
            plot.update_xaxes(range=[1958, 1963])
            plot.update_yaxes(range=[312, 322])

        if zone == 'last 5 years':
            plot.update_xaxes(range=[2015, 2020])
            plot.update_yaxes(range=[395, 415])

        if zone == 'All data':
            plot.update_xaxes(range=[1955, 2023])
            plot.update_yaxes(range=[310, 440])

        predicted_co2_first = predict_co2(line_slope_1st, line_intcpt_1st, 1958, 2023)
        predicted_co2_last = predict_co2(line_slope_last, line_intcpt_last, 1958, 2023)
        plot.layout.title = f"""Predicted CO2 for {2030} (based on linear fit for <b>first</b> 5 years): {predicted_co2_first:1.2f} ppm.<br>
    Predicted CO2 for {2030} (based on linear fit for <b>last</b> 5 years): {predicted_co2_last:1.2f} ppm."""


def initialize_graph(line_slope_1st, line_intcpt_1st, line_slope_last, line_intcpt_last, Data_type, zone):
    plot.data = []
    l1 = line_slope_1st * (co2_data.date - np.min(co2_data.date)) + line_intcpt_1st
    l2 = line_slope_last * (co2_data.date - np.min(co2_data.date)) + line_intcpt_last

    if Data_type == 'Raw data':
        plot.add_trace(go.Scatter(x=co2_data.date, y=co2_data.raw_co2, mode='markers',
                                  line=dict(color='MediumTurquoise'), name="CO2"))
    if Data_type == 'Seasonally adjusted data':
        plot.add_trace(go.Scatter(x=co2_data.date, y=co2_data.seasonally_adjusted, mode='markers',
                                  line=dict(color='MediumTurquoise'), name="CO2"))

    plot.add_trace(go.Scatter(x=co2_data.date, y=l1, mode='lines',
                              line=dict(color='SandyBrown'), name="linear fit (for first 5 years)"))

    plot.add_trace(go.Scatter(x=co2_data.date, y=l2, mode='lines',
                              line=dict(color='MediumVioletRed'), name="linear fit (for last 5 years)"))

    plot.update_layout(xaxis_title='Year', yaxis_title='ppm')
    #    plot.update_xaxes(range=[start, end])

    if zone == 'first 5 years':
        plot.update_xaxes(range=[1958, 1963])
        plot.update_yaxes(range=[312, 322])

    if zone == 'last 5 years':
        plot.update_xaxes(range=[2015, 2020])
        plot.update_yaxes(range=[395, 415])

    if zone == 'All data':
        plot.update_xaxes(range=[1955, 2023])
        plot.update_yaxes(range=[310, 440])

    predicted_co2_first = predict_co2(line_slope_1st, line_intcpt_1st, 1958, 2023)
    predicted_co2_last = predict_co2(line_slope_last, line_intcpt_last, 1958, 2023)
    plot.layout.title = f"""Predicted CO2 for {2030} (based on linear fit for <b>first</b> 5 years): {predicted_co2_first:1.2f} ppm.<br>
Predicted CO2 for {2030} (based on linear fit for <b>last</b> 5 years): {predicted_co2_last:1.2f} ppm."""


# change the visibility of a given list of widgets to the given display type ("flex" for visible or "none" for invisible)
def update_visibility(widget_array, display):
    for w in widget_array:
        w.layout.display = display


def update_widgets(value):
    if value == 'first 5 years':
        update_visibility([slope1_slider, intercept1_slider, slope1_label, intercept1_label], 'flex')
        update_visibility([slope2_slider, intercept2_slider, slope2_label, intercept2_label], 'none')
    elif value == 'last 5 years':
        update_visibility([slope1_slider, intercept1_slider, slope1_label, intercept1_label], 'none')
        update_visibility([slope2_slider, intercept2_slider, slope2_label, intercept2_label], 'flex')
    elif value == 'All data':
        update_visibility([slope1_slider, slope2_slider, intercept1_slider, intercept2_slider,
                           slope1_label, slope2_label, intercept1_label, intercept2_label], 'flex')


# functions, linked to the widgets, to update the plot when a widget is changed
def slope1_eventhandler(change):
    update_graph(change.new, intercept1_slider.value, slope2_slider.value, intercept2_slider.value,
                 signal_type_radiobuttons.value, years_radiobuttons.value)


def slope2_eventhandler(change):
    update_graph(slope1_slider.value, intercept1_slider.value, change.new, intercept2_slider.value,
                 signal_type_radiobuttons.value, years_radiobuttons.value)


def intercept1_eventhandler(change):
    update_graph(slope1_slider.value, change.new, slope2_slider.value, intercept2_slider.value,
                 signal_type_radiobuttons.value, years_radiobuttons.value)


def intercept2_eventhandler(change):
    update_graph(slope1_slider.value, intercept1_slider.value, slope2_slider.value, change.new,
                 signal_type_radiobuttons.value, years_radiobuttons.value)


def signal_type_eventhandler(change):
    update_graph(slope1_slider.value, intercept1_slider.value, slope2_slider.value, intercept2_slider.value, change.new,
                 years_radiobuttons.value)


def years_eventhandler(change):
    update_widgets(change.new)
    update_graph(slope1_slider.value, intercept1_slider.value, slope2_slider.value, intercept2_slider.value,
                 signal_type_radiobuttons.value, change.new)


# link the widgets to the appropriate event handler functions above
slope1_slider.observe(slope1_eventhandler, 'value')
slope2_slider.observe(slope2_eventhandler, 'value')
intercept1_slider.observe(intercept1_eventhandler, 'value')
intercept2_slider.observe(intercept2_eventhandler, 'value')
signal_type_radiobuttons.observe(signal_type_eventhandler, 'value')
years_radiobuttons.observe(years_eventhandler, 'value')

# Initialize plot
plot = go.FigureWidget()
scattf = plot.add_scatter()
scatt = scattf.data[-1]

initialize_graph(slope1_slider.value, intercept1_slider.value, slope2_slider.value, intercept2_slider.value,
                 signal_type_radiobuttons.value, years_radiobuttons.value)
update_widgets(years_radiobuttons.value)

# Formatting widgets
# This is essentially a table with two rows. The first row has two columns of widgets (sliders, labels, radiobuttons),
# and the second row has the graph.
vbox1 = widgets.VBox([slope1_label,
                      slope1_slider,
                      slope2_label,
                      slope2_slider,
                      signal_type_label,
                      signal_type_radiobuttons
                      ])

vbox2 = widgets.VBox([intercept1_label,
                      intercept1_slider,
                      intercept2_label,
                      intercept2_slider,
                      widgets.Label(""),
                      years_radiobuttons
                      ])

hbox = widgets.HBox([vbox1, vbox2])

display(widgets.VBox([hbox, plot]))