import pyperclip
#path_source = input("path to source file")

words_to_not_add = ['and','the','yes','no','for','enable','disable','minutes','hours','active']
str_build = ''

def is_in_do_not_add_list(curr_text):
  is_in_list = False
  for i in range(0,len(words_to_not_add)):
    if curr_text.lower() == words_to_not_add[i].lower():
      is_in_list = True
      break
  return is_in_list
  
  

def main():
  last_run = False
  path_source_base = r"C:\Users\jhall\OneDrive - TIMECLOCK PLUS, LLC\Utilities\parse_page\\"
  path_source = path_source_base + 'UserProfiles_Permissions.txt'
  
  #path_source = path_source + '.html'
  
  file_source = open(path_source,"r", encoding='utf8')

  continue_file_read_lines = True
  curr_line_num = 0
  
  tree_level = 0
  tree_level_prev = 0
  
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
        last_run = True
        tree_level = 0
        curr_txt = ''
        
      if last_run == False:
        #get tree level
        tree_level = 0
        for i in range(0,len(curr_line)):
          curr_char = curr_line[i]
          if curr_char != '\t': # see if curr char is not a tab
            break
          else:
            tree_level = tree_level + 1
            
        #print("tree_level : ", tree_level,"  :  ",curr_line)
        
        curr_txt = curr_line.replace('\t','')
        curr_txt = curr_txt.replace('\r','')
        curr_txt = curr_txt.replace('\n','')
        curr_txt = curr_txt.replace("'",'')
        #print(curr_txt)
      
      tree_level_diff = tree_level - tree_level_prev
      #print("tree_level_diff : " , tree_level_diff)
      if curr_line_num == 1:
        str_build = "[" + curr_txt
      elif tree_level_diff == 0:
        str_build = str_build + ", \\" + "\n" + '  ' * tree_level + '"' + curr_txt + '"'
      elif tree_level_diff > 0:
        str_build = str_build + ", \\"  + "\n" + '  ' * tree_level + '[' + '"' + curr_txt + '"'
      elif tree_level_diff < 0:
        for i in range(tree_level + abs(tree_level_diff),tree_level,-1):
          str_build = str_build + " \\" + "\n" + '  ' * i + "]"
          if last_run == False:
            str_build = str_build + ","
        if last_run == False:
          str_build = str_build + "\n" + '  ' * tree_level + '"' + curr_txt + '"'
        else:
          str_build = str_build + "\n" + '  ' * tree_level + "]"
      tree_level_prev = tree_level
      
    if last_run == True:
      break
    
  print(str_build)
      
  create_file = input("file name  (blank = do not write to file): ")
  if create_file != '':
    try:
      f = open(create_file + '.txt', "x")
    except: 
      overwrite = input("overwrite file? (y/n) : ")
      if overwrite == 'y' or overwrite == 'Y':
        f = open(create_file + '.txt', "w")  
        f.write(str_build)
    else:
      f.write(str_build)

      
main()



