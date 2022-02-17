from asyncio import exceptions
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
    try: 
        print("reading csv....")
        sale_df = pd.read_csv("Sample_Sales_Data.csv")
        sale_array = [
            SaleData(
                region = sale_df.iloc[row]["Region"],
                country = sale_df.iloc[row]["Country"],
                item_type = sale_df.iloc[row]["Item_Type"],
                sales_channel = sale_df.iloc[row]["Sales_Channel"],
                order_priority = sale_df.iloc[row]["Order_Priority"],
                order_date = datetime.strptime(sale_df.iloc[row]["Order_Date"], '%m/%d/%Y').strftime('%Y-%m-%d'),
                order_id = sale_df.iloc[row]["Order_ID"],
                ship_date = datetime.strptime(sale_df.iloc[row]["Ship_Date"], '%m/%d/%Y').strftime('%Y-%m-%d'),
                units_sold = sale_df.iloc[row]["Units_Sold"],
                unit_price = sale_df.iloc[row]["Unit_Price"],
                unit_cost = sale_df.iloc[row]["Unit_Cost"],
                total_revenue = sale_df.iloc[row]["Total_Revenue"],
                total_cost = sale_df.iloc[row]["Total_Cost"],
                total_profit = sale_df.iloc[row]["Total_Profit"], 
            )
            for row in range(len(sale_df))
        ]
        SaleData.objects.bulk_create(sale_array)
        print("Saved all entries to database")
        return 
    except Exception as e : 
        raise e 
if __name__ == "__main__":
    run()
