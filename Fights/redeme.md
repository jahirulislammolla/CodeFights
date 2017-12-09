## Consider an infinite sequence a of decimal digits which is generated using the following algorithm:

<pre>the first 5 digits are initially given;
for i > 4, a[i] = (a[i - 5] + a[i - 4] + a[i - 3] + a[i - 2] + a[i - 1]) % 10, i.e. each element starting with the fifth is the sum of the previous five elements modulo 10.
Given the initial five elements, You need to find the nth element of the sequence (the first element has index 0).

Example

For a = [1, 2, 3, 4, 5] and n = 9, the output should be
sequenceElement(a, n) = 4.

If the sequence starts with digits 1 2 3 4 5 then it continues like this:
1 2 3 4 5 5 9 6 9 4 3 1 3 0 ..., so for n = 9 the answer will be 4.

Input/Output

[time limit] 4000ms (py3)

[input] array.integer a

An array of five integers from 0 to 9 - the first five elements of the sequence.

[input] integer n

Guaranteed constraints:
0 ≤ n < 109.

[output] integer

The value of the nth element.
