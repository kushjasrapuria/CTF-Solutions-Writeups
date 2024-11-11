# JD-GUI Disassembly

The code in Main Activity calls for a func which includes:
```java
public class CodeCheck {
  private native boolean bar(byte[] paramArrayOfbyte);
  
  public boolean a(String paramString) {
    return bar(paramString.getBytes());
  }
}
```

Indicating the application is working with bytes so we use ghidra for disassembling apk and for further analysis

# Ghidra Disassembly 

```C
undefined4
Java_sg_vantagepoint_uncrackable2_CodeCheck_bar(int *param_1,undefined4 param_2,undefined4 param_3)

{
  char *__s1;
  int iVar1;
  undefined4 uVar2;
  int in_GS_OFFSET;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  undefined2 local_20;
  undefined4 local_1e;
  undefined2 local_1a;
  int local_18;
  
  local_18 = *(int *)(in_GS_OFFSET + 0x14);
  if (DAT_00014008 == '\x01') {
    local_30 = 0x6e616854;
    local_2c = 0x6620736b;
    local_28 = 0x6120726f;
    local_24 = 0x74206c6c;
    local_20 = 0x6568;
    local_1e = 0x73696620;
    local_1a = 0x68;
    __s1 = (char *)(**(code **)(*param_1 + 0x2e0))(param_1,param_3,0);
    iVar1 = (**(code **)(*param_1 + 0x2ac))(param_1,param_3);
    if (iVar1 == 0x17) {
      iVar1 = strncmp(__s1,(char *)&local_30,0x17);
      if (iVar1 == 0) {
        uVar2 = 1;
        goto LAB_00011009;
      }
    }
  }
  uVar2 = 0;
LAB_00011009:
  if (*(int *)(in_GS_OFFSET + 0x14) == local_18) {
    return uVar2;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```

local_30 = 0x6e616854;
local_2c = 0x6620736b;
local_28 = 0x6120726f;
local_24 = 0x74206c6c;
local_20 = 0x6568;
local_1e = 0x73696620;
local_1a = 0x68;

This is the secret string which has to be reversed twice in cyberchef to obtain secret string

The secret is: Thanks for all the fish
