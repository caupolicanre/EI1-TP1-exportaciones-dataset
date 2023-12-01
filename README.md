# Exporta Simple Analysis - Practical Work "Espacio Integrador 1"

This repository contains the code and documentation for an analysis performed in the context of the subject "Espacio Integrador 1" of the University Degree in Data Processing and Data Exploitation (Faculty of Engineering - U.N.E.R).  
The work aims to process and analyze data related to exports using the Exporta Simple platform, covering various aspects like shipment costs, frequency of usage, operation amounts, shipping times, and common origin-destination regions.

## Objective

The main objectives of this project are:

- Analyze the provided dataset and its context.
- Use Python for data processing and analysis.
- Implement various thresholds and transformations to better understand the data.
- Generate visualizations and reports for clear communication of results.

## Tools and Technologies

### Python Script
- Utilizes the following libraries:
  - `csv` for reading and writing CSV files.
  - `matplotlib.pyplot` for data visualization.
  - `operator` for specific operations.
  
- Processes the dataset to:
  - Transform the operation amount.
  - Categorize shipping times.
  - Normalize shipping time data.
  - Create a new categorical variable for operation amounts and shipping times.
  - Generate statistics and percentages based on the processed data.

### Excel and Text Files
- The project includes Excel files for initial data analysis and cleaning.
- A text file is generated with a report summarizing the key findings from the data processing.

## Execution

1. **Data Cleaning in Excel**: The initial steps involved modifying encoding, reordering columns, and handling missing or erroneous data.
2. **Python Script**: The main processing is done using a Python script:
    - **Data Processing**: The script categorizes operation amounts and shipping times, normalizes time data, and categorizes destination countries.
    - **File Creation**: New CSV files with processed data and a report text file are generated.
3. **Documentation**: The project includes a report explaining the steps taken and the results obtained during data processing.

## Conclusion

The work demonstrates the application of Python for data processing and analysis. It involved cleaning and processing a dataset related to export operations using the Exporta Simple platform. The generated reports and visualizations help in better understanding the trends and characteristics of the export data.

For detailed information, refer to the [Python script](https://github.com/caupolicanre/EI1-TP1-exportaciones-dataset/blob/main/app/dataset_processing.py), generated [graphs](https://github.com/caupolicanre/EI1-TP1-exportaciones-dataset/tree/main/graphs) and the accompanying [report](https://github.com/caupolicanre/EI1-TP1-exportaciones-dataset/blob/main/results/Exportaciones_report.txt) in the repository.
