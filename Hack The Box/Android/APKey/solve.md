# Challange Info

Name : APKey

Difficulty : Easy

Category : Mobile

Link : https://app.hackthebox.com/challenges/APKey

# Writeup

The challange includes a APKey.apk file.

Installing the apk.

```bash
adb install APKey.apk
```

It promts for Name and Password so i started with static analysis using a tool called MoboSF.

Tool Link : https://github.com/MobSF/Mobile-Security-Framework-MobSF

I looked for hardcoded secrets.

Reconnaissance > Hardcoded Secrets

It has some data which can be useful.

Data : a2a3d412e92d896134d9c9126d756f

For further analysis i tried analysing activities.

Components > Activities

```java
public class a implements View.OnClickListener {
        public a() {
        }
        @Override // android.view.View.OnClickListener
        public void onClick(View view) {
            Toast makeText;
            String str;
            try {
                if (MainActivity.this.f928c.getText().toString().equals("admin")) {
                    MainActivity mainActivity = MainActivity.this;
                    b bVar = mainActivity.e;
                    String obj = mainActivity.d.getText().toString();
                    try {
                        MessageDigest messageDigest = MessageDigest.getInstance("MD5");
                        messageDigest.update(obj.getBytes());
                        byte[] digest = messageDigest.digest();
                        StringBuffer stringBuffer = new StringBuffer();
                        for (byte b2 : digest) {
                            stringBuffer.append(Integer.toHexString(b2 & 255));
                        }
                        str = stringBuffer.toString();
                    } catch (NoSuchAlgorithmException e) {
                        e.printStackTrace();
                        str = "";
                    }
                    if (str.equals("a2a3d412e92d896134d9c9126d756f")) {
                        Context applicationContext = MainActivity.this.getApplicationContext();
                        MainActivity mainActivity2 = MainActivity.this;
                        b bVar2 = mainActivity2.e;
                        g gVar = mainActivity2.f;
                        makeText = Toast.makeText(applicationContext, b.a(g.a()), 1);
                        makeText.show();
                    }
                }
                makeText = Toast.makeText(MainActivity.this.getApplicationContext(), "Wrong Credentials!", 0);
                makeText.show();
            } catch (Exception e2) {
                e2.printStackTrace();
            }
        }
    }
```

This part caught my eye.

```java
if (MainActivity.this.f928c.getText().toString().equals("admin"))
```

This made it clear that Name is admin.

```java
MessageDigest messageDigest = MessageDigest.getInstance("MD5")
```

It seems that our Password is being compared to MD5 hash.

So we can say that the hardcoded value we found was MD5 hash.

But while trying to crack the hash I realized the hash is only 30 hex digits but MD5 hash are 32 hex digit size.

So as the value is hardcoded I tried changing the hash value to something else which is valid MD5.

```bash
apktool d APKey.apk
```

Finding MainActivity.smali file using find and grep.

```bash
find ./ | grep MainAct
```

> ./APKey/smali/com/example/apkey/MainActivity$a.smali
> ./APKey/smali/com/example/apkey/MainActivity.smali

I use sublime text as my goto editior.

subl ./APKey/smali/com/example/apkey/MainActivity$a.smali

Line 141 

```
const-string v1, "a2a3d412e92d896134d9c9126d756f"
```

Changing it to 5f4dcc3b5aa765d61d8327deb882cf99 which is "password".

```
const-string v1, "5f4dcc3b5aa765d61d8327deb882cf99"
```

Compiling the modified APK with apktool.

```bash
apktool b APKey -o unsig.apk
```

Aligning APK with online zipalign tool (Due to APKtool i am having trouble using zipalign on my kali so i use website for it).

Zipalign Website : https://sisik.eu/zipalign

Generating keystore.

```bash
keytool -genkey -v -keystore ../../RSAKeys/geektech.keystore -alias patch -keyalg RSA -keysize 2048 -validity 100
```

Signing APK with apksigner.

```bash
apksigner sign --ks ../../RSAKeys/geektech.keystore --out final.apk unsig.apk
```

Installing APK (Make sure to uninstall old version from your android device/emulator).

```bash
adb install final.apk
```

Entering Name as admin and Password as password.

A toast appears with the flag.
