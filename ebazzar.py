from easygui import*
import sys
 
while 1:
 msgbox("welcome to ebazaar")

 msg="choose the section"
 title="shopping choices"
 choices=["electronics","clothes","footwear"]
 choice=choicebox(msg,title,choices)
 msgbox("you choose:"+str(choice))

 if choice=="electronics":
    msg="choose ur electronic gadget"
    title="electronic choices"
    choices1=["mobile","dryer"]
    choice=choicebox(msg,title,choices)
    msgbox("you chose"+str(choice1))



   if choice1=="mobile":
      msg="choose ur mobile"
      title="mobiles"
      choices11=["samsung a6 15,000";"SAMSUNG J6 12000";"REDME 18000"]
      choice=choicebox(msb,title,choices)
      msgbox("you chose"+str(choice11))


   elif choice1=="dryer":
      msg="choose ur dryer"
      title="dryers"
      choices12=["hp dryer 15,000";"godrej 5000";"elle 3000"]
      choice=choicebox(msb,title,choices)
      msgbox("you chose"+str(choice12))



 elif choice=="clothes":
    msg="choose clothes"
    title="clothes choices"
    choice2=["shirts","jeans"]
    choices=choicebox(msg,title,choices)
    msgbox("you chose"+str(choice2))


   
   if choice2=="shirts":
      msg="choose ur shirt"
      title="shirts"
      choices21=["lee 5000";"vermoda 4000";"you 8000"]
      choice=choicebox(msb,title,choices)
      msgbox("you chose"+str(choice21))


   elif choice2=="jeans":
      msg="choose ur jeans"
      title="jeans"
      choices22=["denim 15,000";"jeolous 5000";"leec 8000"]
      choice=choicebox(msb,title,choices)
      msgbox("you chose"+str(choice22))



 elif choice=="footwear":
    msg="choose footwear"
    title="footwear choices"
    choice3=["shoes","sandals"]
    choices=choicebox(msg,title,choices)
    msgbox("you chose"+str(choice3))

   
  if choice3=="shoes":
     msg="choose ur shoes"
     title="shoes"
     choices31=["adidas 5000";"nike 4000";"bata 8000"]
     choice=choicebox(msb,title,choices)
     msgbox("you chose"+str(choice32))
  elif choice3=="sandals":
     msg="choose ur sandals"
     title="sandals"
     choices32=["retro 15,000";"metro 5000";"bata 8000"]
     choice=choicebox(msg,title,choices)
     msgbox("you chose"+str(choice32))

msg="do u want to continue"
title="confirmation box"
choice=ccbox(msg,title)
if choice==1:
 exit(0)
elif choice==0:
 msgbox("u have chosen to continue")