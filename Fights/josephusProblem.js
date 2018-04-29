function josephusProblem(n, k) {
        removed = [];
        currentPerson = 0;

        for (i = 1; i < n; i++) {
            skipped = 0;
            while (skipped < k - 1) {
                if (!removed[currentPerson]) {
                    skipped++;
                }
                currentPerson = (currentPerson + 1) % n;
            }
            while (removed[currentPerson]) {
                currentPerson = (currentPerson + 1) % n;
            }
            removed[currentPerson] = true;
        }

        for (i = 0; i < n; i++) {
            if (!removed[i]) {
                return i + 1;
            }
        }

}
