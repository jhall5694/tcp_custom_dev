from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import pyperclip
import time
import datetime
import webbrowser


class parse_badge():
  def __init__(self):
    self.exit_program = False
    self.num_binary_entry_fields = 15
    self.app_initialized = True
    self.replace_char = " ."
    self.str_binary_full = None
    self.pos_start = None
    self.bit_length = None
    self.str_decimal_full = None
    self.total_bit_length = None

    self.tk_default_padx = 5
    self.tk_default_pady = 5
    self.frame_row_count = 1
    self.frame_border_width = 1
    self.tkinter_frame_border_display = False
    #self.tkinter_frame_border_display = True
    
    self.tool_tips_on = True    

    self.color_blue_1 = '#004989'
    self.color_blue_2 = '#0082BA'
    self.color_blue_3 = '#00B5E2'
    self.color_blue_4 = '#004989'
    self.color_green_1 = '#93d500'
    self.color_green_2 = '#93d500'
    self.color_green_3 = '#93d500'
    self.color_green_4 = '#93d500'
 
    self.color_bit_option_elements = 'lightblue'
    self.color_generate_elements = 'lightblue'
    #self.color_btn_on = '#93d500'
    self.color_btn_on = self.color_green_1
    self.color_btn_off = 'lightgrey'


    self.create_window()

  # logging -----------------------------------------------------------------
  def write_to_log_file(self, data):
    self.file_write = open("log.txt","a") # log file
    self.file_write.write(str(datetime.datetime.now()) + " : " + data + "\n")
    self.file_write.close()

  def write_to_notes_file(self,data):
    self.file_write = open("notes.txt","a") # log file
    self.file_write.write(data + " : " + str(datetime.datetime.now()) + "\n")
    self.file_write.close()

  def date_time_str(self):
    now = datetime.datetime.now()
    mo = str(now.month)
    if len(mo) < 2:
      mo = "0" + mo
    da = str(now.day)
    if len(da) < 2:
      da = "0" + da
    yr = str(now.year)[2:4]
    hr = str(now.hour)
    if len(hr) < 2:
      hr = "0" + hr
    mi = str(now.minute)
    if len(mi) < 2:
      mi = "0" + mi
    timestamp = mo + da + yr + "_" + hr + mi
    return timestamp



  # data workers -----------------------------------------------------------------
  def binary_to_decimal(self,str_bin):
    return_val = 0
    bin_multiplier = 0
    for i in range(len(str_bin)-1,-1,-1):
      curr_char = str_bin[i]
      match curr_char:
        case '1':
          return_val = return_val + pow(2, bin_multiplier)

      bin_multiplier = bin_multiplier + 1

    return return_val

  def decimal_to_binary(self):
    if self.str_decimal_full == '':
      self.post_message('enter a value in the "full decimal" field')
      return

    self.val_desired_decimal = int(self.str_decimal_full)

    # clear previous
    self.update_entry_field('entry_binary_full_val','')
    self.update_entry_field('entry_binary_partial','')
    self.update_entry_field('entry_decimal_partial',self.val_desired_decimal)
    
    # get start bit and length info
    if self.pos_start == '':
      self.pos_start = 1
      self.update_entry_field('entry_start_position','1')
    else:
      self.pos_start = int(self.pos_start)

    if self.bit_length == '':
      self.bit_length = 0
    else:
      self.bit_length = int(self.bit_length)

    if self.total_bit_length == '':
      self.total_bit_length = 0
    else:
      self.total_bit_length = int(self.total_bit_length)

    str_binary = '0' * (self.pos_start - 1)

    # generate binary string
    remaining_decimal = self.val_desired_decimal

    start_posting = False
    for i in range(60,-1,-1):
      curr_binary_val = pow(2,i)
      prev_binary_val = pow(2,i+1)
      if curr_binary_val <= remaining_decimal and prev_binary_val > remaining_decimal:
        if start_posting == False:
          start_posting = True
          if self.bit_length == 0 or self.bit_length < i + 1: # user did not enter a bit length or bit length entered is not sufficient
            self.bit_length = i + 1
            self.update_entry_field('entry_bit_length',self.bit_length)
          elif self.bit_length > i + 1: # prepend 0's in consideration of bit length entered by user i.e. bit length entered is greater than what is necessary to generate decimal value
            str_binary = str_binary + '0' * (self.bit_length - i - 1)
        str_binary = str_binary + "1"
        remaining_decimal = remaining_decimal - pow(2,i)
      elif start_posting == True:
        str_binary = str_binary + "0"

    # pad 0's if necessary
    if len(str_binary) < self.total_bit_length:
      if self.parse_mode == "parse_then_translate":
        str_binary = str_binary + '0' * (self.total_bit_length - len(str_binary))
      else:
        str_binary = '0' * (self.total_bit_length - len(str_binary)) + str_binary
    self.total_bit_length = len(str_binary)
    self.update_entry_field('entry_total_length',self.total_bit_length)

    # update binary short fields
    self.update_binary_short_fields()
    
    if remaining_decimal != 0:
      self.post_message('total length too short for requested decimal')
      return

    self.update_entry_field('entry_binary_full_val',str_binary)
    self.str_binary_full = str_binary
    self.generate_partial_binary()

  def generate_partial_decimal(self):
    # parse partial decimal string
    self.pos_start = self.pos_start - 1
    self.str_decimal_partial = str(self.val_decimal_full)[self.pos_start:self.pos_start + self.bit_length]
    # the following is not in use (format problems) - new decimal string with self.replace_char inserted in front of and after new parsed decimal
    #str_new = self.replace_char * self.pos_start + self.str_decimal_partial + self.replace_char * (len(self.str_decimal_full) - self.pos_start - self.bit_length)
    #self.update_entry_field('entry_decimal_partial',str_new)
    self.update_entry_field('entry_decimal_partial',self.str_decimal_partial)
    
  def generate_partial_binary(self):
    # parse partial binary string
    self.pos_start = self.pos_start - 1
    self.str_binary_partial = self.str_binary_full[self.pos_start:self.pos_start + self.bit_length]
    # new full binary string with self.replace_char inserted in front of and after new parsed binary
    if self.parse_mode == "parse_then_translate":
      str_new = self.replace_char * self.pos_start + self.str_binary_partial + self.replace_char * (len(self.str_binary_full) - self.pos_start - self.bit_length)
    else:
      str_new = self.str_binary_full
    self.update_entry_field('entry_binary_partial',str_new)

  def parse_then_translate(self):
    if self.create_binary_string_successful()  == False:
      return
      
    # get start bit and length info
    if self.pos_start == '':
      self.pos_start = 1
      self.update_entry_field('entry_start_position','1')
    else:
      self.pos_start = int(self.pos_start)

    if self.bit_length == '':
      self.bit_length = len(self.str_binary_full)
      self.update_entry_field('entry_bit_length',str(self.bit_length))
    else:
      self.bit_length = int(self.bit_length)

    self.generate_partial_binary()

    # convert binary to decimal
    val_decimal = self.binary_to_decimal(self.str_binary_partial)

    # post resulting decimal
    self.update_entry_field('entry_decimal_full',val_decimal)
    self.update_entry_field('entry_decimal_partial',val_decimal)

  def translate_then_parse(self):
    if self.create_binary_string_successful()  == False:
      return
    self.val_decimal_full = self.binary_to_decimal(self.str_binary_full)
    self.str_decimal_full = str(self.val_decimal_full)
    self.update_entry_field('entry_decimal_full',self.val_decimal_full)
    
    # get start bit and length info
    if self.pos_start == '':
      self.pos_start = 1
      self.update_entry_field('entry_start_position','1')
    else:
      self.pos_start = int(self.pos_start)

    if self.bit_length == '':
      self.bit_length = len(self.str_binary_full)
      self.update_entry_field('entry_bit_length',str(self.bit_length)) 
    else:
      self.bit_length = int(self.bit_length)    
      
    self.generate_partial_decimal()

  def update_binary_short_fields(self):
    # update short fields to match full binary field
    
    # clear current binary short fields
    for i in range(self.num_binary_entry_fields):
      exec('self.update_entry_field("entry_binary_' + str(i) + '","")')

    # update short fields
    curr_binary_short_field = 0
    for i in range(0,len(self.str_binary_full),4):
      curr_str = self.str_binary_full[i:i+4]
      if curr_str == '':
        break
      else:
        exec('self.update_entry_field("entry_binary_' + str(curr_binary_short_field) + '","' + curr_str + '")')
      curr_binary_short_field = curr_binary_short_field + 1  
  
  def create_binary_string_successful(self):  
    valid_binary_short_fields = True
    valid_binary_full_field = True
    # see if data exists in binary short fields - if so, concatenate into continuous binary string
    str_from_binary_short_fields = ''  
    for i in range(self.num_binary_entry_fields):
      curr_bin_val = eval('self.entry_binary_' + str(i) + '.get()')
      str_from_binary_short_fields = str_from_binary_short_fields + curr_bin_val
    
    if str_from_binary_short_fields == '':
      valid_binary_short_fields = False
      
    if self.str_binary_full == '':
      valid_binary_full_field = False      
      
    if valid_binary_short_fields == False and valid_binary_full_field == False:
      self.post_message('no data in binary short fields or binary full field')
      return False      
    if self.binary_use_mode == 'use_binary_short_fields':
      if valid_binary_short_fields == True:
        self.update_entry_field('entry_binary_full_val',str_from_binary_short_fields)
        self.str_binary_full = str_from_binary_short_fields  
      else:        
        self.post_message('no data in binary short fields - using binary full field')  
      
    elif self.binary_use_mode == 'use_binary_full_field':
      if valid_binary_full_field == True:
        None
      else:
        self.post_message('no data in binary full field - using binary short fields')
        self.update_entry_field('entry_binary_full_val',str_from_binary_short_fields)
        self.str_binary_full = str_from_binary_short_fields      
    
    # match binary short fields to binary full field
    self.update_binary_short_fields()

    # post total length
    total_length = len(self.str_binary_full)
    if total_length > 0:
      self.update_entry_field('entry_total_length',total_length)
      
    if self.parse_mode == 'translate_then_parse':
      self.update_entry_field('entry_binary_partial',self.str_binary_full)    
    
    return True

  def validate_input(self,val,field_length,mode, element_index=0):
    if len(val) > int(field_length): # only allow 4 binary characters
      return False
      
    if len(val) == int(field_length): # move focus to next element
      if int(element_index) < self.num_binary_entry_fields - 1:
        exec('self.entry_binary_' + str(int(element_index) + 1) + '.focus_set()')        
    
    for i in range(len(val)):
      curr_char = val[i]
      match mode:
        case 'binary':
          match curr_char:
            case '0'|'1': # valid input
              None

            case _:
              return False
              
        case 'numeric':
          match curr_char:
            case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9': # valid input
              None

            case _:
              return False        
    return True # input validated

  def generate_parsing_rules(self):
    # get binary info
    if self.create_binary_string_successful()  == False:
      return
    if self.str_binary_full == '':
      return
  
    # verify decimal info
    if self.str_desired_decimal == '':
      return
      
    # check translate then parse rules
    self.indices_found = []
    self.val_decimal_full = self.binary_to_decimal(self.str_binary_full)
    self.str_decimal_full = str(self.val_decimal_full)
    for i in range(0,len(self.str_decimal_full)):
      new_str = self.str_decimal_full[i:] # substring after character position i 
      #print("new_str : " + new_str)
      index_match = new_str.find(self.str_desired_decimal) # search remaining characters of full decimal string for desired decimal
      #print("index_match : " + str(index_match))
      if index_match == -1: # no more occurences found
        break
      index_match = index_match + i + 1
      if not(index_match in self.indices_found):
        self.indices_found.append(index_match)
    
    for i in range (len(self.indices_found)):
      curr_element = self.indices_found[i]
      self.indices_found[i] = 'Starting position : ' + str(self.indices_found[i]) + '   Length : ' + str(len(self.str_desired_decimal))
    
    # update combobox with results
    self.cb_parsing_rules_translate_then_parse['values'] = self.indices_found
    if not(len(self.indices_found) > 0):
      self.cb_parsing_rules_translate_then_parse['values'] = ['no matching rules found']
    self.cb_parsing_rules_translate_then_parse.current(0)
      
    # check parse then translate rules
    self.rules_found = []
    for i in range(len(self.str_binary_full)):
      for j in range(i,len(self.str_binary_full)):
        curr_str_binary = self.str_binary_full[i:j+1]
        curr_val_decimal = self.binary_to_decimal(curr_str_binary)
        curr_length = j - i + 1
        curr_str_decimal = str(curr_val_decimal)
        if curr_str_decimal == self.str_desired_decimal:
          self.rules_found.append("Start position : " + str(i + 1) + "   Length : " + str(curr_length))
    
    self.cb_parsing_rules_parse_then_translate['values'] = self.rules_found
    if not(len(self.rules_found) > 0):
      self.cb_parsing_rules_parse_then_translate['values'] = ['no matching rules found']
    self.cb_parsing_rules_parse_then_translate.current(0)
    
  def toggle_tool_tips(self):
    if self.tool_tips_on == True:
      self.tool_tips_on = False
    else:
      self.tool_tips_on = True
    
    
  # action -----------------------------------------------------------------  
  def btn_action(self,str_action):
    self.clear_message()
    self.get_user_selections()
    match str_action:
      case 'binary_to_decimal':
        if self.parse_mode == 'parse_then_translate':
          self.parse_then_translate()
        else:
          self.translate_then_parse()

      case 'decimal_to_binary':
        self.decimal_to_binary()

      case 'clear_all_fields':
        self.clear_fields('all_fields')
          
      case 'generate_parsing_rules':
        self.clear_generated_parse_rules()
        self.generate_parsing_rules()
          
      case 'clear_bit_fields':
        self.clear_fields('bit_fields')
        
      case 'open_help_file':
        webbrowser.open('parse_badge_help.txt')
        
      case 'toggle_tool_tips':
        self.toggle_tool_tips()
      
      case 'exit':
        self.soft_exit()



  # GUI -----------------------------------------------------------------
  def clear_message(self):
    self.lbl_message_box.config(text='')

  def reset_all(self):
    self.clear_fields('all_fields')
    self.clear_message()
    self.clear_generated_parse_rules()
    
  def clear_fields(self,mode):
    match mode:
      case 'all_fields':
        self.update_entry_field('entry_binary_full_val','')
        self.update_entry_field('entry_binary_partial','')
        self.update_entry_field('entry_decimal_full','')
        self.update_entry_field('entry_start_position','')
        self.update_entry_field('entry_bit_length','')
        self.update_entry_field('entry_total_length','')
        self.update_entry_field('entry_binary_full_val','')
        self.update_entry_field('entry_decimal_partial','')
        self.update_entry_field('entry_desired_decimal','')
        for i in range(self.num_binary_entry_fields):
          exec('self.update_entry_field("entry_binary_' + str(i) + '","")')  
          
      case 'bit_fields':
        self.update_entry_field('entry_start_position','')
        self.update_entry_field('entry_bit_length','')
        self.update_entry_field('entry_total_length','')      
      
  def update_entry_field(self, field_name, val):
    #print("field_name : %s"%field_name)
    #print("val : %s"%val)
    exec('self.' + field_name + '.delete(0,END)')
    exec('self.' + field_name + '.insert(0,"' + str(val) + '")')

  def get_user_selections(self):
    self.str_binary_full = self.entry_binary_full_val.get()
    self.pos_start = self.entry_start_position.get()
    self.bit_length = self.entry_bit_length.get()
    self.str_decimal_full = self.entry_decimal_full.get()
    self.total_bit_length = self.entry_total_length.get()
    self.str_desired_decimal = self.entry_desired_decimal.get()

  def post_message(self,val):
    self.lbl_message_box.config(text=val)

  def clear_generated_parse_rules(self):
    self.cb_parsing_rules_translate_then_parse['values'] = []
    self.cb_parsing_rules_translate_then_parse.set('')
    self.cb_parsing_rules_parse_then_translate['values'] = []
    self.cb_parsing_rules_parse_then_translate.set('')
  
  def set_button_state(self,btn_name,val):
    if val == 0:
      cmd_str = 'self.' + btn_name + '.config(relief = RAISED,bg=self.color_btn_off)'
    else:
      cmd_str = 'self.' + btn_name + '.config(relief = SUNKEN,bg=self.color_btn_on)'
    exec(cmd_str)

  def create_tkinter_frame(self,parent_element, element_name, frame_width, frame_height, element_row, element_col, padx, pady,color='lightblue'):
    exec('self.' + element_name + ' = Frame(self.' + parent_element + ', width=' + str(frame_width) + ', height=' + str(frame_height) + ', padx = ' + str(padx) + ', pady = '  + str(padx) + ', bg="' + color
    + '")')
    exec('self.' + element_name + '.grid(row=' + str(element_row) + ', column = ' + str(element_col) + ')')
    if self.tkinter_frame_border_display == True:
      exec('self.' + element_name + '.config(highlightbackground="blue", highlightthickness=self.frame_border_width)')
    self.frame_row_count = self.frame_row_count + 1

  def create_tkinter_label(self, parent_element, element_name, element_text, element_row, element_col, padx, pady,color='lightblue'):
    exec('self.' + element_name + ' = tk.Label(self. ' + parent_element + ', text="' + element_text + '",bg="' + color + '")')
    exec('self.' + element_name + '.grid(row=' + str(element_row) + ', column=' + str(element_col) + ')')

  def create_tkinter_entry(self, parent_element, element_name, element_row, element_col, entry_width, padx, pady,color='lightblue'):
    exec('self.' + element_name + ' = tk.Entry(self. ' + parent_element + ', width=' + str(entry_width) + ',bg="' + color + '")')
    exec('self.' + element_name + '.grid(row=' + str(element_row) + ', column=' + str(element_col) + ')')
  
  def create_window(self):
    self.window = tk.Tk()
    #self.window.config(bg=self.color_blue_4)
    self.window.config(bg='lightblue')
    self.window.title('parse_badge')
    #self.window.overrideredirect(True) #hides title bar
    #self.window.wm_attributes('-fullscreen', 'True')
    
    self.menu_bar = Menu(self.window)
    self.menu_file = Menu(self.menu_bar, tearoff=0)
    self.menu_bar.add_cascade(label="File", menu=self.menu_file)
    self.menu_file.add_command(label="Exit", command=self.soft_exit)
    
    self.menu_help = Menu(self.menu_bar, tearoff=0)
    self.menu_bar.add_cascade(label="Help", menu=self.menu_help)
    self.menu_help.add_command(label="Help file", command=lambda : self.btn_action('open_help_file'))   
    #self.menu_help.add_checkbutton(label="app tips", command=lambda : self.btn_action('toggle_tool_tips'))

    self.menu_options = Menu(self.menu_bar, tearoff=0)
    self.menu_bar.add_cascade(label="Options", menu=self.menu_options)
    self.menu_options.add_command(label="Reset all to default", command=self.reset_all)       
    

    # create tkinter frames

    self.create_tkinter_frame('window','frame_binary',200,400,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady)
    #self.frame_binary.config(highlightbackground="blue", highlightthickness=self.frame_border_width)

    self.create_tkinter_frame('frame_binary','frame_binary_row_0',200,100,0,0,self.tk_default_padx,self.tk_default_pady)
    self.create_tkinter_frame('frame_binary','frame_binary_row_1',200,100,1,0,self.tk_default_padx,self.tk_default_pady)
    self.create_tkinter_frame('frame_binary','frame_binary_row_2',200,100,2,0,self.tk_default_padx,self.tk_default_pady)
    self.create_tkinter_frame('frame_binary','frame_binary_row_3',200,100,3,0,self.tk_default_padx,self.tk_default_pady,self.color_bit_option_elements)
    self.frame_binary_row_3.config(highlightbackground="blue", highlightthickness=self.frame_border_width)
    
    self.create_tkinter_frame('frame_binary_row_0','frame_binary_short',200,50,0,1,self.tk_default_padx,self.tk_default_pady)

    #self.create_tkinter_frame('frame_binary_row_3','frame_bit_entries',200,50,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady)
    #self.frame_bit_entries.config(highlightbackground="blue", highlightthickness=self.frame_border_width)
    
    self.create_tkinter_frame('window','frame_decimal',200,50,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady)
    

    self.create_tkinter_frame('window','frame_parse_mode',200,50,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady)

    self.create_tkinter_frame('window','frame_binary_mode',200,50,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady)

    self.create_tkinter_frame('window','frame_action_btns',200,50,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady)
    #self.frame_action_btns.config(highlightbackground="blue", highlightthickness=2)
    
    self.create_tkinter_frame('window','frame_generate_parsing_rules',200,50,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady,self.color_generate_elements)
    self.frame_generate_parsing_rules.config(highlightbackground="blue", highlightthickness=self.frame_border_width)
    
    self.create_tkinter_frame('frame_generate_parsing_rules','frame_generate_parsing_rules_entry',200,50,0,0,self.tk_default_padx,self.tk_default_pady,self.color_generate_elements)
    
    self.create_tkinter_frame('frame_generate_parsing_rules','frame_valid_rules_title',200,50,1,0,self.tk_default_padx,self.tk_default_pady,self.color_generate_elements)
    
    self.create_tkinter_frame('frame_generate_parsing_rules','frame_valid_rules_results',200,50,2,0,self.tk_default_padx,self.tk_default_pady,self.color_generate_elements)

    self.create_tkinter_frame('window','frame_message',200,50,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady)

    self.create_tkinter_frame('window','frame_move_window',200,50,self.frame_row_count,0,self.tk_default_padx,self.tk_default_pady)


    #self.window.resizable(0,0)
    #self.window.attributes("-alpha", 0.8) #transparency setting
    #self.window.overrideredirect(True) # hide window controls
    #self.window.iconbitmap("ico.ico") # window icon
    #photo = tk.PhotoImage(file = 'ico.png') # window icon
    #self.window.wm_iconphoto(False, photo) # window icon

    self.defaultFont = font.nametofont("TkDefaultFont")
    self.defaultFont.configure(size=8)





    # binary fields --------------------------------------------------------
    self.create_tkinter_label('frame_binary_row_0','lbl_binary_short','binary short form entry',0,0,self.tk_default_padx,self.tk_default_pady)
    #self.lbl_binary_short = tk.Label(self.frame_binary_row_0, text="binary short form entry")
    #self.lbl_binary_short.grid(row=0, column=0, padx=5, pady=5)
    #self.lbl_running_timer.pack()

    for i in range(self.num_binary_entry_fields):
      #exec('validate_input_wrapper' + str(i) + ' = (self.window.register(self.validate_input), "%P",4)') # for tkinter validation'
      validate_input_wrapper = self.window.register(self.validate_input), "%P",4,'binary',i # for tkinter validation'
      #exec('bin_num' + str(i) + ' = StringVar()')
      bin_num = StringVar()
      #exec('self.entry_binary_' + str(i) + ' = tk.Entry(self.frame_binary_short, width=4, textvariable=bin_num' + str(i) + ', validate="key", validatecommand=validate_input_wrapper' + str(i) + ') ')
      exec('self.entry_binary_' + str(i) + ' = tk.Entry(self.frame_binary_short, width=4, textvariable=bin_num, validate="key", validatecommand=validate_input_wrapper)')
      exec('self.entry_binary_' + str(i) + '.grid(row=0, column=' + str(i) + ')')

    # full binary
    self.create_tkinter_label('frame_binary_row_1','lbl_binary_full_title','full binary',0,0,self.tk_default_padx,self.tk_default_pady)
    validate_input_wrapper = self.window.register(self.validate_input),"%P",60,'binary'
    bin_num = StringVar()    
    self.entry_binary_full_val = tk.Entry(self.frame_binary_row_1, width=60, textvariable=bin_num, validate = "key", validatecommand = validate_input_wrapper)
    self.entry_binary_full_val.grid(row=0, column = 1)
    #self.create_tkinter_entry('frame_binary_row_1','entry_binary_full_val',0,1,60,self.tk_default_padx,self.tk_default_pady)

    # parsed binary
    self.create_tkinter_label('frame_binary_row_2','lbl_binary_parsed_title','parsed binary',0,0,self.tk_default_padx,self.tk_default_pady)
    validate_input_wrapper = self.window.register(self.validate_input),"%P",60,'binary'
    bin_num = StringVar()        
    self.entry_binary_partial = tk.Entry(self.frame_binary_row_2, width=60, textvariable=bin_num, validate = "key", validatecommand = validate_input_wrapper)
    self.entry_binary_partial.grid(row=0, column = 1)    
    #self.create_tkinter_entry('frame_binary_row_2','entry_binary_partial',0,1,60,self.tk_default_padx,self.tk_default_pady)

    # full decimal  
    self.create_tkinter_label('frame_decimal','lbl_decimal_full','full decimal',0,0,self.tk_default_padx,self.tk_default_pady)
    validate_input_wrapper = self.window.register(self.validate_input),"%P",15,'numeric'
    bin_num = StringVar()         
    self.entry_decimal_full = tk.Entry(self.frame_decimal, width=15, textvariable=bin_num, validate = "key", validatecommand = validate_input_wrapper)
    self.entry_decimal_full.grid(row=0, column = 1)      
    #self.create_tkinter_entry('frame_decimal','entry_decimal_full',0,1,15,self.tk_default_padx,self.tk_default_pady)

    # partial decimal
    self.create_tkinter_label('frame_decimal','lbl_decimal_partial','partial decimal',1,0,self.tk_default_padx,self.tk_default_pady)
    validate_input_wrapper = self.window.register(self.validate_input),"%P",15,'numeric'
    bin_num = StringVar()         
    self.entry_decimal_partial = tk.Entry(self.frame_decimal, width=15, textvariable=bin_num, validate = "key", validatecommand = validate_input_wrapper)
    self.entry_decimal_partial.grid(row=1, column = 1)       
    #self.create_tkinter_entry('frame_decimal','entry_decimal_partial',1,1,15,self.tk_default_padx,self.tk_default_pady)    

    # start bit
    self.create_tkinter_label('frame_binary_row_3','lbl_start_position','parse start position',0,0,self.tk_default_padx,self.tk_default_pady)
    validate_input_wrapper = self.window.register(self.validate_input),"%P",4,'numeric'
    bin_num = StringVar()         
    self.entry_start_position = tk.Entry(self.frame_binary_row_3, width=4, textvariable=bin_num, validate = "key", validatecommand = validate_input_wrapper)
    self.entry_start_position.grid(row=0, column = 1)       
    #self.create_tkinter_entry('frame_binary_row_3','entry_start_position',0,1,4,self.tk_default_padx,self.tk_default_pady)

    # length
    self.create_tkinter_label('frame_binary_row_3','lbl_length','parse length',0,2,self.tk_default_padx,self.tk_default_pady)
    validate_input_wrapper = self.window.register(self.validate_input),"%P",4,'numeric'
    bin_num = StringVar()         
    self.entry_bit_length = tk.Entry(self.frame_binary_row_3, width=4, textvariable=bin_num, validate = "key", validatecommand = validate_input_wrapper)
    self.entry_bit_length.grid(row=0, column = 3)    
    #self.create_tkinter_entry('frame_binary_row_3','entry_bit_length',0,3,4,self.tk_default_padx,self.tk_default_pady)

    # total length
    self.create_tkinter_label('frame_binary_row_3','lbl_total_length','total binary bit length',0,4,self.tk_default_padx,self.tk_default_pady)
    validate_input_wrapper = self.window.register(self.validate_input),"%P",4,'numeric'
    bin_num = StringVar()         
    self.entry_total_length = tk.Entry(self.frame_binary_row_3, width=4, textvariable=bin_num, validate = "key", validatecommand = validate_input_wrapper)
    self.entry_total_length.grid(row=0, column = 5)    
    #self.create_tkinter_entry('frame_binary_row_3','entry_total_length',0,5,4,self.tk_default_padx,self.tk_default_pady)

    # clear entry fields button
    self.btn_clear_bit_fields = tk.Button(self.frame_binary_row_3,text="clear fields", command=lambda : self.btn_action('clear_bit_fields'))
    self.btn_clear_bit_fields.grid(row=0, column = 6)
    
    

    # mode buttons --------------------------------------------------------
    # mode button - parse then translate
    self.btn_mode_parse_then_translate = tk.Button(self.frame_parse_mode,text="parse then translate", command=lambda : self.set_mode('parse_then_translate'))
    self.btn_mode_parse_then_translate.grid(row=0, column = 0)
    #self.btn_mode_parse_then_translate.pack()

    # mode button - translate then parse
    self.btn_mode_translate_then_parse = tk.Button(self.frame_parse_mode,text="translate then parse", command=lambda : self.set_mode('translate_then_parse'))
    self.btn_mode_translate_then_parse.grid(row=0, column = 1)
    #self.btn_mode_translate_then_parse.pack()

    # mode button - use binary 4 character fields
    self.btn_mode_binary_short_fields = tk.Button(self.frame_binary_mode, text="use binary short fields", command=lambda : self.set_mode('use_binary_short_fields'))
    self.btn_mode_binary_short_fields.grid(row=0, column = 0)
    #self.btn_mode_binary_short_fields.pack()

    # mode button - use binary full
    self.btn_mode_binary_full_field = tk.Button(self.frame_binary_mode, text="use full binary field", command=lambda : self.set_mode('use_binary_full_field'))
    self.btn_mode_binary_full_field.grid(row=0, column = 1)
    #self.btn_mode_binary_full_field.pack()


    # action buttons --------------------------------------------------------
    # action button binary to decimal
    self.btn_binary_to_decimal = tk.Button(self.frame_action_btns,text="binary to decimal", command=lambda : self.btn_action('binary_to_decimal'))
    self.btn_binary_to_decimal.grid(row=0, column = 0)
    #self.btn_binary_to_decimal.pack()

    # action button decimal to binary
    self.btn_dec_to_binary = tk.Button(self.frame_action_btns,text="decimal to binary", command=lambda : self.btn_action('decimal_to_binary'))
    self.btn_dec_to_binary.grid(row=0, column = 1)
    #self.btn_dec_to_binary.pack()

    # character replacement
    #self.lbl_replace_char = tk.Label(text = 'character replacement').pack()
    #self.entry_replace_char = tk.Entry(width=4)
    #self.entry_replace_char.pack()

    # clear all entry fields button
    self.btn_exit = tk.Button(self.frame_action_btns,text="clear all fields", command=lambda : self.btn_action('clear_all_fields'))
    self.btn_exit.grid(row=0, column = 4)

    # exit button
    self.btn_exit = tk.Button(self.frame_action_btns,text="exit", command=lambda : self.btn_action('exit'))
    self.btn_exit.grid(row=0, column = 5)
    #self.btn_exit.pack()




    # generate parsing rules --------------------------------------------------------
    # desired decimal
    self.create_tkinter_label('frame_generate_parsing_rules_entry','lbl_desired_decimal','desired decimal',0,0,self.tk_default_padx,self.tk_default_pady)
    validate_input_wrapper = self.window.register(self.validate_input),"%P",15,'numeric'
    bin_num = StringVar()         
    self.entry_desired_decimal = tk.Entry(self.frame_generate_parsing_rules_entry, width=15, textvariable=bin_num, validate = "key", validatecommand = validate_input_wrapper)
    self.entry_desired_decimal.grid(row=0, column = 1)         
    #self.create_tkinter_entry('frame_generate_parsing_rules_entry','entry_desired_decimal',0,1,15,self.tk_default_padx,self.tk_default_pady)    

    # action button generate parsing rules
    self.btn_gen_parse_rules = tk.Button(self.frame_generate_parsing_rules_entry,text="generate parsing rules", command=lambda : self.btn_action('generate_parsing_rules'))
    self.btn_gen_parse_rules.grid(row=0, column = 2)
    #self.btn_gen_parse_rules.pack()

    # clear generated parsing rules
    self.btn_clear_parse_rules = tk.Button(self.frame_generate_parsing_rules_entry,text="clear parsing rules", command=lambda : self.clear_generated_parse_rules())
    self.btn_clear_parse_rules.grid(row=0, column = 3)
    
    # generated parsing rules title
    self.create_tkinter_label('frame_valid_rules_title','lbl_title_generated_parsing_rules','valid rules',1,0,self.tk_default_padx,self.tk_default_pady)
    
    # generated parsing rules translate then parse
    self.create_tkinter_label('frame_valid_rules_results','lbl_valid_parsing_rules_translate_then_parse','translate then parse',0,0,self.tk_default_padx,self.tk_default_pady)
    self.cb_parsing_rules_translate_then_parse = ttk.Combobox(self.frame_valid_rules_results, width = 80, state="readonly")
    self.cb_parsing_rules_translate_then_parse.grid(row=0, column = 1)
    
    # generated parsing rules parse then translate 
    self.create_tkinter_label('frame_valid_rules_results','lbl_valid_parsing_rules_parse_then_translate','parse then translate',1,0,self.tk_default_padx,self.tk_default_pady)
    self.cb_parsing_rules_parse_then_translate = ttk.Combobox(self.frame_valid_rules_results, width = 80, state="readonly")
    self.cb_parsing_rules_parse_then_translate.grid(row=1, column = 1)    


    
    
    
    # message box --------------------------------------------------------
    # message box
    self.lbl_message_box = tk.Label(self.frame_message, text = '', bg='lightblue')
    self.lbl_message_box.grid(row=0, column = 0)
    #self.lbl_message_box.pack()



    # move window --------------------------------------------------------
    # move window grip
    self.grip = tk.Label(self.frame_move_window, bitmap="gray25")
    self.grip.grid(row=0,column=0)
    #self.grip.pack(side="right")
    self.grip.bind("<ButtonPress-1>", self.start_move)
    self.grip.bind("<ButtonRelease-1>", self.stop_move)
    self.grip.bind("<B1-Motion>", self.do_move)

    # initialize button states
    self.set_mode('parse_then_translate')
    self.set_mode('use_binary_short_fields')
    
    self.window.config(menu=self.menu_bar)
    
    self.window.mainloop()


  #  move window -----------------------------------------------------------------
  def start_move(self, event): # move window left click mouse down
    self.x = event.x
    self.y = event.y

  def stop_move(self, event): # move window left click mouse up
    self.x = None
    self.y = None

  def do_move(self, event): # move window left click drag
    deltax = event.x - self.x
    deltay = event.y - self.y
    x = self.window.winfo_x() + deltax
    y = self.window.winfo_y() + deltay
    self.window.geometry(f"+{x}+{y}")

  def set_mode(self,val):
    if self.app_initialized == True:
      match val:
        case 'parse_then_translate':
          self.parse_mode = val
          self.set_button_state('btn_mode_parse_then_translate',1)
          self.set_button_state('btn_mode_translate_then_parse',0)
        case 'translate_then_parse':
          self.parse_mode = val
          self.set_button_state('btn_mode_parse_then_translate',0)
          self.set_button_state('btn_mode_translate_then_parse',1)
        case 'use_binary_short_fields':
          self.binary_use_mode = val
          self.set_button_state('btn_mode_binary_full_field',0)
          self.set_button_state('btn_mode_binary_short_fields',1)
        case 'use_binary_full_field':
          self.binary_use_mode = val
          self.set_button_state('btn_mode_binary_full_field',1)
          self.set_button_state('btn_mode_binary_short_fields',0)



  # application -----------------------------------------------------------------
  def soft_exit(self):
    self.write_to_log_file('exit btn pressed')
    self.file_write.close()
    self.window.destroy()
    self.window.quit()
  


# instantiate class/application
cl = parse_badge()