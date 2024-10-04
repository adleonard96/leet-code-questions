/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let val = n - 1;

    return function() {
        val++;
        return val;
    };
};
