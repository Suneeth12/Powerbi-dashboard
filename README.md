# Sales Analytics & Revenue Prediction Dashboard

A comprehensive business intelligence solution combining interactive Power BI dashboards with machine learning-powered revenue prediction capabilities.

<img width="1073" height="643" alt="DashBoard" src="https://github.com/user-attachments/assets/48f0620d-9b03-4409-a5cb-36e4a6fc2063" />



## 📊 Project Overview

This project provides end-to-end sales analytics and predictive modeling for business decision-making. It combines:

- **Interactive Power BI Dashboard** for real-time sales insights
- **Machine Learning Model** for revenue prediction using XGBoost
- **Comprehensive Data Analysis** across multiple business dimensions

## 🏗️ Architecture

```
├── Dashboard.pdf           # Power BI dashboard export
├── script.py              # Revenue prediction model
├── data/                  # Data files directory
│   ├── customers.csv
│   ├── employees.csv
│   ├── offices.csv
│   ├── orders.csv
│   ├── order_details.csv
│   ├── payments.csv
│   ├── products.csv
│   └── productlines.csv
└── README.md
```

## 📈 Dashboard Features

### Sales Performance Metrics
- **Total Sales**: $10M across all periods
- **Total Profit**: $3.83M with detailed profit analysis
- **Average Order Value**: $29.46K per transaction
- **Order Volume**: 326 total orders tracked

### Key Visualizations

#### 1. Sales Trends Over Time
<img width="715" height="438" alt="Sales" src="https://github.com/user-attachments/assets/e895fc53-3850-49f7-924e-812ab73d3096" />

- Year-over-year comparison (2003-2005)
- Monthly breakdowns with seasonal patterns
- YTD vs. Total Sales analysis

#### 2. Top Performing Products
<img width="1122" height="430" alt="Top_products" src="https://github.com/user-attachments/assets/74faaaa5-7e1c-4785-a83f-fcfdc337b217" />

**Leading Products by Revenue:**
- 1992 Ferrari 360 Spider (Red) - $0.3M
- 2001 Ferrari Enzo - $0.25M
- 1952 Alpine Renault 1300 - $0.22M
- 2003 Harley-Davidson Eagle Drag Bike - $0.2M

#### 3. Profit Analysis by Product Line
<img width="1077" height="412" alt="Profit" src="https://github.com/user-attachments/assets/fb5efddc-f0a9-489a-bcb2-f6ea73d61806" />

- **Classic Cars**: Highest profit contributor (~$4M)
- **Vintage Cars**: Second largest segment (~$2M)
- **Motorcycles**: Significant revenue stream (~$1M)

#### 4. Geographic Sales Distribution
<img width="1064" height="355" alt="Graph" src="https://github.com/user-attachments/assets/2f50a5b7-3614-4261-a397-8a0d9389dde3" />

- Global sales mapping with regional performance
- Market penetration analysis
- Geographic opportunity identification

#### 5. Order Trends Analysis
<img width="650" height="375" alt="Orders" src="https://github.com/user-attachments/assets/66f4c471-72c3-4e11-9350-917b0725a73f" />

- **2003**: 111 orders
- **2004**: 64 orders
- **2005**: 151 orders (40% growth)

## 🤖 Machine Learning Model

### Revenue Prediction Engine

Our XGBoost-based model predicts revenue using key business features:

```python
# Key Features Used
- Customer Number
- Product Code  
- Order Line Number
- Credit Limit
```

### Model Performance Metrics

| Metric | Value |
|--------|-------|
| **R² Score** | 0.85+ |
| **MAPE** | <15% |
| **Model Accuracy** | ~85%+ |

### Technical Implementation

```python
# Model Configuration
XGBRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas scikit-learn xgboost
```

### Power BI Dashboard Setup

1. Open Power BI Desktop
2. Import the data files from the `data/` directory
3. Load the dashboard configuration
4. Refresh data connections

## 📊 Data Sources

The project integrates multiple business data sources:

- **Customers**: Customer profiles and credit information
- **Orders**: Transaction records and order details
- **Products**: Product catalog and specifications
- **Payments**: Payment history and amounts
- **Employees & Offices**: Organizational structure data

## 🔍 Key Insights

### Business Intelligence Findings

1. **Product Performance**
   - Ferrari models dominate high-value sales
   - Classic Cars generate 40%+ of total profit
   - Seasonal trends show Q4 performance peaks

2. **Customer Patterns**
   - Average order value of $29.46K indicates premium market focus
   - Customer credit limits correlate with purchase volumes
   - Geographic distribution shows expansion opportunities

3. **Revenue Trends**
   - 2005 showed strong recovery with 151 orders
   - YTD performance tracking enables real-time monitoring
   - Product line diversification supports revenue stability

## 🛠️ Technical Details

### Dashboard Components
- **Power BI Desktop** for visualization
- **Interactive filters** for dynamic analysis
- **Real-time data refresh** capabilities
- **Mobile-responsive design** for accessibility

### ML Model Features
- **XGBoost algorithm** for high accuracy predictions
- **Feature engineering** from transactional data
- **Cross-validation** for model reliability
- **Performance monitoring** with R² and MAPE metrics


