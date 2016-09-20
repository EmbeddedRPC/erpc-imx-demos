 ### The build directory contains the .bin file, for your MCU core.
# Please follow these instructions to make the on-chip Cortex-M4 run your binary from /build directory:

## TFTP Server Install and Setup:

- Install following packages.
```
sudo apt-get install xinetd tftpd tftp
```
- Create /etc/xinetd.d/tftp and put this entry
```
service tftp
{
protocol        = udp
port            = 69
socket_type     = dgram
wait            = yes
user            = nobody
server          = /usr/sbin/in.tftpd
server_args     = /tftpboot
disable         = no
}
```
- Create a folder /tftpboot this should match whatever you gave in server_args. mostly it will be tftpboot
```
sudo mkdir /tftpboot
sudo chmod -R 777 /tftpboot
sudo chown -R nobody /tftpboot
```
- Restart the xinetd service.
 ###### newer systems:
```
sudo service xinetd restart
```
 ###### older systems:
```
sudo /etc/init.d/xinetd restart
```
- Now our tftp server is up and running!
- Move your .bin file to /tftpboot. 

## U-Boot part:

- Open /dev/ttyUSB0 with baud rate of 115200 Baud
- Power up the board, press any key to stop uboot from booting.
- Enter these commands to setup your environment in uboot:
```
setenv bootargs "no_console_suspend clk_ignore_unused uart_from_osc console=${console},${baudrate} root=${mmcroot}"
setenv mmcargs "no_console_suspend clk_ignore_unused uart_from_osc console=${console},${baudrate} root=${mmcroot}"
setenv fdt_file "imx6sx-sdb-m4.dtb"
setenv ipaddr "192.168.0.50"
setenv serverip "192.168.0.100"
setenv loaddemo "tftpboot 0x007f8000 example.bin;bootaux 0x007f8000"
setenv loadocram "tftpboot 0x00901000 example.bin;bootaux 0x00901000"
```
- Set your PC's ethernet interface IP address to 192.168.0.100, mask 255.255.255.0.
- Type ```run loadocram```, the M4 core firmware should be downloaded via tftp and its firmware should boot-up. If you have opened /dev/ttyUSB1 with baudrate of 115200 Baud, then you should see a new printout.
- Type 'boot' in uboot terminal and hit enter. Linux should boot - you will see more printouts appear in the /dev/ttyUSB1.
