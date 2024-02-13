function outerFunction() {
    var count = 0;

    function innerFunction() {
        count++;
        console.log(count);
    }

    return innerFunction;
}

var increment = outerFunction();
increment();
increment();
increment();

(function() {
    var x = 10;
    console.log(x);
})();

function multiplier(x) {
    return function(y) {
        return x * y;
    };
}

var multiplyBy5 = multiplier(5);
console.log(multiplyBy5(3));

function createCounter() {
    var count = 0;

    return function() {
        count++;
        console.log(count);
    };
}

var counter = createCounter();
counter();
counter();
counter();
