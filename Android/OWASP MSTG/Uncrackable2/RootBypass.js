Java.perform(()=>{

	console.log("\n")

	const rootchkpass = Java.use("sg.vantagepoint.a.b");

	rootchkpass.a.implementation = function(){
		console.log("Fun A Bypassed");
		return false;
	}

	rootchkpass.b.implementation = function(){
		console.log("Fun B Bypassed");
		return false;
	}

	rootchkpass.c.implementation = function(){
		console.log("Fun C Bypassed");
		return false;
	}
  
});
