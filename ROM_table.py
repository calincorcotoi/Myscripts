import os, openpyxl, sys

fn = sys.argv[1]
print(os.path.basename(fn))
if os.path.exists(fn):
    os.chdir(os.path.dirname(fn))


wb = openpyxl.load_workbook(os.path.basename(fn), data_only = True)

if os.path.exists('ROM_TABLE.txt'):
    os.remove('ROM_TABLE.txt')

file = open('ROM_TABLE.txt','a')

ws = wb.active
i=2
ABIinputCell = ws.cell(row = i,column =5)
while ABIinputCell.value != None:

    safeCell = ws.cell(row = i,column =9)
    initCell = ws.cell(row = i,column =12)
    faultCell = ws.cell(row = i,column =13)
    minCell = ws.cell(row = i,column =15)
    maxCelll = ws.cell(row = i,column =16)

    if minCell.value == None:
        min = 0;
    else:
        min = int(float(minCell.value))

    if maxCelll.value == None:
        max = 'NO MAX VALUE';
    else:
        max = int(float(maxCelll.value))

    if initCell.value == None:
        init = 'NO INIT VALUE';
    else:
        init = int(initCell.value)

    if safeCell.value == None:
        safe = 'NO SAFE VALUE';
    else:
        safe = int(safeCell.value)

    if faultCell.value == None:
        fault = 'AALModar_sl_UNUSED_FAULT'
    else:
        fault = faultCell.value

    file.write('//------------------------------------------------\n' +
           '// Idx/Key :'+ str(i-2)+ ' ' + str(ABIinputCell.value) + '\n' +
           '//------------------------------------------------\n'
           '{\n' + 
           str('// Minimum Limit').center(23,' ') + str('Maximum Limit').center(23,' ') + str('Fault value').center(23,' ') + str('Init value').center(23,' ') + str('Safe value').center(23,' ') +'\n'+
           (str(min)+ ',').center(24,' ')  +          (str(max)+ ',').center(24,' ')  +          (str(fault)+ ',').center(24,' ')  +      (str(init)+ ',').center(24,' ') +      (str(safe)+ ',').center(24,' ') +'\n'
           '},\n\n')

    i=i+1
    ABIinputCell = ws.cell(row = i,column =5)

print("ROM table generated in file =>ROM_TABLE.txt")
file.close()