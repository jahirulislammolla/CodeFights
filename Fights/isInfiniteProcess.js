function isInfiniteProcess(a, b) {
if(0<=a && a<=20 && 0<=b && b<=20){
        if(b>=a && (b-a)%2==0) {
            return false;
        }
        else {
            return true;
        }
    }
}
