import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"SaleReport.settings")
import sys
import django
django.setup()
import pandas as pd
from SaleReportApp.models import SaleData
from datetime import datetime


sys.path.append("/home/pralipta/SaleApp")


def run():
    print("reading csv....")
    sale_df = pd.read_csv("Sample_Sales_Data.csv")
    sale_array = sale_df.to_dict(orient="records")
    for entry in sale_array:
        sale_data = SaleData(
            Region = entry["Region"],
            Country = entry["Country"],
            Item_Type = entry["Item_Type"],
            Sales_Channel = entry["Sales_Channel"],
            Order_Priority = entry["Order_Priority"],
            Order_Date = datetime.strptime(entry["Order_Date"], '%m/%d/%Y').strftime('%Y-%m-%d'),
            Order_ID = entry["Order_ID"],
            Ship_Date = datetime.strptime(entry["Ship_Date"], '%m/%d/%Y').strftime('%Y-%m-%d'),
            Units_Sold = entry["Units_Sold"],
            Unit_Price = entry["Unit_Price"],
            Unit_Cost = entry["Unit_Cost"],
            Total_Revenue = entry["Total_Revenue"],
            Total_Cost = entry["Total_Cost"],
            Total_Profit = entry["Total_Profit"],
        )
        sale_data.save()
    print("Saved all entries to database")
    return 

if __name__ == "__main__":
    run()
