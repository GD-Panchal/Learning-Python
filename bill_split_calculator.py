print("Bill Split Calculator")
bill_amount = float(input())
tip = float(input())
number_of_peoples = int(input())

tip_amount = (tip/100)*bill_amount

print(f"Total (including tip): Rs{tip_amount + bill_amount}")
print(f"Each person pays: Rs{(tip_amount+bill_amount)/number_of_peoples}")