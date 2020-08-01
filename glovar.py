# GLOBAL VARIABLES
# All units are in um

GRID = 0.005
min_w = dict()
min_w['CO'] = 0.05
min_w['M1'] = 0.1
min_w['SP'] = 0.1
# Layer Map
layer = dict()
layer['LVSDMY'] = 208
layer['MOMDMY'] = 155 
layer['DMEXCL'] = 150 
layer['RH'] = 117
layer['RPDMY'] = 115
layer['VTH_P'] = 68
layer['VTH_N'] = 67
layer['VIA8'] = 58
layer['VIA7'] = 57
layer['VIA6'] = 56
layer['VIA5'] = 55
layer['VIA4'] = 54
layer['VIA3'] = 53
layer['VIA2'] = 52
layer['VIA1'] = 51
layer['M8'] = 38
layer['M7'] = 37
layer['M6'] = 36
layer['M5'] = 35
layer['M4'] = 34
layer['M3'] = 33
layer['M2'] = 32
layer['M1'] = 31
layer['CO'] = 30
layer['RPO'] = 29
layer['NP'] = 26
layer['PP'] = 25
layer['OD_25'] = 18
layer['PO'] = 17
layer['VTL_P'] = 13
layer['VTL_N'] = 12
layer['NT_N'] = 11
layer['OD'] = 6
layer['NW'] = 3
datatype = dict()
datatype['M1'] = 0
datatype['M2'] = 0
datatype['M3'] = 0
datatype['M4'] = 0
datatype['M5'] = 0
datatype['M6'] = 0
datatype['M7'] = 40
datatype['M8'] = 40
datatype['VIA1'] = 0
datatype['VIA2'] = 0
datatype['VIA3'] = 0
datatype['VIA4'] = 0
datatype['VIA5'] = 0
datatype['VIA6'] = 40
datatype['VIA7'] = 40
sp = dict()
sp['CO'] = dict()
sp['CO']['CO'] = 0.1
sp['CO']['PO'] = 0.05
sp['CO']['RPO'] = 0.2
sp['M1'] = dict()
sp['M1']['M1'] = 0.15 
en = dict()
en['M1'] = dict()
en['M1']['CO'] = 0.05 
en['OD'] = dict()
en['OD']['PO'] = 0.10
en['OD']['CO'] = 0.05
en['PO'] = dict()
en['PO']['CO'] = 0.05
en['NP'] = dict()
en['NP']['PO'] = 0.10
en['NW'] = dict()
en['NW']['OD'] = [0.05, 0.15] 
en['PP'] = en['NP']  
en['NT_N'] = dict()
en['NT_N']['OD'] = 0.25
en['RH'] = dict()
en['RH']['PO'] = 0.2
ex = dict()
ex['PO'] = dict()
ex['PO']['OD'] = 0.1
ex['NP'] = dict()
ex['NP']['OD'] = 0.1
ex['PP'] = ex['NP']
ex['RPO'] = dict()
ex['RPO']['PO'] = 0.5
NWELL_GR = True
NW_OD = 0.10
NP_OD = 0.05
OD_W = 0.15
SUB_GR = False
KR_SP = 0
