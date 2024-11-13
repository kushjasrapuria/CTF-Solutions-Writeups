Interceptor.attach(Module.findBaseAddress('libfoo.so').add(0x12c0), {
  onEnter: function(args) {
    console.log("Secret generator on enter, address of secret: " + args[0]);
    this.answerLocation = args[0];
    console.log(hexdump(this.answerLocation, {
      offset: 0,
      length: 0x20,
      header: true,
      ansi: true
    }));
  },
  onLeave: function(retval) {
    console.log("Secret generator on leave");
    console.log(hexdump(this.answerLocation, {
      offset: 0,
      length: 0x20,
      header: true,
      ansi: true
    }));
  }
});
