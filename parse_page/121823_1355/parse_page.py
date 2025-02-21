from html.parser import HTMLParser
#path_source = input("path to source file")



def main():
  path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\landing_page.html"
  #path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\company_defaults.html"
  #path_source = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\employee_profiles.html"
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
      if curr_line.find('</header>') != -1:  
        #break
        None
      # get page title
      if page_title == "":
      
        search_text = '<span class="FeatureTitle ng-binding" ng-show="blnShouldShowFeatureHeading">'
        curr_text = get_html_line_text(curr_line, search_text, '<')
        #print(curr_text)
        if curr_text != "not found":
          page_title = curr_text
          print("page_title : " + page_title + "\n")
      # get page title


       
      # parse page menu
      pos_menuitem = curr_line.find('role="menuitem"')
      pos_arialabel = curr_line.find('aria-label=')
      pos_li_open = curr_line.find('<li ')
      pos_li_close = curr_line.find('</li>')    
      
      if pos_li_open != -1:
        num_li_open = num_li_open + 1
      if pos_li_close != -1:
        num_li_open = num_li_open - 1
        
      # see if menu item is on line  
      reg_exp = ""  # test next line with regex to deal with true/false
      search_text = 'role="menuitem" aria-haspopup="false" aria-current="true" aria-label="'
      curr_text = get_html_line_text(curr_line, search_text, '"')
      str_build = ""
      if curr_text != "not found":
        str_build = curr_text
        print("str_build : " + str_build)
          
          
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
    print(str_to_search)
    pos_start = pos_start + len(str_to_locate)
    pos_end = str_to_search.find(delimiting_char, pos_start)
    if pos_end != -1:
      html_text = str_to_search[pos_start:pos_end]
      #print("html_text : " + html_text )
  
  return html_text

            #<span class="FeatureTitle ng-binding" ng-show="blnShouldShowFeatureHeading">Employee Profiles</span>



# start
main_run = main()
# start




# menu item
#<li ng-repeat="objSubMenuItem in objMenuRootItem.arrMenuItems" id="ManageEmployee" role="menuitem" aria-haspopup="false" aria-current="true" aria-label="Employee Profiles" ng-click="objSubMenuItem.hasMenuItems() ? return : showTooltip(); handleHeaderMenuItem(getHeaderMenu(), objSubMenuItem); $event.stopPropagation();" ng-show="getHeaderMenu().isMenuItemSelected(objMenuRootItem)" class="ng-scope" tabindex="-1"

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
