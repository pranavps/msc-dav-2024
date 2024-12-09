# # Install the dplyr package 
# install.packages("dplyr")
# install.packages("ggplot2") # For ggplot2
# Load necessary libraries
library(dplyr)
library(ggplot2)

# Load the dataset
auto_data <- read.csv("C:\\Users\\prana\\msc-dav\\data\\Automobile_data.csv")

# Basic summary statistics
summary(auto_data)

# Calculate variance for a specific column (e.g., engine size)
variance_engine_size <- var(auto_data$engine.size, na.rm = TRUE)

# Visualize the distribution of a specific column (e.g., price)
ggplot(auto_data, aes(x = price)) +
  geom_histogram(binwidth = 1000, fill = "blue", color = "black") +
  labs(title = "Distribution of Automobile Prices",
       x = "Price",
       y = "Count")

# Print variance
print(variance_engine_size)
