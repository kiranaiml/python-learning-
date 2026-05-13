#e commerce profit sniper
product_name=input("Name Of The Product:  ")
quantity_sold=int(input("Quantity sold:  "))
total_revenue=quantity_sold*45.00
platform_fee_total=total_revenue*0.03
total_shipping=quantity_sold*7.50
final_profit=round(total_revenue-platform_fee_total-total_shipping,2)
tracking_id= product_name[0:5].upper()
shipping_lable=product_name[0:3].lower()
shipping_lable1= shipping_lable + str (quantity_sold)


print(f"\n___SALE REPORT:  {tracking_id}___")
print(f" Shipping Lable: {shipping_lable1}")
print(f"Total Revenue:  ${final_profit}") 