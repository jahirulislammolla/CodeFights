function lateRide(n) {
var k=Math.floor(n/60);
    var h= k.toString();
   
    var length=h.length;
    var sum1=0,sum=0;
if(length==1)
    {
        sum=parseInt(h[0]);
    }
if(length==2)
    {
        sum=parseInt(h[0])+parseInt(h[1]);
    }
    var o=(n%60);
    var m=o.toString();
    var len=m.length;
    if(len==1)
    {
        sum1=parseInt(m[0]);
    }
if(len==2)
    {
        sum1=parseInt(m[0])+parseInt(m[1]);
    }
    return sum+sum1;
}
