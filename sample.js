function processData(input) {
    var i;
    for (i = 0; i < parseInt(input); i++) {
        console.log("hello world");
    }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});