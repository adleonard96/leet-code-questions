/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    return {
        initial: init,
        current: init,
        reset() {
            this.current = this.initial;
            return this.current;
        },
        increment() {
            this.current++;
            return this.current;
        },
        decrement() {
            this.current--;
            return this.current;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */