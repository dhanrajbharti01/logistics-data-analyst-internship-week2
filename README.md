# Logistics Data Analyst Internship - Week 2

## Week 2 - Logistics Data Cleaning and Preprocessing

This project focuses on data quality assessment, cleaning, outlier detection, and data standardization using Python and Pandas on a logistics delivery dataset.

## Dataset

The dataset contains 60 logistics delivery records and 8 attributes:

- Order ID
- Distance (km)
- Parcel Count
- Traffic Level
- Hour
- Vehicle Capacity
- Planned Delivery Time (min)
- Actual Delivery Time (min)

## Data Quality Assessment

The dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Statistical characteristics
- Outliers using the IQR method

### Results

- Total Records: 60
- Total Columns: 8
- Missing Values: 0
- Duplicate Rows: 0
- Detected Outliers: 0

## Data Cleaning

The following preprocessing techniques were implemented:

- Missing value handling using median imputation for numerical columns
- Removal of leading and trailing spaces from text columns
- Duplicate record validation
- Data type inspection
- Outlier detection using the Interquartile Range (IQR) method

## Data Standardization

Numerical features were standardized using `StandardScaler` from Scikit-learn.

The standardized dataset was saved as:

`logistics_orders_standardized.csv`

## Technologies Used

- Python
- Pandas
- Scikit-learn
- CSV
- Jupyter/VS Code

## Project Files

- `week2_data_cleaning.py` - Python preprocessing script
- `logistics_orders.csv` - Original dataset
- `logistics_orders_cleaned.csv` - Cleaned dataset
- `logistics_orders_standardized.csv` - Standardized dataset
- `Week_2_Logistics_Data_Cleaning_and_Preprocessing_Report.docx` - Detailed report

## Conclusion

The logistics dataset was successfully inspected, cleaned, validated, and standardized. The preprocessing workflow provides a reliable dataset for further logistics analytics and decision-making activities.
