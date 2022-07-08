# Bayesian automatic weighting of graders

A number of projects have each been graded by a number of judges. Not all projects were graded by all judges. In general each judge provides
grades for a subset of projects and each project has a small number of judges. 

We are interested in correcting for any bias displayed by particular judges. That is, we want to estimate a model where each grade provided by a judge is 
a random variable centered at a value that is the true value of the project plus a bias by the judge.

All calculations are currently in Jupyter notebooks. This was done for a specific class, so you can see the process on the real grades.

- [Talks 2022](https://nbviewer.org/github/opherdonchin/Grades-for-projects-anonymized/blob/e0b9dcbb75d7eecf17993e9f22f0e7cee98310a2/Regression_analysis_talks_2022.ipynb)
- [Posters 2022](https://nbviewer.org/github/opherdonchin/Grades-for-projects-anonymized/blob/e0b9dcbb75d7eecf17993e9f22f0e7cee98310a2/Regression_analysis_posters_2022.ipynb)

The frist generates two csv files and the second generates and .xlsx showing the final results
