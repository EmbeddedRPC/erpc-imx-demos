/*
 * Copyright 2016 Freescale Semiconductor, Inc. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 * 3. Neither the name of Mentor Graphics Corporation nor the names of its
 *    contributors may be used to endorse or promote products derived from this
 *    software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include "assert.h"
#include "rpmsg_lite.h"
#include "rpmsg_queue.h"
#include "rpmsg_ns.h"
#include "FreeRTOS.h"
#include "task.h"
#include "string.h"
#include "stdint.h"
#include "board.h"
#include "debug_console_imx.h" 

#define REMOTE_DEFAULT_EPT (TC_REMOTE_EPT_ADDR)

#define TC_LOCAL_EPT_ADDR (30)
#define TC_REMOTE_EPT_ADDR (40)

void* rpmsg_lite_base = BOARD_SHARED_MEMORY_BASE;

struct rpmsg_lite_endpoint *ctrl_ept;
rpmsg_queue_handle ctrl_q;
struct rpmsg_lite_instance *my_rpmsg = NULL;

#define TASK_STACK_SIZE 300

/*
 * MU Interrrupt ISR
 */
void BOARD_MU_HANDLER (void)
{
    /*
     * calls into rpmsg_handler provided by middleware
     */
    rpmsg_handler();
}

void test(void *unused)
{
    int recved = 0;
    unsigned long src;
    char buf[256];
    int len;

    hardware_init();
    PRINTF("Hardware initialized\r\n");

    env_init();
    my_rpmsg = rpmsg_lite_remote_init(rpmsg_lite_base, RL_PLATFORM_IMX6SX_M4_LINK_ID, RL_NO_FLAGS);
    ctrl_q = rpmsg_queue_create(my_rpmsg);
    ctrl_ept = rpmsg_lite_create_ept(my_rpmsg, TC_LOCAL_EPT_ADDR, rpmsg_queue_rx_cb, ctrl_q);
    PRINTF("Waiting for master to get ready...\r\n");
    while(!rpmsg_lite_is_link_up(my_rpmsg))
    {
       PRINTF(".");
       vTaskDelay(300);
    }
    PRINTF("Sending name service announcement to Linux...\r\n");
    rpmsg_ns_announce(my_rpmsg, ctrl_ept, "rpmsg-openamp-demo-channel", RL_NS_CREATE);
    PRINTF("Waiting for any messages from Linux...\r\n");
    while(1)
    {
    	rpmsg_queue_recv(my_rpmsg, ctrl_q, &src, (char*)buf, 256, &recved, RL_BLOCK);
    	PRINTF("\n\n\rFrom endpoint %d received %d bytes:\n\r", (int)src, recved);
    	PRINTF(buf);
    	len = sprintf(buf, "Oh you don't say number %d!", (int)src);
    	PRINTF("\n\n\rSending %d bytes to endpoint %d:\n\r ", len, src);
    	PRINTF(buf);
    	rpmsg_lite_send(my_rpmsg, ctrl_ept, src, buf, len, RL_BLOCK);
    }


    rpmsg_lite_destroy_ept(my_rpmsg, ctrl_ept);
    rpmsg_queue_destroy(my_rpmsg, ctrl_q);
    rpmsg_lite_deinit(my_rpmsg);


    while (1)
        ;
}

TaskHandle_t test_task_handle = NULL;
int main(void)
{
    int result =
        xTaskCreate(test, "TEST_TASK", TASK_STACK_SIZE, NULL, tskIDLE_PRIORITY + 1, &test_task_handle);
    assert(pdPASS == result);
    vTaskStartScheduler();
    return 0;
}


