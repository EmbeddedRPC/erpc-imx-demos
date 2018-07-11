INCLUDE(CMakeForceCompiler)

# CROSS COMPILER SETTING
SET(CMAKE_SYSTEM_NAME Generic)
CMAKE_MINIMUM_REQUIRED (VERSION 2.6)

# THE VERSION NUMBER
SET (Tutorial_VERSION_MAJOR 1)
SET (Tutorial_VERSION_MINOR 0)

# ENABLE ASM
ENABLE_LANGUAGE(ASM)

SET(CMAKE_STATIC_LIBRARY_PREFIX)
SET(CMAKE_STATIC_LIBRARY_SUFFIX)

SET(CMAKE_EXECUTABLE_LIBRARY_PREFIX)
SET(CMAKE_EXECUTABLE_LIBRARY_SUFFIX)

 
# CURRENT DIRECTORY
SET(ProjDirPath ${CMAKE_CURRENT_SOURCE_DIR})

# DEBUG LINK FILE
set(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -T${ProjDirPath}/MCIMX7D_M4_ocram.ld  -static")

# RELEASE LINK FILE
set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -T${ProjDirPath}/MCIMX7D_M4_ocram.ld  -static")

# DEBUG ASM FLAGS
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG} -g  -mcpu=cortex-m4  -mfloat-abi=hard  -mfpu=fpv4-sp-d16  -mthumb  -Wall  -fno-common  -ffunction-sections  -fdata-sections  -ffreestanding  -fno-builtin  -mapcs  -std=gnu99")

# DEBUG C FLAGS
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -g  -O0  -fno-strict-aliasing  -mcpu=cortex-m4  -mfloat-abi=hard  -mfpu=fpv4-sp-d16  -mthumb  -MMD  -MP  -Wall  -fno-common  -ffunction-sections  -fdata-sections  -ffreestanding  -fno-builtin  -mapcs  -std=gnu99")

# DEBUG LD FLAGS
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -g  -mcpu=cortex-m4  -mfloat-abi=hard  -mfpu=fpv4-sp-d16  --specs=nano.specs  -lm  -Wall  -fno-common  -ffunction-sections  -fdata-sections  -ffreestanding  -fno-builtin  -Os  -mthumb  -mapcs  -Xlinker --gc-sections  -Xlinker -static  -Xlinker -z  -Xlinker muldefs")

# RELEASE ASM FLAGS
SET(CMAKE_ASM_FLAGS_RELEASE "${CMAKE_ASM_FLAGS_RELEASE} -mcpu=cortex-m4  -mfloat-abi=hard  -mfpu=fpv4-sp-d16  -mthumb  -Wall  -fno-common  -ffunction-sections  -fdata-sections  -ffreestanding  -fno-builtin  -mapcs  -std=gnu99")

# RELEASE C FLAGS
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -Os  -fno-strict-aliasing  -mcpu=cortex-m4  -mfloat-abi=hard  -mfpu=fpv4-sp-d16  -mthumb  -MMD  -MP  -Wall  -fno-common  -ffunction-sections  -fdata-sections  -ffreestanding  -fno-builtin  -mapcs  -std=gnu99")

# RELEASE LD FLAGS
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} -mcpu=cortex-m4  -mfloat-abi=hard  -mfpu=fpv4-sp-d16  --specs=nano.specs  -lm  -Wall  -fno-common  -ffunction-sections  -fdata-sections  -ffreestanding  -fno-builtin  -Os  -mthumb  -mapcs  -Xlinker --gc-sections  -Xlinker -static  -Xlinker -z  -Xlinker muldefs")

# ASM MACRO
SET(CMAKE_ASM_FLAGS_DEBUG "${CMAKE_ASM_FLAGS_DEBUG}  -D__DEBUG")

# C MACRO
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG}  -D__DEBUG")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG}  -DCPU_MCIMX7D_M4")
SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG}  -DFSL_RTOS_FREE_RTOS")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE}  -D__NDEBUG")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE}  -DCPU_MCIMX7D_M4")
SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE}  -DFSL_RTOS_FREE_RTOS")

# CXX MACRO

# INCLUDE_DIRECTORIES
IF(CMAKE_BUILD_TYPE MATCHES Debug)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../..)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../imx7d_sdb_m4)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/portable/GCC/ARM_CM4F)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/CMSIS/Include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices/MCIMX7D/include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices/MCIMX7D/startup)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/utilities/inc)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/platform/imx7d_m4)
ELSEIF(CMAKE_BUILD_TYPE MATCHES Release)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../..)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../imx7d_sdb_m4)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/portable/GCC/ARM_CM4F)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/CMSIS/Include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices/MCIMX7D/include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices/MCIMX7D/startup)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/platform/utilities/inc)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include)
    INCLUDE_DIRECTORIES(${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/platform/imx7d_m4)
ENDIF()

# ADD_EXECUTABLE
ADD_EXECUTABLE(rpmsg_mcu_mpu_hello_world 
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/portable/GCC/ARM_CM4F/port.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/portable/GCC/ARM_CM4F/portmacro.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices/MCIMX7D/startup/gcc/startup_MCIMX7D_M4.S"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/portable/MemMang/heap_2.c"
    "${ProjDirPath}/../../../imx7d_sdb_m4/FreeRTOSConfig.h"
    "${ProjDirPath}/../../../main.c"
    "${ProjDirPath}/../../../rpmsg_config.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/common/llist.c"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/rpmsg_env.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/llist.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/rpmsg_default_config.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/rpmsg_lite.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/rpmsg_ns.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/rpmsg_queue.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/virtio_ring.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/include/virtqueue.h"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/rpmsg_lite/rpmsg_lite.c"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/rpmsg_lite/rpmsg_ns.c"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/rpmsg_lite/rpmsg_queue.c"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/rpmsg_lite/porting/environment/rpmsg_env_freertos.c"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/rpmsg_lite/porting/platform/imx7d_m4/rpmsg_platform.c"
    "${ProjDirPath}/../../../../../middleware/rpmsg-lite/lib/virtio/virtqueue.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/croutine.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/event_groups.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/FreeRTOS.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/list.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/mpu_wrappers.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/portable.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/projdefs.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/queue.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/semphr.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/StackMacros.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/task.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/include/timers.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc/ccm_analog_imx7d.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc/ccm_imx7d.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc/lmem.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc/rdc.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc/rdc_defs_imx7d.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc/wdog_imx.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/croutine.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/event_groups.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/list.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/queue.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/tasks.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/rtos/FreeRTOS/Source/timers.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/src/ccm_analog_imx7d.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/src/ccm_imx7d.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/src/lmem.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/src/rdc.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/src/wdog_imx.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/utilities/src/debug_console_imx.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/utilities/inc/debug_console_imx.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/utilities/src/print_scan.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/utilities/src/print_scan.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices/MCIMX7D/startup/system_MCIMX7D_M4.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/devices/MCIMX7D/startup/system_MCIMX7D_M4.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4/pin_mux.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4/pin_mux.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4/board.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4/board.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4/clock_freq.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/examples/imx7d_sdb_m4/clock_freq.h"
    "${ProjDirPath}/../../../imx7d_sdb_m4/hardware_init.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/src/uart_imx.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc/uart_imx.h"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/src/mu_imx.c"
    "${ProjDirPath}/../../../../../middleware/imx-hal/platform/drivers/inc/mu_imx.h"
)
SET_TARGET_PROPERTIES(rpmsg_mcu_mpu_hello_world PROPERTIES OUTPUT_NAME "rpmsg_mcu_mpu_hello_world.elf")

TARGET_LINK_LIBRARIES(rpmsg_mcu_mpu_hello_world -Wl,--start-group)
# LIBRARIES
IF(CMAKE_BUILD_TYPE MATCHES Debug)
ELSEIF(CMAKE_BUILD_TYPE MATCHES Release)
ENDIF()

# SYSTEM LIBRARIES
TARGET_LINK_LIBRARIES(rpmsg_mcu_mpu_hello_world m)
TARGET_LINK_LIBRARIES(rpmsg_mcu_mpu_hello_world c)
TARGET_LINK_LIBRARIES(rpmsg_mcu_mpu_hello_world gcc)
TARGET_LINK_LIBRARIES(rpmsg_mcu_mpu_hello_world nosys)
TARGET_LINK_LIBRARIES(rpmsg_mcu_mpu_hello_world -Wl,--end-group)

# MAP FILE
SET(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG}  -Xlinker -Map=debug/rpmsg_mcu_mpu_hello_world.map")
SET(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE}  -Xlinker -Map=release/rpmsg_mcu_mpu_hello_world.map")

# BIN AND HEX
ADD_CUSTOM_COMMAND(TARGET rpmsg_mcu_mpu_hello_world POST_BUILD COMMAND ${CMAKE_OBJCOPY} -Oihex ${EXECUTABLE_OUTPUT_PATH}/rpmsg_mcu_mpu_hello_world.elf ${EXECUTABLE_OUTPUT_PATH}/rpmsg_mcu_mpu_hello_world.hex)
ADD_CUSTOM_COMMAND(TARGET rpmsg_mcu_mpu_hello_world POST_BUILD COMMAND ${CMAKE_OBJCOPY} -Obinary ${EXECUTABLE_OUTPUT_PATH}/rpmsg_mcu_mpu_hello_world.elf ${EXECUTABLE_OUTPUT_PATH}/rpmsg_mcu_mpu_hello_world.bin)
