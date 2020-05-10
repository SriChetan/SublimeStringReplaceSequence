import sublime
import sublime_plugin
import json
import re

class CreateReplaceSequenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0,self.view.size())
        viewStr = self.view.substr(region)
        jsonStr = json.loads(viewStr)
        name = jsonStr["name"]
        respFile = open(sublime.packages_path() + "/StringReplace/" + name + ".py", "w+")
        respFile.write("import sublime\n")
        respFile.write("import sublime_plugin\n")
        respFile.write("import re\n")
        respFile.write("\n")
        
        respFile.write("class " + jsonStr["name"] + "Command(sublime_plugin.TextCommand):\n")
        respFile.write("    def run(self, edit):\n")
        respFile.write("        region = sublime.Region(0,self.view.size())\n")
        respFile.write("        viewStr = self.view.substr(region)\n")
        i = 0
        for comd in jsonStr["commands"]:
            respFile.write('        finalStr' + str(i) + ' = ""\n')
            if i == 0:
                respFile.write('        for line in viewStr.split("\\n"):\n')
            else:
                respFile.write('        for line in finalStr' + str(i - 1)+ '.split("\\n"):\n')
            
            respFile.write('            line = line + "\\n"\n')
            respFile.write('            finalStr' + str(i) + ' = finalStr' + str(i) + ' + re.sub("' + comd["Find"] + '", "' + comd["Replace"] + '", line)\n')
            i += 1
            print(i)
        
        
        respFile.write('        self.view.replace(edit, region, finalStr' + str(i - 1) + ')\n')
        respFile.close()
        
        name = re.sub('([A-Z]{1})', r'_\1', name).lower()
        comdName = name[1: len(name)] if name.startswith('_') else name
        
        comdFileName = sublime.packages_path() + "/StringReplace/" + "Default.sublime-commands"
        comdFile = open(comdFileName, "r")
        
        contents = comdFile.readlines()
        comdFile.close()
        contents = "".join(contents)
        
        if comdName not in contents:
            comdToAdd = ',\n    { \n' + '        "caption": "String Replace: ' + re.sub('_', ' ', comdName) + '",\n'
            comdToAdd = comdToAdd + '        "command": "' + comdName + '"\n    }\n]'
            contents = contents.replace("\n]", comdToAdd)
            comdFile = open(comdFileName, "w")
            comdFile.write(contents)
            comdFile.close()
        
        