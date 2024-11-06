Java.perform(() => {

	const classa = Java.use("sg.vantagepoint.uncrackable1.a")

	classa.a.overload("java.lang.String").implementation = function(s){
		console.log("\n")
		console.log(s.toString());
		return true;
	}
});
