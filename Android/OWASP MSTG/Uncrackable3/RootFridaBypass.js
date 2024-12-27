Java.perform(()=>{

	console.log("\n")

	const rootchkpass = Java.use("sg.vantagepoint.util.RootDetection");

	rootchkpass.checkRoot1.implementation = function(){
		console.log("Fun A Bypassed");
		return false;
	}

	rootchkpass.checkRoot2.implementation = function(){
		console.log("Fun B Bypassed");
		return false;
	}

	rootchkpass.checkRoot3.implementation = function(){
		console.log("Fun C Bypassed");
		return false;
	}

    var fgetsPtr = Module.findExportByName("libc.so", "fgets");
    var fgets = new NativeFunction(fgetsPtr, 'pointer', ['pointer', 'int', 'pointer']);

    Interceptor.replace(fgetsPtr, new NativeCallback(function (buffer, size, fp) {        
        var retval = fgets(buffer, size, fp);
        var bufstr = Memory.readUtf8String(buffer);
        if (bufstr.indexOf("frida") > -1) {
            Memory.writeUtf8String(buffer, "ByeByeFrida:\t0");
        }
        return retval;
    }, 'pointer', ['pointer', 'int', 'pointer']));
  
});
