---
title: "Museums and Nature Centers"
output:
  html_document:
    df_print: paged
---

```{r setup, message=FALSE}
library(dplyr)
library(ggplot2)
library(stringr)
library(tidyr)
library(plotrix)

# Load file as data frame
museums_df <- read.csv("museums.csv")
# Inspect data frame
head(museums_df)
# Add scale_x_discrete() with wrap_format
museum_type <- museum_type +
  scale_x_discrete(labels = scales::wrap_format(8))
print(museum_type)
# Create and print bar plot by museum vs non-museum
museum_class <- ggplot(museums_df, aes(x = Is.Museum)) +
  geom_bar() +
  scale_x_discrete(labels = c("TRUE" = "Museum", "FALSE" = "Non-Museum")) +
  labs(title = "Museums vs Non-Museums", x = "Type", y = "Count")
print(museum_class)

# Filter data frame to select specific states
museums_states <- museums_df %>%
  filter(State..Administrative.Location. %in% c("IL", "CA", "NY"))

# Create and print bar plot with facets
museum_facet <- ggplot(museums_states, aes(x = Is.Museum)) +
  geom_bar() +
  facet_grid(~State..Administrative.Location.) +
  scale_x_discrete(labels = c("TRUE" = "Museum", "FALSE" = "Non-Museum")) +
  labs(title = "Museum Distribution by State", x = "Type", y = "Count")
print(museum_facet)
# Filter data frame for unique parent organizations with revenue > 0
museums_revenue_df <- museums_df %>%
  distinct(Legal.Name, .keep_all = TRUE) %>%
  filter(Annual.Revenue > 0)

# Filter for small museums
museums_small_df <- museums_revenue_df %>%
  filter(Annual.Revenue < 1e6)

# Filter for large museums
museums_large_df <- museums_revenue_df %>%
  filter(Annual.Revenue > 1e9)
