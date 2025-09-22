nums=[1,2,3,4,5]
squares_of_num = { x:x**2 for x in nums}
print(squares_of_num)

milk_rate_inr={
    'Cow':40,
    'Buffalo':80,
    'Sheep' :150
}

milk_rate_usd = { animal:price/85 for animal,price in milk_rate_inr.items() }

print(milk_rate_usd)