def evaporator(content, evap_per_day, threshold):
    count = 0
    thresholdContent = (threshold/100) * content
    
    while content >= thresholdContent:
        content = content - ((evap_per_day / 100) * content)
        count += 1
    
    return count