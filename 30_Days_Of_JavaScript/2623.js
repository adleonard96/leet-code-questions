/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let memory = new Map();
    return function(...args) {
        if(memory.has(JSON.stringify(args))){
            return memory.get(JSON.stringify(args))
        }
        let ans = fn(...args);
        memory.set(JSON.stringify(args), ans);
        return ans;
    }
}
