const fs = require("fs");

function gcd(a,b){
    if (a == b){
        return a;
    }
    else if (a<b){
        return gcd(b, a);
    }
    else{
        return gcd(a-b, b);
    }
}

function parseCSV(csvfile){
    let text = fs.readFileSync(csvfile, encoding='utf-8');
    var lines = text.split("\r\n");
    let result = new Array();
    while(typeof lines[0] !== 'undefined'){
        var line = lines.shift();
        if(line !== ''){
            var split = line.split(',');
            result.push(split)
        }
    }

    return result
}

function quicksort(arr){
    function partition(array, left, right){
        var pivot = array[Math.floor((left+right)/2)];
        var i = left;
        var j = right;

        while (i <= j){
            while(array[i] < pivot){
                i = i + 1;
            }
            while (array[j] > pivot){
                j = j - 1;
            }
            if (i <= j){
                var temp = array[i];
                array[i] = array[j];
                array[j] = temp;
                i = i + 1;
                j = j - 1;
            }
        }

        return i;
    }

    function quicksort_recursive(array, left, right){
        var index;
        if(array.length > 1){
            index = partition(array, left, right);

            if (left < index - 1){
                quicksort_recursive(array, left, index -1);
            }
            if (index < right){
                quicksort_recursive(array, index, right);
            }
        }

        return array;
    }

    let left = 0;
    let right = arr.length - 1
    return quicksort_recursive(arr, left, right)
}