function fixedPointsPermutation(permutation) {
    return permutation.filter((v, i) => v === i + 1).length
}
