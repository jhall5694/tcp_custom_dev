import tkinter as tk

ary_main_menu = ['ary_main_menu',{"no_ary" : "My Dashboard" , "ary_hours" : "Hours", "ary_schedules" : "Schedules"}]
ary_hours = ['ary_hours', {"ary_individual_hours":"Individual Hours","ary_group_hours":"Group Hours","ary_mass_hours":"Mass Hours","ary_covered_hours":"Covered Hours","ary_period_export":"Period Export","ary_time_sheets":"Time Sheets"}]
ary_schedules = ['ary_schedules',{"no_ary":"Employee","no_ary":"Daily","no_ary":"Weekly","no_ary":"Recurring","no_ary":"Template","no_ary":"Global Scheduler","no_ary":"Staffing Requirements","ary_shift_assignments":"Shift Assignments","ary_shift_board":"Shift Board"}]
ary_shift_assignments = ['ary_shift_assignments',{"no_ary":"Shift Roster","no_ary":"Shift Calendar"}]
ary_shift_board = ['ary_shift_board',{"no_ary":"Swaps","no_ary":"Drops","no_ary":"Opens"}]

ary_all_arys = [ary_main_menu, ary_hours, ary_schedules, ary_shift_assignments, ary_shift_board]

window = tk.Tk()



def handle_click(ary_name, dict_key):
  #print(event)
  #print("The button was clicked!")
  
  # see if there is a matching list / sub-menu
  if dict_key != "no_ary":
    try:
      curr_dict = ary_name[1]
      #cmd_str = 'curr_dict = ' + ary_name + '[1]'
      #print("cmd_str 4: " + cmd_str)
      #eval(cmd_str)  
      #print(curr_dict)
      
    except:
      None
      
    else:
      # get dict index
      
      # get dict index
      print(curr_dict)

      print(dict_key)
      print("here 6")
      eval('print(' + dict_key + ')')
      cmd_str = 'new_ary = ' + dict_key
      print(cmd_str)
      eval(cmd_str)      
      print(cmd_str)
      print("here 5")
      print(new_ary)
      load_page_buttons(new_ary)
  
def load_page_buttons(curr_ary_full):
  # clear previous buttons
  for widget in window.winfo_children():
    widget.destroy()  
  # clear previous buttons
  
  curr_ary_name = curr_ary_full[0]
  curr_dict = curr_ary_full[1]
  print("here 3")
  print(curr_dict)
  print("here 4")
  indx = 0
  for key in curr_dict:
    val = curr_dict[key]
    print("indx : " + str(indx) + "   key : " + key + "   val : " + val)
    cmd_str = 'btn' + str(indx) + ' = tk.Button(text="' + val + '")'
    print("cmd_str 1: " + cmd_str)
    eval(cmd_str)
    cmd_str = 'btn' + str(indx) + '.pack()'
    print("cmd_str 2: " + cmd_str)
    eval(cmd_str)    
    cmd_str = 'btn' + str(indx) + '.bind("<Button-1>", handle_click(' + curr_ary_name + ', "' + key + '" ))'
    print("cmd_str 3: " + cmd_str)
    indx = indx + 1
    eval(cmd_str)
    
    #greeting = tk.Button(text = "hello tkinter")
    #greeting.pack()    
    
load_page_buttons(ary_main_menu)    

window.mainloop()
