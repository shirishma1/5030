class LowerCaseConversion():
   
    def lowercase(self,text): # if there are no specific conditions this method is used
        return text.lower()
        
    def Irish(self,text):
        lc = ""
        vowels = ['A','E','I','O','U','Á','É','Í','Ó','Ú']
        if(len(text)>=2 and (text[0] == 'n' or text[0] == 't')):
            if text[1] in vowels:
                lc = text[0]+'-'+text[1:].lower()
        else:
             lc+=text.lower()
        return lc    
   
    def Greek(self,text):
        lc = ""
        if(text[-1] == 'Σ'):
            lc+=text[0:-1].lower()+'ς'
        else:
            lc+=text.lower()
        return lc  
    def Turkish(self,text):
         lc = ""
         tr_dict = {'I':'ı', 'İ':'i'}
         for letter in text:
            if letter == 'I' or letter == 'İ':
                lc += tr_dict[letter]
            else:
                lc += letter.lower()
         return lc  
   
             
def Choose_Lang(text,lang_code):
    Lang_Codes = ['en', 'th', 'en-US', 'zh-Hans', 'en-Latn', 'en-IE']
    if(lang_code in  Lang_Codes ):
        return obj.lowercase(text)
    elif lang_code == 'ga' or lang_code == 'ga-IE':
        return obj.Irish(text)
    elif lang_code == 'el':
        return obj.Greek(text) 
    elif lang_code == 'tr' or lang_code == 'az' :
        return obj.Turkish(text)
    
    else:
        return 'invalid language code'
Word = input()
Language_Code = input()
obj = LowerCaseConversion()
LC_Text = Choose_Lang(Word,Language_Code)
print("{}".format(LC_Text))