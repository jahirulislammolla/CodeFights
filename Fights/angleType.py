def angleType(m):
    if m<90:
        return "acute"
    if m==90:
        return "right"
    if 90<m<180:
        return "obtuse"
    return "straight"
