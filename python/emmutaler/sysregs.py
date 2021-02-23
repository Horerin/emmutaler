from parse import parse

SYSREGS = {
    'S3_0_c15_c0_0'  : ( 'HID0', '' ),
    'S3_0_c15_c0_1'  : ( 'EHID0', '' ),
    'S3_0_c15_c1_0'  : ( 'HID1', '' ),
    'S3_0_c15_c1_1'  : ( 'EHID1', '' ),
    'S3_0_c15_c2_0'  : ( 'HID2', '' ),
    'S3_0_c15_c2_1'  : ( 'EHID2', '' ),
    'S3_0_c15_c3_0'  : ( 'HID3', '' ),
    'S3_0_c15_c3_1'  : ( 'EHID3', '' ),
    'S3_0_c15_c4_0'  : ( 'HID4', '' ),
    'S3_0_c15_c4_1'  : ( 'EHID4', '' ),
    'S3_0_c15_c5_0'  : ( 'HID5', '' ),
    'S3_0_c15_c5_1'  : ( 'EHID5', '' ),
    'S3_0_c15_c6_0'  : ( 'HID6', '' ),
    'S3_0_c15_c7_0'  : ( 'HID7', '' ),
    'S3_0_c15_c8_0'  : ( 'HID8', '' ),
    'S3_0_c15_c9_0'  : ( 'HID9', '' ),
    'S3_0_c15_c10_0' : ( 'HID10', '' ),
    'S3_0_c15_c10_1' : ( 'EHID10', '' ),
    'S3_0_c15_c11_0' : ( 'HID11', '' ),
    'S3_0_c15_c11_1' : ( 'EHID11', '' ),
    'S3_0_c15_c14_0' : ( 'HID13', '' ),
    'S3_0_c15_c15_0' : ( 'HID14', '' ),
    'S3_0_c15_c15_2' : ( 'HID16', '' ),
    'S3_1_c15_c0_0'  : ( 'PMCR0', 'Apple Performance Monitor Control Register 0' ),
    'S3_1_c15_c1_0'  : ( 'PMCR1', 'Controls which execution modes count events' ),
    'S3_1_c15_c2_0'  : ( 'PMCR2', 'Controls watchpoint registers' ),
    'S3_1_c15_c3_0'  : ( 'PMCR3', 'Controls breakpoints and address matching' ),
    'S3_1_c15_c4_0'  : ( 'PMCR4', 'Controls opcode matching' ),
    'S3_1_c15_c5_0'  : ( 'PMESR0', '' ),
    'S3_1_c15_c6_0'  : ( 'PMESR1', '' ),
    'S3_1_c15_c7_0'  : ( 'OPMAT0', '' ),
    'S3_1_c15_c8_0'  : ( 'OPMAT1', '' ),
    'S3_1_c15_c9_0'  : ( 'OPMSK0', '' ),
    'S3_1_c15_c10_0' : ( 'OPMSK1', '' ),
    'S3_1_c15_c13_0' : ( 'PMSR', '' ),
    'S3_2_c15_c0_0'  : ( 'PMC0', '48-bit cycles counter' ),
    'S3_2_c15_c1_0'  : ( 'PMC1', '48-bit instructions counter' ),
    'S3_2_c15_c2_0'  : ( 'PMC2', '' ),
    'S3_2_c15_c3_0'  : ( 'PMC3', '' ),
    'S3_2_c15_c4_0'  : ( 'PMC4', '' ),
    'S3_2_c15_c5_0'  : ( 'PMC5', '' ),
    'S3_2_c15_c6_0'  : ( 'PMC6', '' ),
    'S3_2_c15_c7_0'  : ( 'PMC7', '' ),
    'S3_2_c15_c9_0'  : ( 'PMC8', '' ),
    'S3_2_c15_c10_0' : ( 'PMC9', '' ),
    'S3_2_c15_c12_0' : ( 'PMTRHLD6', '' ),
    'S3_2_c15_c13_0' : ( 'PMTRHLD4', '' ),
    'S3_2_c15_c14_0' : ( 'PMTRHLD2', '' ),
    'S3_2_c15_c15_0' : ( 'PMMMAP', '' ),
    'S3_3_c15_c0_0'  : ( 'LSU_ERR_STS', 'LSU Error Status' ),
    'S3_3_c15_c1_0'  : ( 'LSU_ERR_CTL', 'LSU Error Control' ),
    'S3_3_c15_c2_0'  : ( 'E_LSU_ERR_STS', 'LSU Error Status' ),
    'S3_3_c15_c7_0'  : ( 'L2_CRAMCONFIG', 'LSU Error Status' ),
    'S3_3_c15_c8_0'  : ( 'LLC_ERR_STS', 'LLC Error Status' ),
    'S3_3_c15_c8_1'  : ( 'L2E_ERR_STS', '' ),
    'S3_3_c15_c9_0'  : ( 'LLC_ERR_ADR', 'LLC Error Address' ),
    'S3_3_c15_c9_1'  : ( 'L2E_ERR_ADR', '' ),
    'S3_3_c15_c10_0' : ( 'LLC_ERR_INF', 'LLC Error Information' ),
    'S3_3_c15_c10_1' : ( 'L2E_ERR_INF', '' ),
    'S3_4_c15_c0_0'  : ( 'FED_ERR_STS', 'FED Error Status' ),
    'S3_4_c15_c0_2'  : ( 'E_FED_ERR_STS', 'FED Error Status' ),
    'S3_4_c15_c0_4'  : ( 'APCTL_EL1/MIGSTS', '' ),
    'S3_4_c15_c1_0'  : ( 'KERNELKEYLO_EL1', 'PAC Kernel Key (bits[63:0])' ),
    'S3_4_c15_c1_1'  : ( 'KERNELKEYHI_EL1', 'PAC Kernel Key (bits[127:64])' ),
    'S3_4_c15_c1_2'  : ( 'VMSA_LOCK_EL1', 'VMSA Lock' ),
    'S3_4_c15_c1_6'  : ( 'CTRR_B_UPR_EL1', 'CTRR Upper Range B' ),
    'S3_4_c15_c1_7'  : ( 'CTRR_B_LWR_EL1', 'CTRR Lower Range B' ),
    'S3_4_c15_c2_0'  : ( 'APRR_0', 'APRR Register 0' ),
    'S3_4_c15_c2_1'  : ( 'APRR_1', 'APRR Register 1' ),
    'S3_4_c15_c2_2'  : ( 'CTRR_LOCK', 'CTRR Lockdown' ),
    'S3_4_c15_c2_3'  : ( 'CTRR_A_LWR_EL1', 'CTRR Lower Range' ),
    'S3_4_c15_c2_4'  : ( 'CTRR_A_UPR_EL1', 'CTRR Upper Range' ),
    'S3_4_c15_c2_5'  : ( 'CTRR_CTL_EL1', 'CTRR Control Register' ),
    'S3_4_c15_c2_6'  : ( 'APRR_6', 'APRR Register 6' ),
    'S3_4_c15_c2_7'  : ( 'APRR_7', 'APRR Register 7' ),
    'S3_4_c15_c11_0' : ( 'ACC_CTRR_A_LWR_EL2', '' ),
    'S3_4_c15_c11_1' : ( 'ACC_CTRR_A_UPR_EL2', '' ),
    'S3_4_c15_c11_4' : ( 'ACC_CTRR_CTL_EL2', '' ),
    'S3_4_c15_c11_5' : ( 'ACC_CTRR_LOCK_EL2', '' ),
    'S3_5_c15_c0_0'  : ( 'IPI_RR_LOCAL', '' ),
    'S3_5_c15_c0_1'  : ( 'IPI_RR_GLOBAL', '' ),
    'S3_5_c15_c0_5'  : ( 'DPC_ERR_STS', '' ),
    'S3_5_c15_c1_1'  : ( 'IPI_SR', '' ),
    'S3_5_c15_c3_1'  : ( 'IPI_CR', '' ),
    'S3_5_c15_c4_0'  : ( 'ACC_CFG/CYC_CFG', '' ),
    'S3_5_c15_c5_0'  : ( 'CYC_OVRD', '' ),
    'S3_5_c15_c6_0'  : ( 'ACC_OVRD', '' ),
    'S3_5_c15_c6_1'  : ( 'ACC_EBLK_OVRD', '' ),
    'S3_6_c15_c0_0'  : ( 'MMU_ERR_STS', 'MMU Error Status' ),
    'S3_6_c15_c2_0'  : ( 'E_MMU_ERR_STS', 'MMU Error Status' ),
    'S3_6_c15_c12_4' : ( 'APSTS_EL1', '' ),
    'S3_7_c15_c0_4'  : ( 'UPMCR0', 'Controls which counters are enabled and how interrupts are generated for overflows' ),
    'S3_7_c15_c0_5'  : ( 'UPMC8', '' ),
    'S3_7_c15_c1_4'  : ( 'UPMESR0', 'Event selection register for counters 0-7' ),
    'S3_7_c15_c1_5'  : ( 'UPMC9', '' ),
    'S3_7_c15_c2_5'  : ( 'UPMC10', '' ),
    'S3_7_c15_c3_4'  : ( 'UPMECM0', 'Event core masks for counters 0-3' ),
    'S3_7_c15_c3_5'  : ( 'UPMC11', '' ),
    'S3_7_c15_c4_4'  : ( 'UPMECM1', 'Event core masks for counters 4-7' ),
    'S3_7_c15_c4_5'  : ( 'UPMC12', '' ),
    'S3_7_c15_c5_4'  : ( 'UPMPCM', '' ),
    'S3_7_c15_c5_5'  : ( 'UPMC13', '' ),
    'S3_7_c15_c6_4'  : ( 'UPMSR', '' ),
    'S3_7_c15_c6_5'  : ( 'UPMC14', '' ),
    'S3_7_c15_c7_4'  : ( 'UPMC0', '' ),
    'S3_7_c15_c7_5'  : ( 'UPMC15', '' ),
    'S3_7_c15_c8_4'  : ( 'UPMC1', '' ),
    'S3_7_c15_c8_5'  : ( 'UPMECM2', 'Event core masks for counters 8-11' ),
    'S3_7_c15_c9_4'  : ( 'UPMC2', '' ),
    'S3_7_c15_c9_5'  : ( 'UPMECM3', 'Event core masks for counters 12-15' ),
    'S3_7_c15_c10_4' : ( 'UPMC3', '' ),
    'S3_7_c15_c11_4' : ( 'UPMC4', '' ),
    'S3_7_c15_c11_5' : ( 'UPMESR1', 'Event selection register for counters 8-15' ),
    'S3_7_c15_c12_4' : ( 'UPMC5', '' ),
    'S3_7_c15_c13_4' : ( 'UPMC6', '' ),
    'S3_7_c15_c14_4' : ( 'UPMC7', '' ),
}

SYSREG_FMT = "S{op0:d}_{op1:d}_c{cn:d}_c{cm:d}_{op2:d}"

def psysop(op, len):
    return f"{op:0{len}b}"

def parse_sys_reg(reg):
    res = parse(SYSREG_FMT, reg)
    return [psysop(res['op0'], 2), psysop(res['op1'], 3), psysop(res['cn'], 4), psysop(res['cm'], 4), psysop(res['op2'], 3)]



    

