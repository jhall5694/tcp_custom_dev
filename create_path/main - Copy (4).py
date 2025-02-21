import tkinter as tk
import pyperclip

btn_index = 0
ary_path = ''
ary_path_str = ''
ary_path_str_base = ''
final_path_str = ''

ary_menu =  ["Settings", 
              [ "My Dashboard", \
                "Hours", \
                  ["Individual Hours","Group Hours","Mass Hours","Covered Hours","Period Export","Time Sheets"], \
                "Schedules", \
                  ["Employee","Daily","Weekly","Recurring","Template","Global Scheduler", \
                   "Staffing Requirements", \
                    ["Shift Assignments", \
                      ["Shift Roster","Shift Calendar"], \
                     "Shift Board", \
                      ["Swaps","Drops","Opens"] \
                    ] \
                  ], \
                "Employee", \
                  ["Employee Profiles", \
                    ["(specific Employee Profile)", \
                      ["Information", \
                        ["Personal", \
                          ["ID","First Name"], \
                         "Company",
                           ["Active","Classification"],\
                        ],
                       "Jobs",
                         ["Work Profile", \
                           ["Assign"]
                         ]  
                      ]
                    ]
                  ],\
                "Reports", \
                  ["Period Reports"] ,\
                "Tools", \
                  ["Import", "Requests" ,
                    ["Request Manager"]], \
                "Configuration", \
                  ["Users",["User Profiles"]], \
                "Company", \
                  ["Close Week", \
                   "Automated Task", \
                     ["Manage Automated Task"]], \
                "On-Demand Pay", \
                  ["About Clair On-Demand Pay"]                          
              ]
            ]
          
window = tk.Tk()
window.resizable()
  


def load_page_buttons(ary_path, curr_element, final_path_str):
  print(ary_path)
  if ary_path == '[1]':
    final_path_str = curr_element  
  else:
    final_path_str = final_path_str + ' > ' + curr_element  
  # clear previous buttons
  for widget in window.winfo_children():
    widget.destroy()  
  
  # entry box holds final path string for user viewing and copy
  lbl = tk.Entry(width=250)
  lbl.pack()
  lbl.insert(0,final_path_str)

  #copy button
  btn_copy = tk.Button(text="copy", command=pyperclip.copy(lbl.get()))
  btn_copy.pack() 
  
  # start over button
  btn_restart = tk.Button(text="start over", command=lambda : load_page_buttons('', '', ''))
  btn_restart.pack()

  
  # exit button
  btn_exit = tk.Button(text="exit", command=exit)
  btn_exit.pack()  
  
 

  
  try:  
    curr_ary_full = eval('ary_menu' + ary_path)
  except:
    print(final_path_str)
  else:
    if isinstance(curr_ary_full,str):
      print(final_path_str)
    else:
      for i in range(0,len(curr_ary_full)):
        curr_element = curr_ary_full[i]
        if isinstance(curr_element,str):
          ary_path_str = ary_path + "[" + str(i + 1) + "]"
          btn0 = tk.Button(text = curr_element, command=lambda \
            ary_path_str = ary_path_str, \
            curr_element = curr_element, \
            final_path_str = final_path_str : \
            load_page_buttons(ary_path_str, curr_element,final_path_str))
          btn0.pack()      
      
load_page_buttons('', '', '')    


window.mainloop()
