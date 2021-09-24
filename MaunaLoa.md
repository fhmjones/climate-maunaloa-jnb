---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.12.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"extensions": {"jupyter_dashboards": {"views": {"grid_default": {}, "report_default": {"hidden": false}}, "version": 1}}}

### Approximate linear models for CO2 at Mauna Loa, Hawaii
#### Instructions 
This plot shows measurements of monthly-averaged CO2 concentrations (in ppm), 
from Mauna Loa Observatory, spanning from 1958-2020. 
Two adjustable linear trends are also plotted.

Your task is to adjust the linear trends by changing their slopes and intercepts, so that one straight line, or "linear model", can approximate the *first 5 years* of data and the other straight line approximates the *most recent 5 years* of data. 

Do your two linear models predict the same CO2 concentrations for the year 2030? 
NOTE: the values in ppm predicted by both straight line models are given in the graph's two-line title.

Interactive graph controls appear when your mouse is over the graph. These

***

```{code-cell} ipython3
---
extensions:
  jupyter_dashboards:
    version: 1
    views:
      grid_default: {}
      report_default:
        hidden: false
---
import MaunaLoaWidget
```

+++ {"extensions": {"jupyter_dashboards": {"views": {"grid_default": {}, "report_default": {"hidden": false}}, "version": 1}}}

***

#### Discussion and Questions
Within relatively short time windows (e.g. 5 years), the linear model can represent a 
reasonable fit to the data, but it remains less clear how good the predictive power of 
this model is for longer periods. 

To analyze this further, revisit the linear fit for "early" and "recent" 5 year periods and **answer the following**:
1. Out to which year would you trust the model built for the window 1958 - 1963? In other words, where does this model start to break down?
2. How far out would you trust the model predictions with the model built for 2015 - 2020? Would you trust the model to predict $\mathrm{CO}_2$ for the year 2050?
3. How might you approach building a model to fit all of the data (1958-2020)?
4. Given what the "raw data" look like, what do you think "seasonally adjusted data" means?
5. Use the graph's "Camera" icon to make a PNG file of your graph with all data and linear model fitting determined from the *first* 5 years.
6. Do the same for the case with linear model fitting from the *last* 5 years. Submit both PNG files for assessment.
7. FINALLY - We are just beginning to learn how to use Dashboards in courses. 
Therefore we would be grateful if each student could individually complete the online anonymous feedback form at [https://ubc.ca1.qualtrics.com/jfe/form/SV_0ju4v38gf1Ok0ke](https://ubc.ca1.qualtrics.com/jfe/form/SV_0ju4v38gf1Ok0ke).
It can also be done on your Phone, and should take only 1-2 minutes. Many thanks! 

***

#### Attribution

* Derived from [L. Heagy's presentation](https://ubc-dsci.github.io/jupyterdays/sessions/heagy/widgets-and-dashboards.html) at
UBC's Jupyter Days 2020, which in turn is adapted from the [Intro-Jupyter tutorial from ICESat-2Hackweek](https://github.com/ICESAT-2HackWeek/intro-jupyter). 
* This version code by F. Jones, adapted for J-Notebook by J. Byer.
* Original data are at the [Scripps CO2 program](https://scrippsco2.ucsd.edu/data/atmospheric_co2/primary_mlo_co2_record.html). See the NOAA [Global Monitoring Laboratory](https://www.esrl.noaa.gov/gmd/ccgg/trends/) for additional details.

```{code-cell} ipython3
---
extensions:
  jupyter_dashboards:
    version: 1
    views:
      grid_default: {}
      report_default:
        hidden: true
---

```
