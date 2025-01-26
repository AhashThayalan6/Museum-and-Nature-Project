---
title: "Museums and Nature Centers"
output:
  html_document:
    df_print: paged
---

```{r data, message=FALSE}

library(dplyr)
library(ggplot2)
library(stringr)
library(tidyr)
library(plotrix)

```

## Data Exploration

```{r load, message=FALSE}
# Load file as data frame
# Load file as data frame
museums_df <- read.csv("museums.csv")

# Inspect data frame
head(museums_df)

```

```{r inspect, message=FALSE}
# Inspect data frame

```

## Museums by Type

```{r barplot, message=FALSE}
# Create and print bar plot by type

```

```{r barplot_museum, message=FALSE}
# Create and print bar plot by museum vs non-museum

```

```{r barplot_type, message=FALSE}
# Filter data frame to select states


# Create and print bar plot with facets

```

```{r barplot_stack, message=FALSE}
# Create and print stacked bar plot

```

## Museums by Revenue

```{r process, message=FALSE}
# Filter data frame


# Filter for only small museums


# Filter for only large museums

```

```{r histogram, message=FALSE}
# Create and print histogram

```

```{r boxplot, message=FALSE}
# Create and print boxplot

```

```{r mean, message=FALSE}
# Create and print bar plot with means

```

```{r mean_errorbar, message=FALSE}
# Calculate means and standard errors


# Create and print bar plot with means and standard errors


```

