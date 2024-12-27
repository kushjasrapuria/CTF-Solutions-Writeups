# Challange Info

Name : Debugging Interface

Difficulty : Very Easy

Category : Hardware

Link : https://app.hackthebox.com/challenges/Debugging%2520Interface

# Writeup

The challange includes debugging_interface_signal.sal file.

I used file command to gather basic information about the file.

There is a tool named Logic for analysing hardware signals.

Tool Link : https://www.saleae.com/pages/downloads

```bash
logic
```

Load the capture file.

In order to find the bit rate zoom in to the very start of data capture and hover to it. It will show width 31.23 which gives us 31230 bit rate.

Analysers > Async Serial > Bit Rate = 31230 > Save

Set data view to terminal and display format to ASCII which will reveal the flag.
