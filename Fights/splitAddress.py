def splitAddress(address):
    rotocol = ""
    domain = ""
    context = ""
    result = address.split("://")
    protocol = result[0]
    result = result[1].split(".com")
    domain = result[0]
    if len(result) > 1 and result[1]!="":
        context=result[1][1:].split("/")
        return [protocol, domain, *context]
    return [protocol, domain]
