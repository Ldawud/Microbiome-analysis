# Microbiome-analysis
## Pipeline
 Main copy of microbiome pipeline and other assorted tools for microbiome analysis. If you're performing microbiome analysis and realize that the pipeline needs something fixed or updated, feel free to fix it and contribute a pull request, or let me (John) know, and I can update it here. Just trying to keep one centralized copy that people can update when need be.

## Volatility
Contains a .py with a function to calculate the volatility for each sample, which can be imported into your analysis code. Volatility is defined as the beta diversity to the previous sample from that individual, and high volatility indicates that an individual's microbiome is changing a lot over the sampling period. See the paper [Volatility as a Concept to Understand the Impact of Stress on the Microbiome](https://www.sciencedirect.com/science/article/pii/S0306453020304704) from the Cryan Lab for an introduction to the relevance of volatility in stress research. (Dr. Lowry is particularly interesting in looking more at volatility)

## Tools
Currently contains a command line tool (written in python) to export a histogram of a QIIME2 alpha diversity vector. Lamya'a and I found this useful for verifying if we can run an ANOVA vs if we would need to use Kruskal-Wallis for stats testing due to ANOVA's assumption of normality.
