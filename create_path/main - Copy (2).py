import tkinter as tk

btn_index = 0
ary_path = ''
ary_path_str = ''
ary_path_str_base = ''
final_path_str = ''

'''
ary_menu = [ ["My Dashboard"] , \
             ["Hours", \
               ["Individual Hours", \
               "Group Hours", \
               "Mass Hours", \
               "Covered Hours", \
               "Period Export", \
               "Time Sheets" \
               ] \
             ], \
             ["Schedules", \
               ["Employee", \
                "Daily", \
                "Weekly", \
                "Recurring", \
                "Template", \
                "Global Scheduler", \
                "Staffing Requirements", \
                  ["Shift Assignments", \
                    ["Shift Roster","Shift Calendar"]], \
                  ["Shift Board", \
                    ["Swaps","Drops","Opens"] \
                  ] \
                ] \
             ] \
           ]
'''
           
ary_menu = ["My Dashboard", "Hours", ["Individual Hours", "Group Hours"], "Schedules", ["Employee", "Shift Assignments", ["Shift Roster","Shift Calendar"]]]

# if ary_path list has more than one element:
  # display first level elements in list
  # 


window = tk.Tk()
window.resizable()
  
def func(args):
    print(args)
    
def load_page_buttons(ary_path, final_path_str):
  print(ary_path)
  if ary_path == '':
    final_path_str = "Settings"
    print("final_path_str : " + final_path_str)
  else:
    final_path_str = final_path_str + " > " + eval('ary_menu' + ary_path + '[0]')
    print("final_path_str : " + final_path_str)
    
  # clear previous buttons
  for widget in window.winfo_children():
    widget.destroy()  
  
  ary_path_str_base = ary_path
  curr_ary_full = eval('ary_menu' + ary_path)
  if not(isinstance(curr_ary_full,str)):
    for i in range(0,len(curr_ary_full)):
      curr_element = curr_ary_full[i]
      if not(isinstance(curr_element,str)): # element is a list
        ary_path_str = ary_path_str_base + "[" + str(i) + "]"
        for j in range(0,len(curr_element)):
          curr_list_item = curr_element[j] 
          if isinstance(curr_list_item, str): 
            curr_label = curr_element[j]
            btn0 = tk.Button(text = curr_label, command=lambda ary_path_str = ary_path_str : load_page_buttons(ary_path_str, final_path_str))
            btn0.pack()
  else:
    print("final_path_str : " + final_path_str)
    

load_page_buttons('', final_path_str)    

window.mainloop()
