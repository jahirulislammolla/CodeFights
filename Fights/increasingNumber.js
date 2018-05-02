function increasingNumber(x, n) {
    var res=1;
    while (res<=n)
    {
        while(x%res!=0)
            x+=1;
        res+=1;
    }
    return x;
}
