### How to boot this Linux image
# For i.MX6SX SDB:
1. Please run in this folder: 
    # where mmcblk0 is the name of your target sdcard
    dd if=imx6sx_sdb.sdcard of=/dev/mmcblk0 bs=10M && sudo sync
2. Insert it in your i.MX6SX SDB board in slot "SD4 BOOT"
3. Connect micro USB cable to your PC and to "J16 UART TO USB" connector.
4. Open /dev/ttyUSB0 with baud rate of 115200 Baud
5. Power up the board, press any key to stop uboot from booting.
6. Enter these commands to setup your environment in uboot:
setenv bootargs "no_console_suspend clk_ignore_unused uart_from_osc console=${console},${baudrate} root=${mmcroot}"
setenv mmcargs "no_console_suspend clk_ignore_unused uart_from_osc console=${console},${baudrate} root=${mmcroot}"
setenv fdt_file "imx6sx-sdb-m4.dtb"
setenv ipaddr "192.168.0.50"
setenv serverip "192.168.0.100"
setenv loaddemo "tftpboot 0x007f8000 example.bin;bootaux 0x007f8000"
setenv loadocram "tftpboot 0x00901000 example.bin;bootaux 0x00901000"
7. Set your PC's ethernet interface IP address to 192.168.0.100, mask 255.255.255.0.
8. Setup a tftp server in your PC, share the example.bin (firmware for Cortex-M4) via it. (see readme in /MCU/example)
9. Type 'run loadocram', the M4 core firmware should be downloaded via tftp and its firmware should boot-up. If you have opened /dev/ttyUSB1 with baudrate of 115200 Baud, then you should see a new printout.
10. Type 'boot' in uboot terminal and hit enter. Linux should boot - you will see more printouts appear in the /dev/ttyUSB1.
11. When Linux is on, log in using root as user name. Upload somehow to your board or copy to the home directory the file example.py.
12. Use python to run example.py. You should see Linux talking to Cortex-M4 :-)

Optional:
13. If you enter 'lsmod', you should see rpmsg_multiept kernel module, this kernel module exports RPMsg to user space using sysfs and udev...

