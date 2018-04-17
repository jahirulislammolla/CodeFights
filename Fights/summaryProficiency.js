function summaryProficiency(a, n, m) {
result = 0;
        for (i = 0; n > 0; i++) {
            if (a[i] >= m) {
                result += a[i];
                n--;
            }
        }

return result;
}
