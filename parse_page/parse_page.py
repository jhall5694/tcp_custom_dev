from html.parser import HTMLParser
import pyperclip
import re # regex
#path_source = input("path to source file")

words_to_not_add = ['and','the','yes','no','for','enable','disable','minutes','hours','active']

def str_from_list(ary, str_path, level, level_prev, prev_element_type): # build formatted string from list
  #print(ary)
  #print(str_path)
  #print("A1")
  for i in range(0,len(ary)):
    #print("A2 : " + str(i))
    # determine what level of branching element is at
    curr_element = ary[i]
    #print("curr element")
    #print(curr_element)
    #print("\n \n")
    add_element = False
    

    #if prev_element_type == 'string': # recursion called this - meaning iteration is now in a new list / level up
      

    if isinstance(curr_element,str):
      add_element = True
      if prev_element_type == 'list':
        level = level - 1
      
      prev_element_type = 'string'
    else:
      if prev_element_type == 'string':
        level = level + 1
      str_path = str_from_list(curr_element, str_path, level, level_prev, prev_element_type) # recursion
      prev_element_type = 'list'            
      
    if add_element == True:
      #print("level : " , level , "   \n level_prev : " , level_prev , "   \n level_prev : " , level_prev )
      # build string 
      curr_element    = curr_element.replace('"','""')
      curr_element    = curr_element.replace('“','""')
      if level == 1:
        if level_prev == 0:
          #print("here")
          str_path = str_path + '  ["' + curr_element + '"'
        elif level_prev == 1:
          #print("here1")
          str_path = str_path + ', \\' + '\n' + '  "' + curr_element + '"'
        elif level_prev == 2:
          #print("here3")
          str_path = str_path + '\n    ], \\' + '\n' + '  "' + curr_element + '"'            
        elif level_prev == 3:
          #print("here3")
          str_path = str_path + '\n      ]\n    ], \\' + '\n' + '  "' + curr_element + '"'                        
        level_prev = 1
        #print(ary_main_menu[len(ary_main_menu)- 1])
      if level == 2:
        if level_prev == 1:
          #print("here4")
          str_path = str_path + ', \\' + '\n    ["' + curr_element + '"'
        elif level_prev == 2:
          #print("here5")
          str_path = str_path + ', \\' +  '\n    "' + curr_element + '"'
        elif level_prev == 3:
          #print("here6")
          str_path = str_path + '\n      ], \\' +  '\n    "' + curr_element + '"'
        level_prev = 2
      if level == 3:
        if level_prev == 2:
          #print("here7")
          str_path = str_path + ', \\' +  '\n      ["' + curr_element + '"'
        elif level_prev == 3:
          #print("here8")
          str_path = str_path + ', \\' +  '\n      "' + curr_element + '"'
        level_prev = 3
          
    if i == len(ary) - 1: # last element in current list
      str_path = str_path + ' \\\n' + '  ' * level + ']' 
      level = level - 1  
      #if level != 1:
        #str_path = str_path + '\\'
        #None
          
  return str_path    

def is_in_do_not_add_list(curr_text):
  is_in_list = False
  for i in range(0,len(words_to_not_add)):
    if curr_text.lower() == words_to_not_add[i].lower():
      is_in_list = True
      break
  return is_in_list
  
  

def main():
  path_source_base = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\\"
  #path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\landing_page.html"
  #path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\company_defaults.html"
  #path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\employee_profiles.html"
  
  #
  #path_source = path_source + '\employee_roles_information'
  path_source = path_source_base + 'employee_roles_information'
  path_source = path_source_base + 'employee_roles_jobs'
  path_source = path_source_base + 'employee_profiles_jobs'
  path_source = path_source_base + 'job_codes_general'
  path_source = path_source_base + 'user_profiles_permissions'
  path_source = path_source_base + 'employee_profiles_payroll'
  path_source = path_source_base + 'employee_profiles_access'
  path_source = path_source_base + 'employee_profiles_overtime'
  path_source = path_source + '.html'
  
  file_source = open(path_source,"r", encoding='utf8')

  num_li_open = 0
  num_li_open_prev = 0
  count_li = False
  str_main_menu = ''

  continue_file_read_lines = True
  curr_line_num = 0

  ary_main_menu = []

  page_title = ""
  #page_title = "User Delegation"
  #page_title = "Mass Hours"
  #page_title = "Swaps"
  #page_title = input("search term ->    ")
  
  search_label = ""
  search_label = "Export code"
  search_label = "default job code"
  search_label = "scheduled job code"
  search_label = "assign"
  
  curr_tab = ""
  curr_branch = ""
  prev_branch = ""
  curr_legend = ""
  curr_legend_prev = ""
  curr_label = ""
  ary_ary_tab_branches = []
  
  branch_div_count = 0
  in_branch = False
  
  grid_div_count = 0
  in_grid = False
  
  while continue_file_read_lines == True:
    try:
      curr_line_num = curr_line_num + 1
      #print(curr_line_num)
      curr_line = file_source.readline()
    except:
      print("exception reading line : " + str(curr_line_num))
      raise
      break
    else:
      if not curr_line:
        break
    
      # list selection
      # <span class="ButtonContent" ng-click="openPopup()" aria-label="jason hall flyout, press enter to open, escape to close and tab keys to navigate">
      search_text = '<span class="ButtonContent" ng-click="openPopup()" aria-label="'
      pos_start = curr_line.find(search_text)
      pos_end = curr_line.find(' flyout, press enter to open, escape to close and tab keys to navigate">')
      if pos_start != -1 and pos_end != -1:
        curr_list_selection = curr_line[pos_start + len(search_text):pos_end]   
        #print(curr_list_selection)
      # list selection
      
      
      
      # curr_tab   
      #search_text = '<span tcp-bind-html-unsafe="menuRoot.strMenuText | formatNewLine">'
      search_text = '<li class="menuRoot ng-scope HasMenus Selected" ng-repeat="menuRoot in getMenu().arrMenuItems track by $index" role="menuitem" ng-show="menuRoot.strMenuText" aria-haspopup="true" aria-label="'
      curr_text = get_html_line_text(curr_line, search_text, '"')
      if curr_text != "not found" and not(is_in_do_not_add_list(curr_text)):
        curr_tab = curr_text
        ary_ary_tab_branches.append(curr_tab)
        ary_ary_tab_branches.append([])
        #print(ary_ary_tab_branches)
        #print("curr_tab : " + curr_tab + "\n")
      # curr_tab  
        
        
      
      if curr_tab != "":
        # branch outside div count
        if branch_div_count > 0:
          branch_divs_open_on_line = re.findall(r'<div[^\s]?', curr_line) 
          branch_divs_close_on_line = re.findall(r'</div[^\s]?', curr_line)
          branch_div_count = branch_div_count + len(branch_divs_open_on_line) - len(branch_divs_close_on_line)            
          if branch_div_count <= 0:
            branch_div_count = 0
            in_branch = False
            curr_branch = ""
            #print("branch_div_count : " + str(branch_div_count) + "   line : " + str(curr_line_num))
          #print("branch_div_count : " + str(branch_div_count))
            
        pos_branch_open_div = re.search(r'<div class=".*Collapsible', curr_line)  #curr_line.find('<div class="Collapsible')
        #print(pos_branch_open_div, "  :  ", curr_line_num)
        if not(pos_branch_open_div is None):
          pos_branch_open_div = pos_branch_open_div.start()
          #print(curr_line)
          in_branch = True
          branch_divs_open_on_line = re.findall(r'<div[^\s]?', curr_line[pos_branch_open_div:]) 
          branch_divs_close_on_line = re.findall(r'</div[^\s]?', curr_line[pos_branch_open_div:])
          branch_div_count = len(branch_divs_open_on_line) - len(branch_divs_close_on_line)
          #print("branch_div_count : " + str(branch_div_count))
        # branch outside div count
        
        # grid outside div count - don't include labels within grid/table
        if grid_div_count > 0:
          grid_divs_open_on_line = re.findall(r'<div[^\s]?', curr_line) 
          grid_divs_close_on_line = re.findall(r'</div[^\s]?', curr_line)
          grid_div_count = grid_div_count + len(grid_divs_open_on_line) - len(grid_divs_close_on_line)            
          if grid_div_count <= 0:
            grid_div_count = 0
            in_grid = False
            curr_grid = ""
            #print("grid_div_count : " + str(grid_div_count) + "   line : " + str(curr_line_num))
          #print("grid_div_count : " + str(grid_div_count))
            
        pos_grid_open_div = curr_line.find('<div class="GridContainer"')
        if pos_grid_open_div != -1:
          in_grid = True
          grid_divs_open_on_line = re.findall(r'<div[^\s]?', curr_line[pos_grid_open_div:]) 
          grid_divs_close_on_line = re.findall(r'</div[^\s]?', curr_line[pos_grid_open_div:])
          grid_div_count = len(grid_divs_open_on_line) - len(grid_divs_close_on_line)
          #print("grid_div_count : " + str(grid_div_count))
        # grid outside div count - don't include labels within grid/table
      
        # curr_branch  - only include labels inside a branch
        search_text = '<div class="Title ng-binding" ng-click="toggleOpen()" tabindex="0">'
        curr_text = get_html_line_text(curr_line, search_text, '<')
        if curr_text != "not found" and in_branch == True and not(is_in_do_not_add_list(curr_text)):
          #print(curr_text)
          curr_branch = curr_text
          if curr_branch != prev_branch:
            prev_branch = curr_branch
            curr_legend = ""
            ary_ary_tab_branches[1].append(curr_branch) # start new array to hold next branch/labels          
            #print(ary_ary_tab_branches)
            #print("\n")
            continue
            #print("curr_branch : " + curr_branch + "\n" + "curr_line_num : " + str(curr_line_num) + "\n")   
        
        if curr_branch != "":
        
          # curr_legend
          search_text = '<legend'
          curr_text = get_html_line_text(curr_line, search_text, '<')
          if curr_text != "not found" and not(is_in_do_not_add_list(curr_text)):
            pos_start = curr_text.find('>')
            if pos_start != -1:
              curr_legend = curr_text[pos_start + 1:len(curr_text)]
              continue
          # curr_legend
          
          curr_tag = ""
          curr_full_tag = ""
          curr_text = ""
          in_tag = False
          capturing_tag = False
          in_text = False
          
          for i in range(0,len(curr_line)):
            curr_char = curr_line[i]
            match(curr_char):
              case '<':
                in_tag = True
                capturing_tag = True
                
                if in_text == True:
                  in_text = False
                  curr_text = curr_text.strip()
                  if curr_text != "" and not(is_in_do_not_add_list(curr_text)):
                    match curr_tag:
                      case "span"|"label"|"td":
                        if curr_full_tag.find('display:none') == -1 and in_grid == False:
                          curr_indx = len(ary_ary_tab_branches[1]) - 1
                          if isinstance(ary_ary_tab_branches[1][curr_indx],str):
                            ary_ary_tab_branches[1].append([curr_text])
                          else:
                            ary_ary_tab_branches[1][curr_indx].append(curr_text) # append new label                      
                          #print("curr_line_num : " + str(curr_line_num) + "  tag : " + curr_tag + "   text : " + curr_text) 
                          str_build =  "curr_line_num : " + str(curr_line_num)
                          str_build = str_build + "  -  "  + page_title
                          if curr_list_selection != "":
                            str_build = str_build + " > (selected list item : " + curr_list_selection + ")"
                            
                          str_build = str_build + " > " + curr_tab + " > " + curr_branch 
                          
                          if curr_legend != "":
                            str_build = str_build + " > " + curr_legend
                            
                          str_build = str_build  + " > " + curr_text
                            
                          #print(str_build)
                      case _:
                        None
                        #print("curr_line_num : " + str(curr_line_num) + "  tag : " + curr_tag + "   text : " + curr_text)                            
                curr_tag = ""
                
              case '>':
                in_text = True
                if in_tag == True:
                  in_tag = False
                  curr_full_tag = curr_full_tag.strip()
                if capturing_tag == True:
                  capturing_tag = False
                  curr_tag = curr_tag.strip()
                curr_text = ""
                
              case ' ':
                if capturing_tag == True:
                  capturing_tag = False
                  curr_tag = curr_tag.strip()    

                if in_text == True:
                  curr_text = curr_text + curr_char
                  
              case '/':
                if capturing_tag == True:
                  capturing_tag = False
                
              case _:
                if in_tag == True:
                  curr_full_tag = curr_full_tag + curr_char
                if capturing_tag == True:
                  curr_tag = curr_tag + curr_char                  
                if in_text == True:
                  curr_text = curr_text + curr_char



          '''
          #ary_curr_line_text = text_between_angle_brackets(curr_line)
          for ary_element in ary_curr_line_text:              
            #print(type(ary_element))
            #print(ary_element + " : " + str(len(ary_element)))
            curr_indx = len(ary_ary_tab_branches) - 1
            ary_ary_tab_branches[curr_indx].append(ary_element) # append new label
            
            if ary_element.lower().find(search_label.lower()) != -1:
              str_build = page_title
              if curr_list_selection != "":
                str_build = str_build + " > (selected list item : " + curr_list_selection + ")"
                
              str_build = str_build + " > " + curr_tab + " > " + curr_branch 
              
              if curr_legend != "":
                str_build = str_build + " > " + curr_legend
                
              str_build = str_build  + " > " + ary_element
                
              print(str_build)
              break
                
          # curr_label  
          '''
      
      
      if curr_line.find('</header>') != -1:  
        #break
        None
      # get page title
      if page_title == "":
      
        search_text = '<span class="FeatureTitle ng-binding" ng-show="blnShouldShowFeatureHeading">'
        curr_text = get_html_line_text(curr_line, search_text, '<')
        if curr_text != "not found":
          page_title = curr_text
          #print("page_title : " + page_title + "\n")
      # get page title


      
      # parse page menu
      pos_menuitem = curr_line.find('role="menuitem"')
      pos_arialabel = curr_line.find('aria-label=')
      ary_li_open = re.findall(r'<li',curr_line)
      ary_li_close = re.findall(r'</li',curr_line)
        
      if count_li == True:
        if num_li_open == 0:
          if num_li_open_prev == 1:
            str_main_menu = str_main_menu + '\n  ]' +  '\n]'
          elif num_li_open_prev == 2:
            str_main_menu = str_main_menu + '\n    ]' +  '\n  ]' +  '\n]'
          elif num_li_open_prev == 3:
            str_main_menu = str_main_menu + '\n      ]' + '\n    ]' + '\n  ]' +  '\n]'
          count_li = False
        if len(ary_li_open) > 0:
          num_li_open = num_li_open + len(ary_li_open)
        if len(ary_li_close) > 0:
          num_li_open = num_li_open - len(ary_li_close)
          

                    
      # see if menu item is on line  
      #search_text = 'role="menuitem" aria-haspopup="false" aria-current="true" aria-label="'

      reg_exp = r'role="menuitem".+aria-haspopup=".+".+aria-current=".+".+aria-label="'
      menu_items_on_line = re.findall(reg_exp,curr_line) 
      curr_text = "not found"
      if len(menu_items_on_line) > 0:
        curr_text = get_html_line_text(curr_line, menu_items_on_line[0], '"')    
      #branch_divs_open_on_line = re.findall(r'<div[^\s]?', curr_line)
      #curr_text = get_html_line_text(curr_line, search_text, '"')
      str_build = ""
      if curr_text != "not found":
        str_build = curr_text
        #print("str_build : " + str_build)

        if num_li_open == 0:
          num_li_open = len(ary_li_open)
          count_li = True
          str_main_menu = '["Settings", \\\n'
        if count_li == True:
          if num_li_open == 0:
            count_li = False        

          
          '''   
          #print("num_li_open : " + str(num_li_open))
          cl = True
          curr_index = pos_arialabel + 12
          str_build = ""
          #str_build = "| " * (1 * (num_li_open - 1))
          while cl == True:
            curr_char = curr_line[curr_index]
            if curr_char != '"':
              str_build = str_build + curr_char  
            else:            
              #input("")
              cl = False
            curr_index = curr_index + 1
          '''      

        if num_li_open == 1:
          if num_li_open_prev == 0:
            str_main_menu = str_main_menu + '  ["' + str_build + '"'
          elif num_li_open_prev == 1:
            str_main_menu = str_main_menu + ', \\' + '\n' + '  "' + str_build + '"'
          elif num_li_open_prev == 2:
            str_main_menu = str_main_menu + '\n    ], \\' + '\n' + '  "' + str_build + '"'            
          elif num_li_open_prev == 3:
            str_main_menu = str_main_menu + '\n      ]\n    ], \\' + '\n' + '  "' + str_build + '"'                        
          ary_main_menu.append([str_build])
          num_li_open_prev = 1
          #print(ary_main_menu[len(ary_main_menu)- 1])
        if num_li_open == 2:
          if num_li_open_prev == 1:
            ary_main_menu.append([str_build])
            str_main_menu = str_main_menu + ', \\' + '\n    ["' + str_build + '"'
          elif num_li_open_prev == 2:
            ary_indx = len(ary_main_menu) - 1
            ary_main_menu[ary_indx].append(str_build)
            str_main_menu = str_main_menu + ', \\' +  '\n    "' + str_build + '"'
          elif num_li_open_prev == 3:
            ary_indx_1 = len(ary_main_menu) - 1
            curr_ary = ary_main_menu[ary_indx_1]
            ary_indx_2 = len(curr_ary) - 1
            ary_main_menu[ary_indx_1].append(str_build)
            str_main_menu = str_main_menu + '\n      ], \\' +  '\n    "' + str_build + '"'
          num_li_open_prev = 2
        if num_li_open == 3:
          if num_li_open_prev == 2:
            ary_indx = len(ary_main_menu) - 1
            curr_ary = ary_main_menu[ary_indx]
            ary_main_menu[ary_indx].append([str_build])
            str_main_menu = str_main_menu + ', \\' +  '\n      ["' + str_build + '"'
          elif num_li_open_prev == 3:
            ary_indx_1 = len(ary_main_menu) - 1
            curr_ary = ary_main_menu[ary_indx_1]
            ary_indx_2 = len(curr_ary) - 1
            ary_main_menu[ary_indx_1][ary_indx_2].append(str_build)
            str_main_menu = str_main_menu + ', \\' +  '\n      "' + str_build + '"'
          num_li_open_prev = 3

        #print(ary_main_menu)
   

  str_path = ''
  level = 1
  level_prev = 0
  prev_element_type = ''
  #print(ary_ary_tab_branches)
  final_str = str_from_list(ary_ary_tab_branches, str_path, level, level_prev, prev_element_type)  
  print(final_str," \n \n")
  curr_str = page_title +  "_" +  curr_tab
  curr_str = curr_str.replace(' ','')
  curr_str = curr_str.replace(' ','')
  command=pyperclip.copy(curr_str)
  create_file = input("file name  (blank = do not write to file): ")
  if create_file != '':
    try:
      f = open(create_file + '.txt', "x")
    except: 
      overwrite = input("overwrite file? (y/n) : ")
      if overwrite == 'y' or overwrite == 'Y':
        f = open(create_file + '.txt', "w")  
        f.write(final_str)
    else:
      f.write(final_str)
    #None
    
    #print(ary_tab_branches)
    #print("\n")
  
  # determine path to page from main menu
  itr_1 = -1
  itr_2 = -1
  itr_3 = -1
  itr_4 = -1
  for m in ary_main_menu:
    itr_1 = itr_1 + 1
    itr_2 = -1
    itr_3 = -1
    itr_4 = -1  
    if m ==  page_title:
      None
      #print("found 1 : " + m)
    for mm in m:
      itr_2 = itr_2 + 1
      itr_3 = -1
      itr_4 = -1      
      if mm ==  page_title:
        None
        #print("itr_1 : " , itr_1)
        #print(ary_main_menu[itr_1][0])
      for mmm in mm:
        itr_3 = itr_3 + 1
        itr_4 = -1
        if mmm ==  page_title:
          None
          #print("itr_1 : " , itr_1 , "itr_2 : " , itr_2)
          #print(ary_main_menu[itr_1][0]," > ", ary_main_menu[itr_1][itr_2][0])
        for mmmm in mmm:
          itr_4 = itr_4 + 1
          if mmmm ==  page_title:
            None
            #print("itr_1 : " , itr_1 , "itr_2 : " , itr_2 , "itr_3 : " , itr_3)
            #print(ary_main_menu[itr_1][0]," > ", ary_main_menu[itr_1][itr_2][0]," > ", ary_main_menu[itr_1][itr_2][itr_3][0])
  # determine path to page from main menu
      
  #print(ary_main_menu)      
    #<div class="Title ng-binding" ng-click="toggleOpen()" tabindex="0">Display Options</div></div><div ng-show="shouldExpand()" class="Body" ng-transclude="">
    #<span class="FeatureTitle ng-binding" ng-show="blnShouldShowFeatureHeading">Company Defaults</span>
    #<nav class="MenuFeatureOption Menu HasMenus" ng-class="{HasMenus: hasMenuItems()}" aria-label="Global" menu="config.objFeatureMenu">
    #<li ng-repeat="item in menuRoot.arrMenuItems" aria-label="Display Options"
    #<label ng-bind="objDisplayOptionsConfig.strCompanyName" class="ng-binding">Company Name</label>
  
def get_html_line_text(str_to_search, str_to_locate,delimiting_char):
  html_text = "not found"
  pos_start = str_to_search.find(str_to_locate)
  if pos_start != -1:
    #print("str_to_locate : " + str_to_locate)
    #print("str_to_search : " + str_to_search)
    pos_start = pos_start + len(str_to_locate)
    pos_end = str_to_search.find(delimiting_char, pos_start)
    if pos_end != -1:
      html_text = str_to_search[pos_start:pos_end]
      #print("html_text : " + html_text )
  
  return html_text

def text_between_angle_brackets(str_to_search):

  # 
  #reg_exp = r'.*?\[>.*<].*'
  #reg_exp = r'>{1}[\w]+<{1}'
  reg_exp = r'>{1}[^<^>]+<{1}'
  ary_results = re.findall(reg_exp, str_to_search)
  ary_itr = 0
  for val in ary_results:
    
    ary_results[ary_itr] = val[1:len(val) - 1]
    #print(ary_results[ary_itr])  
    ary_itr = ary_itr + 1
  
  #print(ary_results)  
  return ary_results

#test_mode = True
test_mode = False
if test_mode == True:
  str_to_search = '<div class="Heading"><span class="CollapseStateBG FeatherIcons chevron-down" ng-click="toggleOpen()" ng-class="getCollapseStateIcon()"></span><div class="Title ng-binding" ng-click="toggleOpen()" tabindex="0">Sub Assignment Templates</div></div><div ng-show="shouldExpand()" class="Body ng-hide" ng-transclude="">'
  branch_divs_open_on_line = re.findall(r'<div[^\s]?', str_to_search) 
  #print(branch_divs_open_on_line)
  branch_divs_close_on_line = re.findall(r'</div[^\s]?', str_to_search)
  #print(branch_divs_close_on_line)
  branch_div_count = len(branch_divs_open_on_line) - len(branch_divs_close_on_line)
  #print(branch_div_count)
        
else:
  main_run = main()



# have standard menu already loaded
# then determine:
# page
# specific employee, job code, etc (list on left)
# tab
# branch
# label


# menu item
#<li ng-repeat="objSubMenuItem in objMenuRootItem.arrMenuItems" id="ManageEmployee" role="menuitem" aria-haspopup="false" aria-current="true" aria-label="Employee Profiles" ng-click="objSubMenuItem.hasMenuItems() ? return : showTooltip(); handleHeaderMenuItem(getHeaderMenu(), objSubMenuItem); $event.stopPropagation();" ng-show="getHeaderMenu().isMenuItemSelected(objMenuRootItem)" class="ng-scope" tabindex="-1"

# list on left
#<tcp-navigation-list entities-collection="config.getEntitiesForGrid

# selected employee/job code etc
# <td ng-repeat="fncEvaluator in fncGetStaticFieldEvaluators()" ng-bind="getData(objEntity, fncEvaluator)" class="ng-binding ng-scope" tabindex="0">test emp</td>
# <td class="Value StandardRightSpacer" tcp-bind-default-empty="objSelected...................>data<

# information tab
# <span tcp-bind-html-unsafe="menuRoot.strMenuText | formatNewLine">Information</span> 

# personal branch
# <div class="Title ng-binding" ng-click="toggleOpen()" tabindex="0">Personal</div>

# First name field label
# <td class="Label ng-binding" ng-bind="getAppConfig().strFirstName">First name</td>

# Gender Dropdown
# <select ng-model="objSelectedEmployee.intGender" ng-options="gender.intKey as gender.strText for gender in config.arrIntStringItemGenderItems" ng-disabled="!config.blnCanEditGender" class="ng-pristine ng-valid ng-not-empty ng-touched"><option label="Male" value="number:1">Male</option><option label="Female" value="number:0">Female</option><option label="Other" value="number:3">Other</option><option label="<< Unspecified >>" value="number:2" selected="selected">&lt;&lt; Unspecified &gt;&gt;</option></select>

'''
# radio button and label - Company > Work Status
<div>
  <input class="TcpRadio ng-pristine ng-untouched ng-valid ng-not-empty" type="radio" id="rdoFullTime" ng-model="objSelectedEmployee.objEmployeeCompanyContext.intWorkStatus" ng-value="objSelectedEmployee.objEmployeeCompanyContext.intFullTime" label="objSelectedEmployee.objEmployeeCompanyContext.strFullTime" ng-disabled="!objSelectedEmployee.objEmployeeCompanyContext.blnCanEdit" name="46640" value="2">
  <label class="TcpRadioLabel ng-binding" for="rdoFullTime" ng-bind="objSelectedEmployee.objEmployeeCompanyContext.strFullTime" ng-disabled="!objSelectedEmployee.objEmployeeCompanyContext.blnCanEdit">
    Full time
  </label> 
  </div>
'''

'''
suspended checkbox and label
<div class="ng-scope">
  <input class="TcpCheckbox ng-empty ng-valid" type="checkbox" id="chkIsSuspended" label="config.strSuspended" ng-model="objSelectedEmployee.blnIsSuspended" ng-disabled="!config.blnCanEditSuspended" ng-show="config.blnCanViewSuspended">
    <label class="TcpCheckboxLabel tcp-btn ng-binding ng-scope" ng-bind="config.strSuspended" for="chkIsSuspended" ng-show="config.blnCanViewSuspended" ng-disabled="!config.blnCanEditSuspended">
    Suspended
    </label>
</div>
'''


# Other > Password label
# <legend ng-bind="getAppConfig().strPassword" class="ng-binding ng-scope">Password</legend>

# fieldset ng-transclude


'''
['Information', \
  ['Personal', \
    ['ID', 'First name', 'Last name', 'Address', 'City', 'State', 'Zip', 'Gender', 'DOB', 'SSN', 'Language', 'Cell', 'Phone', 'Office Phone', 'ext', 'Email', 'SMS Address'], \
  'Company', \
    ['Override role settings', 'Role ID', 'Description', 'Active', 'Classification', 'Department', 'Default Location', 'Schedule Group', 'None', 'Full time', 'Part time', 'Seniority Date', 'Hire date', 'Export code', 'Import ID', 'Termination', 'Suspended'], \
  'Role History', 
  'Other', \
    ['Network ID', 'LDAP User Name', 'Badge', 'PIN Status', 'PIN is not set', 'New PIN', 'Re-Enter PIN', 'Password Status', 'Password is not blank', 'New Password', 'Re-Enter Password', 'Employee must change password every', 'Days', 'SubSearch Plus account email', 'NA'], \
  'Qualifications', \
    ['Active only']
  ]
]
'''