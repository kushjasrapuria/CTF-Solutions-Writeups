const messageboxaddr = Module.findExportByName("user32.dll", "MessageBoxA");
console.log("Address of MsgBox: " + messageboxaddr);

var welldone = Memory.allocUtf8String("Well Done");
var congrats = Memory.allocUtf8String("Congrats");

Interceptor.attach(messageboxaddr, {
    onEnter: function(args){
        console.log("MsgBox Called");
        console.log("LpText: " + Memory.readUtf8String(args[1]));
        console.log("LpCaption: " + Memory.readUtf8String(args[2]));

        args[1] = welldone;
        args[2] = congrats;
        args[3] = ptr("0x00000040");
    },

    onLeave: function(retval){
        console.log("MsgBox Return");
    },
});
