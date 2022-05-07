def amount_of_pages(su):
    n=1
    r=0
    while r<su:
        r+=len(str(n))
        n+=1
    return n-1


print(amount_of_pages(660))
