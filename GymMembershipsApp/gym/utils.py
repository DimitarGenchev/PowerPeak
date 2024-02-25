def determine_membership_price(duration, membership_type):
    if duration == 1:
        price = membership_type.price_for_one_month
    elif duration == 3:
        price = membership_type.price_for_three_months
    elif duration == 6:
        price = membership_type.price_for_six_months
    elif duration == 12:
        price = membership_type.price_for_twelve_months

    return price
