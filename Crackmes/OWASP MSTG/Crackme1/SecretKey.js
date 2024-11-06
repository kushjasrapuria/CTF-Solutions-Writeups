Java.perform(()=>{

	console.log("\n");

	console.log("Base64 Decode");
	const base64 = Java.use("android.util.Base64");
	var arrayOfByte = base64.decode("5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc=", 0);

	console.log("Func B");
	const classa = Java.use("sg.vantagepoint.uncrackable1.a");
	var enckey = classa.b("8d127684cbc37c17616d806cf50473cc");

	console.log("Func A");
	const decrypter = Java.use("sg.vantagepoint.a.a");
	var encsecret = decrypter.a(enckey, arrayOfByte);

	console.log("String Decryption")
	const strcls = Java.use("java.lang.String");
	var secret = strcls.$new(encsecret);

	console.log("Secret : " + secret);

});
