# Welcome to i.MX6/7 eRPC and RPMsg how-to and demo repository!

This repository serves as a demonstration how can one setup a simple multicore communication between Linux user space application written in Python (feel free to use anything else!) and a Cortex-M4 coprocessor using RPMsg library. It further shows, how
to use RPMsg as a transport layer for embedded remote procedure call (eRPC) library.

- Run 
  *MCU/example_rpmsg/build/armgcc/imx6sx_sdb_m4/build_all.sh*  
  **or**  
  *MCU/example_erpc/build/armgcc/imx6sx_sdb_m4/build_all.sh*  
  to build the **Cortex-M4** firmware.
- You can either use pre-built image for sdcard located in Linux/deploy or build the **Yocto Linux** by running:  
*MPU/setup_yocto/clone_setup_yocto.sh*
- When you manage to boot into **Linux**, use the *MPU/example_rpmsg/example.py* (or respectively *MPU/example_erpc/example.py*) Python script to talk to the **Cortex-M4** coprocessor.

- This repository demonstrates multiple components developped by NXP Semiconductors:
     - **RPMsg Lite** - an optimized implementation of RPMsg protocol for MCUs
     - **RPMsg Multiendpoint** (rpmsg_multiept.ko) - kernel module exporting RPMsg interface to Linux user-space, in form of a patch
     - **RPMsg Python** - Python wrapper for rpmsg_multiept.ko
     - **eRPC** - Embedded RPC library

