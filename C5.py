def star_to_delta(ra, rb, rc):
    # Calculate the numerator factor to avoid redundancy
    numerator = (ra * rb) + (rb * rc) + (rc * ra)
    
    # Calculate the three Delta resistors
    r_ab = numerator / rc
    r_bc = numerator / ra
    r_ca = numerator / rb
    
    # Return rounded values to two decimal places
    return round(r_ab, 2), round(r_bc, 2), round(r_ca, 2)

print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))
