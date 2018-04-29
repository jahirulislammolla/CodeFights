String[] unusualLexOrder(String[] words) {
        String[] sorted = new String[words.length];
        for(int i = 0; i < words.length;i++) {
            sorted[i] = new StringBuilder(words[i]).reverse().toString();
        }
        Arrays.sort(sorted);
        for(int i = 0; i < words.length;i++) {
            words[i] = new StringBuilder(sorted[i]).reverse().toString();
        }
        return words;
}
