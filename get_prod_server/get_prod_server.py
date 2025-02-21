#!/usr/bin/python
import subprocess

cid = input("CID --> ")
if len(cid) > 4:
  output = subprocess.check_output("nslookup " + str(cid) + ".tcplusondemand.com", shell = True)
  output = output.decode("utf-8")
  print(output)
  #print('string length : ' + str(len(output)))
  prod_start_index = output.find("prod")
  #print('prod_start_index : ' + str(prod_start_index))
  decimal_loc = 0
  if prod_start_index > 0:
    decimal_loc = output.find(".",prod_start_index)
    str_val = 'decimal_loc : ' + str(decimal_loc)
    prod_number = output[prod_start_index:decimal_loc]
    print(prod_number)
  
  tex = input("input")