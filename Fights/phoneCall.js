function phoneCall(min1, min2_10, min11, s) {
    var fst=s-min1;
    var sum=1;
    if(fst<0)
        {
            return 0;
        }
    var sec=9*min2_10;
    if(sec>=fst)
        {
          var val=Math.floor(fst/min2_10);  
          return sum+val;
        }
    if(sec<fst)
        {
            sum=sum+9;
        }
    var trd=fst-sec;
    var m=Math.floor(trd/min11);
    return sum+m;
}
