/*
 * Copyright (c) 2015, Freescale Semiconductor, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 * o Redistributions of source code must retain the above copyright notice, this list
 *   of conditions and the following disclaimer.
 *
 * o Redistributions in binary form must reproduce the above copyright notice, this
 *   list of conditions and the following disclaimer in the documentation and/or
 *   other materials provided with the distribution.
 *
 * o Neither the name of Freescale Semiconductor, Inc. nor the names of its
 *   contributors may be used to endorse or promote products derived from this
 *   software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
 * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
 * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <stdio.h>
#include "board.h"
#include "debug_console_imx.h"
#include "ccm_imx7d.h"
#include "rdc.h"
#include "wdog_imx.h"
#include "pin_mux.h"

/* Initialize clock. */
void BOARD_ClockInit(void)
{
    /* OSC/PLL is already initialized by Cortex-A7 (u-boot) */

    /* 
     * Disable WDOG3 
     *  Note : The WDOG clock Root is shared by all the 4 WDOGs, so FreeROTS
     *  code should avoid closing it
     */
    CCM_UpdateRoot(CCM, ccmRootWdog, ccmRootmuxWdogOsc24m, 0, 0);
    CCM_EnableRoot(CCM, ccmRootWdog);
    CCM_ControlGate(CCM, ccmCcgrGateWdog3, ccmClockNeededRun);

    RDC_SetPdapAccess(RDC, BOARD_WDOG_RDC_PDAP, 3 << (BOARD_DOMAIN_ID * 2), false, false);
    WDOG_DisablePowerdown(BOARD_WDOG_BASEADDR);

    CCM_ControlGate(CCM, ccmCcgrGateWdog3, ccmClockNotNeeded);

    /* We need system PLL Div2 to run M4 core */
    CCM_ControlGate(CCM, ccmPllGateSys, ccmClockNeededRun);
    CCM_ControlGate(CCM, ccmPllGateSysDiv2, ccmClockNeededRun);

    /* Enable clock gate for IP bridge and IO mux */
    CCM_ControlGate(CCM, ccmCcgrGateIpmux1, ccmClockNeededRun);
    CCM_ControlGate(CCM, ccmCcgrGateIpmux2, ccmClockNeededRun);
    CCM_ControlGate(CCM, ccmCcgrGateIpmux3, ccmClockNeededRun);
    CCM_ControlGate(CCM, ccmCcgrGateIomux, ccmClockNeededRun);
    CCM_ControlGate(CCM, ccmCcgrGateIomuxLpsr, ccmClockNeededRun);

    /* Enable clock gate for RDC */
    CCM_ControlGate(CCM, ccmCcgrGateRdc, ccmClockNeededRun);
}

/* Initialize debug console. */
void dbg_uart_init(void)
{
    /* Set debug uart for M4 core domain access only */
    RDC_SetPdapAccess(RDC, BOARD_DEBUG_UART_RDC_PDAP, 3 << (BOARD_DOMAIN_ID * 2), false, false);

    /* Select board debug clock derived from OSC clock(24M) */
    CCM_UpdateRoot(CCM, BOARD_DEBUG_UART_CCM_ROOT, ccmRootmuxUartOsc24m, 0, 0);
    /* Enable debug uart clock */
    CCM_EnableRoot(CCM, BOARD_DEBUG_UART_CCM_ROOT);
    /*
     * IC Limitation
     * M4 stop will cause A7 UART lose functionality
     * So we need UART clock all the time
     */
    CCM_ControlGate(CCM, BOARD_DEBUG_UART_CCM_CCGR, ccmClockNeededAll);

    /* Config debug uart pins */
    configure_uart_pins(BOARD_DEBUG_UART_BASEADDR);

    DbgConsole_Init(BOARD_DEBUG_UART_BASEADDR, get_uart_clock_freq(BOARD_DEBUG_UART_BASEADDR), 115200);
}

void BOARD_RdcInit(void)
{
    /* Move M4 core to specific RDC domain */
    RDC_SetDomainID(RDC, rdcMdaM4, BOARD_DOMAIN_ID, false);
}

/*******************************************************************************
 * EOF
 ******************************************************************************/
