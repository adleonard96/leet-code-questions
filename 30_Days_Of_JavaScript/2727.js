/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    let objeval = JSON.stringify(obj);
    return (objeval === '[]' || objeval === '{}')
};