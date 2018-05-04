function isSmooth(arr) {
if(arr.length%2==0) {
        return arr[0]==arr[arr.length-1] && arr[0]== (arr[arr.length/2-1]+arr[arr.length/2]);
    }
    else {
        return arr[0]==arr[arr.length-1] && arr[0]== arr[(arr.length-1)/2];
    }
}
