const str = "Be good, Harika B"
var string1 = "harika is learning javascript"
var letter = 'i'

function countBs(str1) {
    count = 0;
    for(let i = 0; i < str.length; i++) {
        if(str[i] === "B") {
            count++;
        }

    }
    console.log(count)
    // return count
    }
    

countBs(str)    

function countChar(string,letter) {
    count = 0;
    letter = 'h'
    for(let i = 0; i<string.length;i++) {
        if(string[i] === letter) {
            count++;
        }
    }
    console.log(count)
    
}
countChar(string1,letter)


