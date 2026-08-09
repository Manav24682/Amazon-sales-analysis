# ======================================================
# Weather Data Analysis Project
# Author : Manav Kumar
# Tools  : Pandas, Matplotlib, Seaborn
# ======================================================


# ======================================================
# STEP 1 : Import Required Libraries
# ======================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# ======================================================
# STEP 2 : Load Dataset
# ======================================================
df=pd.read_csv("Amazon_Sale_Report.csv")

# ======================================================
# STEP 3 : Explore Dataset
# ======================================================

print("sum of null values",df.isnull().sum())
print("sum of duplicated values are",df.duplicated().sum())
print("first 5 rows are",df.head())
print("Last 5 rows are",df.tail())
print("Shape of data is",df.shape)
print("Columns in data",df.columns)
print("Data type of columns",df.dtypes)
print("Statistical summary",df.describe())


#=======================================================
# STEP 4 : Data Cleaning & Preprocessing
# ======================================================

print("After removing duplicate values")
df=df.drop_duplicates()
print(df.shape)
print("Deleting some missing values row:")
df=df.dropna(subset=['ship-city','ship-state','ship-postal-code','ship-country'])
print("Deleting the some columns that have all empty ")
df=df.dropna(axis=1,how="all")
print(df.shape)
print(df.isnull().sum())
df=df.drop(columns=['fulfilled-by'])
print(df.isnull().sum())
df["currency"]=df["currency"].fillna(df["currency"].mode()[0])
df["Amount"]=df["Amount"].fillna(df["Amount"].mean())
df["Date"]=pd.to_datetime(df["Date"],utc='True')
print(df["Date"])

#=======================================================
# STEP 4 : Exploratory Data Analysis(EDA)
# ======================================================

#1.  Find the top 10 states with the highest sales amount
top_states_in_saleAmount=df.groupby("ship-state")["Amount"].sum().sort_values(ascending=False).head(10)
print(top_states_in_saleAmount)

#2.  Find the number of orders in each order status
Status_count = df.groupby("Status")["Order ID"].count().head(5)
print(Status_count) 

#3.  which size is sold the most
Size_quantity=df.groupby("Size")["Qty"].sum().sort_values(ascending=False).head(10)
print(Size_quantity)

#4.  Which courier status  has the highest number of orders
print(df.columns)
top_courier_status=df.groupby("Courier Status")["Order ID"].count()
print(top_courier_status)

#5.  find the top 10 cities with the highest sales amount
top_sale_city=df.groupby("ship-city")["Amount"].sum().sort_values(ascending=False).head(10)
print(top_sale_city)

#6.  Which month generated the highest sales
df["Month"]=df["Date"].dt.month_name()
print(df["Month"])
top_Sale_month=df.groupby("Month")["Amount"].sum().sort_values(ascending=False)
print("Top_sale_months",top_Sale_month)

#7.  Which product category generated the highest sales amount
top_Sale_product=df.groupby("Category")["Amount"].sum().sort_values(ascending=False).head(10)
print("This product category generated the highest sales amount",top_Sale_product)

#8.  Highest sales by sales channel
top_sale_channel=df.groupby("Sales Channel")["Amount"].sum().sort_values(ascending=False)
print("Top sale channel",top_sale_channel)

#9. Find which fulfilment method generated the highest sales
top_sale_fulfilment=df.groupby("Fulfilment")["Amount"].sum().sort_values(ascending=False)
print(top_sale_fulfilment)

#10. Compare B2B vs non-b2b sales
b2b_comparison=df.groupby("B2B")["Amount"].sum().sort_values(ascending=False)
print(b2b_comparison)

#11.  Find the average sales amount for each category 
average_Sale_product=df.groupby("Category")["Amount"].mean().sort_values(ascending=False).head()
print(average_Sale_product)

#12.  Which state has the highest average order value
top_average_order_state=df.groupby("ship-state")["Amount"].mean().sort_values(ascending=False).head(5)
print(top_average_order_state)

#13.  Which category has the highest number of orders
top_category_orders=df.groupby("Category")["Order ID"].count().sort_values(ascending=False)
print(top_category_orders)

#14.  which state has the highest number of orders
top_orders_in_state=df.groupby("ship-state")["Order ID"].count().sort_values(ascending=False).head(10)
print(top_orders_in_state)

#15.  Which city has the highest no of orders
top_orders_in_city=df.groupby("ship-city")["Order ID"].count().sort_values(ascending=False).head(10)
print(top_orders_in_city)

#16.  Which size generate the highest sales amount
top_sales_in_size=df.groupby("Size")["Amount"].sum().sort_values(ascending=False).head(10)
print(top_sales_in_size)

#17.  Which category generated the highest quantity sold
top_category_in_quantity=df.groupby("Category")["Qty"].sum().sort_values(ascending=False).head(10)
print(top_category_in_quantity)

#18.  Which state generated the highest total quantity sold
top_state_in_quantity=df.groupby("ship-state")["Qty"].sum().sort_values(ascending=False).head()
print(top_state_in_quantity)

#19.  which city generated the highest total quantity sold
top_city_in_quantity=df.groupby("ship-city")["Qty"].sum().sort_values(ascending=False).head(10)
print(top_city_in_quantity)

#20.  Find the average quantity sold for each category
average_quantity_for_category=df.groupby("Category")["Qty"].mean()
print(average_quantity_for_category)

#21.  Compare B2B vs NON B2B by no of orders
b2b_comparison_in_orders=df.groupby("B2B")["Order ID"].count()
print(b2b_comparison_in_orders)

#22.  which sales channel recieved the highest no of orders
top_Sales_channel_in_orders=df.groupby("Sales Channel")["Order ID"].count().sort_values(ascending=False)
print(top_Sales_channel_in_orders)

#23.  Which fulfilment method generated the highest sales amount
top_fulfilment_in_sales=df.groupby("Fulfilment")["Amount"].sum().sort_values(ascending=False)
print(top_fulfilment_in_sales)

#24.  Which fulfilment method procesed the highest no of orders
top_fulfilment_in_orders=df.groupby("Fulfilment")["Order ID"].count()
print(top_fulfilment_in_orders)

#25.  Which month has the highest no of orders
top_month_in_orders=df.groupby("Month")["Order ID"].count().head(1)
print(top_month_in_orders)

#26.  Which month sold the highest total quantity
high_qty_sale_month=df.groupby("Month")["Qty"].sum().sort_values(ascending=False)
print(high_qty_sale_month)


# ======================================================
# STEP 7 : Data Visualization 
# ======================================================

#1. # Top 10 states by sales amount
sb.barplot(top_states_in_saleAmount)
plt.tight_layout()
plt.xticks(rotation=13,fontsize=8)
plt.xlabel("Top-10-states",fontsize=10)
plt.title("Top 10 states by sales amount")
plt.ticklabel_format(style="plain",axis="y")
plt.show()

#2. # Top 10 cities by sale amount
sb.barplot(top_sale_city)
plt.tight_layout()
plt.xticks(rotation=18)
plt.title("Top 10 cities by sales amount")
plt.xlabel("Top 10 cities")
plt.ticklabel_format(style="plain",axis="y")
plt.show()

#3. # Sales by product category
sb.barplot(top_Sale_product)
plt.xlabel("Products category")
plt.ylabel("Sales")
plt.title("Sales by product category")
plt.show()

#4. # Quantity sold by category
sb.barplot(top_category_in_quantity)
plt.title("Quantity sold by category")
plt.ylabel("Quantity")
plt.xlabel("Category")
plt.ticklabel_format(style="plain",axis="y")
plt.xticks()
plt.tight_layout()
plt.show()

#5. # Sales by size
sb.barplot(top_sales_in_size)
plt.title("Sales by size")
plt.xlabel("Sizes")
plt.ylabel("Sale")
plt.tight_layout()
plt.ticklabel_format(style="plain",axis="y")
plt.show()

#6. # Orders by order status
sb.barplot(Status_count)
plt.title("Orders by order status")
plt.xlabel("Order status")
plt.ylabel("NO of orders")
plt.xticks(rotation=20,fontsize=10)
plt.tight_layout()
plt.ticklabel_format(style="plain",axis="y")
plt.show()

#7. # Sales by fulfilment
sb.barplot(top_fulfilment_in_sales)
plt.title("Top_fulfilment_in_sales")
plt.xlabel("Top-Fulfilment")
plt.ylabel("No of sales")
plt.show()

#8. # Sales by sales channel
sb.barplot(top_sale_channel)
plt.title("Sales by sales Channel")
plt.xlabel("Top sale channel")
plt.ylabel("Sales")
plt.show()

#9. # Monthly sales trend
sb.lineplot(top_Sale_month,marker="o")
plt.title("Monthly sales trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

#10.  Monthly Quantity sold trend
sb.lineplot(high_qty_sale_month,marker="o")
plt.title("Monthly quantity sold trend")
plt.xlabel("Months")
plt.ylabel("No of quantity")
plt.show()

#11. B2B vs Non B2B Sales
plt.pie(b2b_comparison, autopct="%1.1f%%",labels=b2b_comparison.index)
plt.title("B2B vs Non B2B sales")
plt.ylabel("")
plt.xlabel("")
plt.show()

#12. Box plot of sales amount(detect outliers)
Sales_amount=df["Amount"]
sb.boxplot(Sales_amount)
plt.title("Sales amount")
plt.show()

#13. Histogram of sales amount 
sb.histplot(Sales_amount)
plt.title("Sales amount distribution")
plt.show()

#14. Heatmap(correlation between numeric columns)
corr=df.corr(numeric_only=True)
sb.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation heatmap")
plt.tight_layout()
plt.show()


# ======================================================
# STEP 7 : FINAL DASHBOARD
# ======================================================

fig = plt.figure(figsize=(16, 12))

# Create 4 rows and 4 columns
gs = fig.add_gridspec(
    3, 4,
    height_ratios=[1,  2, 2],
    hspace=0.8,
    wspace=0.35
)

fig.suptitle(
    "Amazon Sales Analysis Dashboard",
    fontsize=20,
    fontweight="bold"
)


# ======================================================
# KPI 1 : TOTAL SALES
# ======================================================

ax1 = fig.add_subplot(gs[0, 0])

Total_sales_amount = df["Amount"].sum()

ax1.text(
    0.5, 0.5,
    f"₹{Total_sales_amount/1e7:.2f} Cr",
    ha="center",
    va="center",
    fontsize=20,
    fontweight="bold"
)

ax1.set_title("Total Sales")
ax1.axis("off")


# ======================================================
# KPI 2 : TOTAL QUANTITY
# ======================================================

ax2 = fig.add_subplot(gs[0, 1])

Total_Quantity = df["Qty"].sum()

ax2.text(
    0.5, 0.5,
    f"{Total_Quantity:,}",
    ha="center",
    va="center",
    fontsize=20,
    fontweight="bold"
)

ax2.set_title("Total Quantity")
ax2.axis("off")


# ======================================================
# KPI 3 : TOTAL ORDERS
# ======================================================

ax3 = fig.add_subplot(gs[0, 2])

Total_orders = df["Order ID"].nunique()

ax3.text(
    0.5, 0.5,
    f"{Total_orders:,}",
    ha="center",
    va="center",
    fontsize=20,
    fontweight="bold"
)

ax3.set_title("Total Orders")
ax3.axis("off")


# ======================================================
# KPI 4 : AVERAGE ORDER VALUE
# ======================================================

ax4 = fig.add_subplot(gs[0, 3])

Average_order_value = Total_sales_amount / Total_orders

ax4.text(
    0.5, 0.5,
    f"₹{Average_order_value:.2f}",
    ha="center",
    va="center",
    fontsize=20,
    fontweight="bold"
)

ax4.set_title("Average Order Value")
ax4.axis("off")


# ======================================================
# 1. MONTHLY SALES TREND
# ======================================================

ax5 = fig.add_subplot(gs[1, 0:2])

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_sales = (
    df.groupby("Month")["Amount"]
    .sum()
    .reindex(month_order)
    .dropna()
)

monthly_sales_cr = monthly_sales / 1e7

sb.lineplot(
    x=monthly_sales_cr.index,
    y=monthly_sales_cr.values,
    marker="o",
    ax=ax5
)

ax5.set_title("Monthly Sales Trend")
ax5.set_xlabel("")
ax5.set_ylabel("Sales (₹ Crore)")
ax5.tick_params(axis="x", rotation=30)


# ======================================================
# 2. SALES BY CATEGORY
# ======================================================

ax6 = fig.add_subplot(gs[1, 2:4])

category_sales = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

category_sales_cr = category_sales / 1e7

sb.barplot(
    x=category_sales_cr.index,
    y=category_sales_cr.values,
    ax=ax6
)

ax6.set_title("Top 5 Categories by Sales")
ax6.set_xlabel("")
ax6.set_ylabel("Sales (₹ Crore)")
ax6.tick_params(axis="x", rotation=30)


# ======================================================
# 3. TOP 10 STATES BY SALES
# ======================================================

ax7 = fig.add_subplot(gs[2, 0:2])

states_sales_cr = top_states_in_saleAmount / 1e7

sb.barplot(
    x=states_sales_cr.index,
    y=states_sales_cr.values,
    ax=ax7
)

ax7.set_title("Top 10 States by Sales")
ax7.set_xlabel("")
ax7.set_ylabel("Sales (₹ Crore)")
ax7.tick_params(axis="x", rotation=35, labelsize=8)


# ======================================================
# 4. TOP 10 CITIES BY SALES
# ======================================================

ax8 = fig.add_subplot(gs[2, 2:4])

cities_sales_cr = top_sale_city / 1e7

sb.barplot(
    x=cities_sales_cr.index,
    y=cities_sales_cr.values,
    ax=ax8
)

ax8.set_title("Top 10 Cities by Sales")
ax8.set_xlabel("")
ax8.set_ylabel("Sales (₹ Crore)")
ax8.tick_params(axis="x", rotation=35, labelsize=8)


# ======================================================
# FINAL DISPLAY
# ======================================================
plt.tight_layout(rect=[0,0,1,0.95])
plt.subplots_adjust(hspace=1.4,bottom=0.15)
plt.show()