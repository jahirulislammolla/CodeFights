def pagesNumbering(n):
    tens=1
    i=1
    res=0
    while tens*10<=n:
        res+=9*tens*i
        i+=1
        tens*=10
    return res+(n-tens+1)*i
    
    function pagesNumbering(n) {
    let pageDivision = 9;
    let total = 0;
    let digits = 1;
    
    while(n >= pageDivision) {
        n -= pageDivision;
        total += pageDivision * digits
        pageDivision *= 10;
        digits++;
    }
    
    total += n * digits;
    
    return total;
}
