'''
Author: Yinbo Chen
Class: COMP 6710
Team: 15
Date: 04/25/2023
'''
from scanner import isValidUserName
from scanner import isValidPasswordName
from scanner import isValidKey
from scanner import checkIfValidSecret
from scanner import checkIfValidKeyValue
import sys
import traceback

def doFuzz(inputList, method):
    for inputItem in inputList:
        try:
            result = method(inputItem)
        except Exception:
            print("Exception in user code:")
            print(f'Fuzz:{method.__qualname__} failed!')
            print("-"*80)
            traceback.print_exc(file=sys.stdout)
            print("-"*80)
        else:
            if result == True:
                print(f'Fuzz:{method.__qualname__} passed!')
                print(f'Detect input value is valid:')
                print(f'Test value is {inputItem}')
                print("-"*50)
            else:
                print(f'Fuzz:{method.__qualname__} passed!')
                print(f'Detect input value is invalid:')
                print(f'Test value is {inputItem}')
                print("-"*50)

def generateFuzzValues(funcName):
    returnList = []
    validFuncNameList = ['isValidUserName','isValidPasswordName','isValidKey',\
                     'checkIfValidSecret', 'checkIfValidKeyValue']
    if (isinstance(funcName, str)==False) or (funcName not in validFuncNameList):
        print("Input function name is invalid!")
    else:
        if funcName == validFuncNameList[0]:
            returnList = [0,'%',None,'group_111','domainAuCOMP',\
                        '1234567','\\\\',\
                        '<script\\x2Ftype=\"text/javascript\">javascript:alert(1);</script>',\
                        '𠜎𠜱𠝹𠱓𠱸𠲖𠳏',[]]
        elif funcName == validFuncNameList[1]:
            returnList = [10,'_auth-__','hashTable','/',\
                        True,None,'Null',\
                        '<script\\x2Ftype=\"text/javascript\">javascript:alert(1);</script>',\
                        '0,0/0,0',{}]
        elif funcName == validFuncNameList[2]:
            returnList = [10,'crt_auth-__','key:hashTable','key/',\
                        True,None,'Null',\
                        '<script\\x2Ftype=\"text/javascript\">javascript:alert(1);</script>',\
                        '0,0/0,0',{}]
        elif funcName == validFuncNameList[3]:
            returnList = [10,'unset_auth-__','key:hashTable','/',\
                        True,None,'undefined',\
                        '<script\\x2Ftype=\"text/javascript\">javascript:alert(1);</script>',\
                        '0,0/0,0',[]]
        elif funcName == validFuncNameList[4]:
            returnList = [0,'-----BEGIN RSA PRIVATE KEY-----crt_auth-__','key:hashTable','key/',\
                        True,None,'Null',\
                        '<script\\x2Ftype=\"text/javascript\">-----BEGIN CERTIFICATE-----</script>',\
                        '0,0/0,0',{}]
        else:
            print("Input function name is invalid!")
    return returnList
if __name__=="__main__":
    method = [isValidUserName,isValidPasswordName,isValidKey,\
            checkIfValidSecret, checkIfValidKeyValue]
    testFuncCount = 1
    for funcNameDenote in method:
        print("*"*50)   
        print(" "*10,f'{testFuncCount}.{funcNameDenote.__qualname__}:')
        print("*"*50)
        returnedList = generateFuzzValues(funcNameDenote.__qualname__)
        doFuzz(returnedList, funcNameDenote)
        testFuncCount+=1

