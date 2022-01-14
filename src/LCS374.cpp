/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int lo = 1, hi = n;
        if (lo == hi) {
            return 1;
        }
        while (lo < hi && hi - lo > 1) {
            long midlong = (long)lo + (long)hi;
            int mid = (int)(midlong / 2);
            int curr = guess(mid);
            if (curr == 0) {
                return mid;
            } else if (curr == 1) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        if (guess(hi) == 0) {
            return hi;
        } else if (guess(lo) == 0) {
            return lo;
        } else {
            return hi - lo;
        }
    }
};