/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        valhold: val,
        toBe(val2) {
            if(this.valhold === val2){
                return true;
            } else {
              throw new Error("Not Equal");
            }
        },
        notToBe(val) {
            if(this.valhold !== val){
                return true;
            }  else {
                throw new Error("Equal");
            }
        }
    }
};
