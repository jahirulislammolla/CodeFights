function arrayChange(inputArray) {
    result = 0;
    for(i=1; i< inputArray.length; i++){
        if(inputArray[i]<=inputArray[i-1]){
            result += inputArray[i-1] - inputArray[i] +1;
           inputArray[i] = inputArray[i-1] + 1;
        }
    }
    return result;
}
