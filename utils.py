# Gets the max length of item in response data
def get_max_length(items):
    mx = 0
    for i in items.json():
        for key, val in i.items():
            mx = max(len(str(val)), mx)
    # Cap at 60 
    mx = min(mx, 60)
    return mx