def reorderingOfProducts(boundaries, y):
    boundaries.insert(0, -float('inf'))
    l = 0
    r = len(boundaries) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if y>(boundaries[mid]+boundaries[mid+1])//2:
            l = mid
        else:
            r = mid
    return l
