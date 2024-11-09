const cfileaddr = Module.getExportByName("kernel32.dll", "CreateFileA");
console.log("Create File Address: " + cfileaddr);

Interceptor.attach(cfileaddr, {
	onEnter: function(args){
		console.log("CreateFile Called");
		console.log("LpFileName: " + args[0].readUtf8String());
		console.log("DesiredAccess: " + args[1]);
	},

	onLeave: function(retval){
		console.log("CreateFile Returned");
		console.log("Return Value: " + retval);
	},
});
