#make a 5 word dictionary for user so that after giving input they can get the meaning if the word

dict={"Abnegation":"Renouncing a belief or doctrine","Beguile":"influence someone in a deceptive way",
      "Cognizant":"awareness or realization","Embezzlement":"misappropriation of funds",
      "Fatuous":"devoid of intelligence"}
dictinput = input("give any words for the given 5 words to know their meaning[Abnegation],[Beguile],[Cognizant],"
                  "[Embezzlement],[Fatuous]")
print(dict[dictinput])

