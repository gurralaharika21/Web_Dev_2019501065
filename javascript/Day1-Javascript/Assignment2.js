function deepEqual(str1,str2) {
    if (str1 === str2) {
        return true
    }
    else if (typeof(str1) === 'object' && str1 !== null && typeof(str2) === 'object' && str2 !==null) {
        keys = Object.keys(str1).concat(Object.keys(str2))
        // console.log(keys)
        for (prop of keys) {
            if (typeof str1[prop] === 'object' && typeof str2[prop] === 'object') {
                if (deepEqual(str1[prop],str2[prop]) === false) {
                    return false
                }
            }    
            else if (str1[prop] !== str2[prop]) {
                    return false;
            }
        }
        return true;
    }
    else {
        return false

     }

}


obj1 = {fn:"harika",ls:"reddy",number:101}
obj2 = {fn:"sri",number:123}


str11 = "harika"
str21 = 901
str31="nice"
const o = {
    firstname : "harika",
    lastname:"reddy",
    number:7032144899
}

const o2 = {
    firstname : "harika",
    lastname:"reddy",
    number:7032144899
}
const o3 = {
    firstname : "harika",
    lastname:"gurrala",
    
}



console.log(deepEqual(o,o2))
console.log(deepEqual(obj1,obj2))
console.log(deepEqual(str11,str21))
console.log(deepEqual(str11,str31))
console.log(deepEqual(str11,str11))
console.log(deepEqual(o,o3))

