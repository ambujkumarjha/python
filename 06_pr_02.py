# write a python program to fill in a letter template given below with name and date 
#letter = ''' dear <|Name|>,
 #            you are slected !
  #           <|date|> '''
letter =  ''' dear  <|Name|>,
             greetings from google . I  am proud to tell you about your selection 
             you are slected at the head of google india.
             have a great day.
              thanks ands regards .
              sunder pichai
               <|date|> 
               '''
name =   input (" Enter your name\n")
date  =  input("Enter date\n ")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|date|>", date)
print(letter)