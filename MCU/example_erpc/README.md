# The build directory contains the .bin file, for your MCU core.
# Please follow these instructions to setup a tftp server:

## TFTP Server Install and Setup

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
newer systems:
```
sudo service xinetd restart
```
older systems:
```
sudo /etc/init.d/xinetd restart
```
- Now our tftp server is up and running!
- Move your .bin file to /tftpboot. 
