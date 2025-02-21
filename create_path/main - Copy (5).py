import tkinter as tk
import pyperclip

btn_index = 0
ary_path = ''
ary_path_str = ''
ary_path_str_base = ''
final_path_str = ''

ary_menu =  \
["Settings", \
  ["My Dashboard", \
  "Hours", \
    ["Individual Hours", \
    "Group Hours", \
    "Mass Hours", \
    "Covered Hours", \
    "Period Export", \
    "Time Sheets"
    ], \
  "Schedules", \
    ["Employee", \
    "Daily", \
    "Weekly", \
    "Recurring", \
    "Template", \
    "Global Scheduler", \
    "Staffing Requirements", \
    "Shift Assignments", \
      ["Shift Roster", \
      "Shift Calendar"
      ], \
    "Shift Board", \
      ["Swaps", \
      "Drops", \
      "Opens"
      ]
    ], \
  "Employee", \
    ["Employee Profiles", \
    "Employee Roles", \
    "Dashboard Templates", \
    "Global Modification", \
    "Employee Messaging", \
    "Pay Progressions", \
    "Employee Recovery"
    ], \
  "Reports", \
    ["Period Reports", \
    "Scheduler Reports", \
    "Analytics"
    ], \
  "Tools", \
    ["Import", \
    "Export", \
    "Employee Status", \
    "Requests", \
      ["Request Manager", \
      "Substitute Assignment Manager", \
      "Leave Bid Manager", \
      "FMLA Case Manager"
      ], \
    "Labor Analytics", \
    "Labor Cost", \
      ["Worked", \
      "Schedule"
      ], \
    "Documents", \
      ["Document Categories", \
      "General Documents"
      ], \
    "QR Code Generator", \
    "Other Tools", \
      ["Attendance Monitor", \
      "Audit Log", \
      "Notifications", \
      "Unresolved Punches", \
      "Data Purge", \
      "Calculator"
      ]
    ], \
  "Configuration", \
    ["Users", \
      ["User Profiles", \
      "User Roles", \
      "Security Check", \
      "Dashboard Templates", \
      "User Delegation"
      ], \
    "Job Codes", \
    "Cost Codes", \
      ["Cost Code Simple Select", \
      "Cost Code List", \
      "Cost Code Tree", \
      "Cost Code Groups", \
      "Cost Code Elements", \
      "Labor Standards"
      ], \
    "Work Profiles", \
    "Accruals", \
      ["Accrual Banks", \
      "Accrual Cap Rules", \
      "Accrual Reset Rules", \
      "Accrual Rules", \
      "Leave Groups", \
      "Leave Calendars"
      ], \
    "Advanced Scheduler", \
      ["AutoFill Profiles", \
      "Master Shifts", \
      "Master Schedules", \
      "Shift Bids", \
      "Sequences", \
      "Swap Limits", \
      "Position Templates", \
      "Publisher"
      ], \
    "Templates", \
      ["Contract Templates", \
      "Request Templates", \
      "Substitute Assignment Templates", \
      "Budget Templates"
      ], \
    "Benefit Status", \
      ["Measurement Periods", \
      "Break Period Groups"
      ], \
    "FMLA", \
      ["Reason Codes", \
      "Questions"
      ], \
    "Geofencing", \
      ["Geofences", \
      "Geofence Groups"
      ], \
    "Other Configurations", \
      ["Clock Configurations", \
      "Shift Schedules", \
      "Automatic Breaks", \
      "Occurrence Rules", \
      "Rotating Overtime Schedules", \
      "Job Classes", \
      "Qualifications", \
      "Locations", \
      "Hour Calculation Priority Groups"
      ]
    ], \
  "Company", \
    ["Close Week", \
    "Company Defaults", \
    "Company Setup", \
    "Company Template", \
    "Custom Fields", \
    "Holidays", \
    "Automated Tasks", \
      ["Manage Automated Task", \
      "Automated Import", \
      "Automation Modules"
      ], \
    "Certificates", \
    "Embeddable Widgets"
    ], \
  "On-Demand Pay", \
    ["About Clair On-Demand Pay", \
    "Settings"
    ], \
  "Quick Links", \
    ["Employee Profiles", \
    "Leave Groups", \
    "Request Templates", \
    "Clock Configurations"
    ]
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
