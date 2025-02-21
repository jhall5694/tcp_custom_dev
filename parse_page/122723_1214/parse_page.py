from html.parser import HTMLParser
import re # regex
#path_source = input("path to source file")



def main():
  path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\landing_page.html"
  path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\company_defaults.html"
  path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\employee_profiles.html"
  file_source = open(path_source,"r", encoding='utf8')

  num_li_open = 0
  num_li_open_prev = 0

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
  
  while continue_file_read_lines == True:
    try:
      curr_line_num = curr_line_num + 1
      #print(curr_line_num)
      curr_line = file_source.readline()
    except:
      #print("exception reading line : " + str(curr_line_num))
      #raise
      break
    else:
      # check if in a new section, branch, etc
      
      # check if in a new section, branch, etc
      
      # have standard menu already loaded
      # then determine:
      # page_title
      # specific employee, job code, etc (list on left)
      # tab
      # branch
      # label
      
      
      
      # <span class="ButtonContent" ng-click="openPopup()" aria-label="jason hall flyout, press enter to open, escape to close and tab keys to navigate">
      search_text = '<span class="ButtonContent" ng-click="openPopup()" aria-label="'
      pos_start = curr_line.find(search_text)
      pos_end = curr_line.find(' flyout, press enter to open, escape to close and tab keys to navigate">')
      if pos_start != -1 and pos_end != -1:
        curr_list_selection = curr_line[pos_start + len(search_text):pos_end]   
        #print(curr_list_selection)
      
      
      # curr_tab   
      #search_text = '<span tcp-bind-html-unsafe="menuRoot.strMenuText | formatNewLine">'
      search_text = '<li class="menuRoot ng-scope HasMenus Selected" ng-repeat="menuRoot in getMenu().arrMenuItems track by $index" role="menuitem" ng-show="menuRoot.strMenuText" aria-haspopup="true" aria-label="'
      curr_text = get_html_line_text(curr_line, search_text, '"')
      if curr_text != "not found":
        curr_tab = curr_text
        #print("curr_tab : " + curr_tab + "\n")
      # curr_tab  
        
      if curr_tab != "":
        # curr_branch  
        search_text = '<div class="Title ng-binding" ng-click="toggleOpen()" tabindex="0">'
        curr_text = get_html_line_text(curr_line, search_text, '<')
        if curr_text != "not found":
          curr_branch = curr_text
          if curr_branch != prev_branch:
            prev_branch = curr_branch
            curr_legend = ""
            ary_ary_tab_branches.append([curr_branch]) # start new array to hold next branch/labels          
            continue
            #print("curr_branch : " + curr_branch + "\n" + "curr_line_num : " + str(curr_line_num) + "\n")   
          # curr_branch
        
        if curr_branch != "":
          # curr_legend
          search_text = '<legend'
          curr_text = get_html_line_text(curr_line, search_text, '<')
          if curr_text != "not found":
            pos_start = curr_text.find('>')
            if pos_start != -1:
              curr_legend = curr_text[pos_start + 1:len(curr_text)]
              continue
          # curr_legend
          
          ary_curr_line_text = text_between_angle_brackets(curr_line)
          
          # curr_label
          #search_text = '<td class="Label ng-binding" ng-bind='
          #print("search_text : " + search_text)
          #curr_text = get_html_line_text(curr_line, search_text, '<')
          #print("curr_text : " + curr_text + "\n")
          #if ary_curr_line_text[0] != "":
            
            #print("curr_line : " + curr_line)
            #pos_start = curr_text.find('>')
            #if pos_start != -1:
              #print("curr_text : " + curr_text)
              #curr_label = curr_text[pos_start + 1:len(curr_text)]
              #print("\n")
              #print("curr_tab : " + curr_tab + "\n")
              #print("curr_branch : " + curr_branch + "\n")
              #print("curr_label : " + curr_label + "\n")   
              
              #print(curr_label)
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
      pos_li_open = curr_line.find('<li ')
      pos_li_close = curr_line.find('</li>')    
        
        
      # see if menu item is on line  
      search_text = 'role="menuitem" aria-haspopup="false" aria-current="true" aria-label="'
      curr_text = get_html_line_text(curr_line, search_text, '"')
      str_build = ""
      if curr_text != "not found":
        str_build = curr_text
        #print("str_build : " + str_build)
          
        if pos_li_open != -1:
          num_li_open = num_li_open + 1
        if pos_li_close != -1:
          num_li_open = num_li_open - 1        
          
        '''
        if pos_menuitem != -1 and pos_arialabel != -1:
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
          ary_main_menu.append([str_build])
          #print(ary_main_menu[len(ary_main_menu)- 1])
        if num_li_open == 2:
          #None
          ary_indx = len(ary_main_menu)-1
          ary_main_menu[ary_indx].append([str_build])
        if num_li_open == 3:
          #None
          ary_indx_1 = len(ary_main_menu)-1         
          curr_ary = ary_main_menu[ary_indx_1]
          ary_indx_2 = len(curr_ary) - 1
          ary_main_menu[ary_indx_1][ary_indx_2].append([str_build])        
        # parse page menu
      
  #print (ary_main_menu)
  print(ary_ary_tab_branches)
  
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

def get_tags_and_text(str_to_search):
  curr_tag = ""
  curr_text = ""
  in_tag = False
  in_text = False
  
  for i in range(0,len(str_to_search)):
    curr_char = str_to_search[i]
    #print(str_to_search[1:i])
    match(curr_char):
      case '<':
        in_tag = True
        curr_tag = "" 
        if in_text == True:
          in_text = False
          curr_text = curr_text.strip()
          if curr_text != "":
            print("text : " + curr_text)
          curr_text = ""        
        
      case '>':
        in_text = True
        curr_text = ""
        if in_tag == True:
          in_tag = False
          curr_tag = curr_tag.strip()
          if curr_tag != "":
            print("tag : " + curr_tag)
          curr_tag = ""        
        
      case ' ':
        if in_tag == True:
          in_tag = False
          curr_tag = curr_tag.strip()
          if curr_tag != "":
            print("tag : " + curr_tag)
          curr_tag = ""        

        if in_text == True:
          curr_text = curr_text + curr_char
          
      case '/':
        if in_tag == True:
          in_tag = False
          curr_tag = ""
        
      case _:
        if in_tag == True:
          curr_tag = curr_tag + curr_char
        if in_text == True:
          curr_text = curr_text + curr_char


#test_mode = True
test_mode = False
if test_mode == True:
  str_to_search = '              <yo>    asdfasdf  <span ng-bind="getCompanyConfig().strDefaultCostCode" class="ng-binding">Default Cost Code</span><span></span><legend></legend> '
  curr_tag = ""
  curr_text = ""
  in_tag = False
  in_text = False
  
  for i in range(0,len(str_to_search)):
    curr_char = str_to_search[i]
    #print(str_to_search[1:i])
    match(curr_char):
      case '<':
        in_tag = True
        curr_tag = "" 
        if in_text == True:
          in_text = False
          curr_text = curr_text.strip()
          if curr_text != "":
            print("text : " + curr_text)
          curr_text = ""        
        
      case '>':
        in_text = True
        curr_text = ""
        if in_tag == True:
          in_tag = False
          curr_tag = curr_tag.strip()
          if curr_tag != "":
            print("tag : " + curr_tag)
          curr_tag = ""        
        
      case ' ':
        if in_tag == True:
          in_tag = False
          curr_tag = curr_tag.strip()
          if curr_tag != "":
            print("tag : " + curr_tag)
          curr_tag = ""        

        if in_text == True:
          curr_text = curr_text + curr_char
          
      case '/':
        if in_tag == True:
          in_tag = False
          curr_tag = ""
        
      case _:
        if in_tag == True:
          curr_tag = curr_tag + curr_char
        if in_text == True:
          curr_text = curr_text + curr_char
          
        
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
