const messageboxaddr = Module.findExportByName("user32.dll", "MessageBoxA");
console.log("Address of MsgBox: " + messageboxaddr);

Interceptor.attach(messageboxaddr, {
    onEnter: function(args){
        console.log("MsgBox Called");
        console.log("LpText: " + Memory.readUtf8String(args[1]));
        console.log("LpCaption: " + Memory.readUtf8String(args[2]));
    },

    onLeave: function(retval){
        console.log("MsgBox Return");
    },
});
