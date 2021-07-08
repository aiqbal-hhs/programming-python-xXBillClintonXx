#Variables
score = 0

#Title
print("Rise and Fall of The Roman Empire Quiz")
print("---")
#Instructions
print('!!!IMPORTANT!!! \n To answer questions simply type in the letter that corellates to an answer (e.g. "a" for a not "a.")')
print("---")
#Who was the last dictator of the Roman Republic?
answer1 = input("1. Who was the last dictator of the Roman Republic? \n a. Julius Caesar \n b. Marcus Krassus \n c. Mark Antony \n d. Pompey \n Enter Answer Here:")
if answer1 == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("After defeating his enemies Marcus Crassus and Pompey in a bloody civil war Caesar declared himself dictator for life, much to the annoyance of the Roman Senate")
print("---")
#On what day was Caesar assassinated?
answer2 = input("2. On what day was Julius Caesar assassinated? \n a. December 26 \n b. April 20 \n c. March 15 \n d. July 1 \n Enter Answer Here:")
if answer2 == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print('Julius Caesar was assassinated by over 60 conspirators on March 15, 44 BC (also known as the Ides of March). Caesars last words are said to have been "Et tu, Brute" in reference to senator Marcus Junius Brutus who has since been suggested as a possible illegitemate child of Caesar, altough many modern historians dispute this fact')
print("---")
#Who was the first emperor of Rome?
answer3 = input("3. Who was the first emperor of the Roman Empire? \n a. Remus \n b. Spartacus \n c. Romulus \n d. Octavian \n Enter Answer Here:")
if answer3 == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("Due to the fact that Caesar had no legitamite children, he named his favourite relative Gaius Octavius as his heir. Octavian was Caesars grand nephew and used the wealth and estates he accquired to defeat all his political opponents and name himself the first emperor of Rome. Ironically, by killing Caesar for being a dictator the senate had indirectly paved the way for Octavian to become emperor. Upon ascendence to the throne Octavian renamed himself as Augustus.")
print("---")
#What year was the Roman Empire founded?
answer4 = input("4. What year was the Roman Empire founded? \n a. 0 AD \n b. 200 BC \n c. 27 BC \n d. 50 AD \n Enter Answer Here:")
if answer4 == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("In 27 BC Octavian was rewarded the title of princeps (first citizen in Latin) effectively making him de-facto ruler of Rome. While the senate still existed the only held ceremonial powers at this point. The empire was further solidified with Augustus named his step-son Tiberius as the heir to the Roman throne.")
print("---")
#What was the first capital of the Roman Empire?
answer5 = input("5. What was the first capital of the Roman Empire? \n a. Rome \n b. Naples \n c. Venice \n d. Athens \n Enter Answer Here:")
if answer5 == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("Rome was the founding city of the Roman Republic and the Roman Empire. According to ancient Roman tradition Rome was founded by brothers Romulus and Remus in the year 753 BC. Contrary to popular belief Rome was not always the capital of the Roman Empire and it moved around three times.")
print("---")
#Which of the following is NOT considered one of the Five Good Emperors?
answer6 = input("6. Which of the following is not one of the “Five Good Emperors”? \n a. Marcus Aurelius \n b. Nerva \n c. Trajan \n d. Diocletian \n e. Antoninus Pius \n f. Hadrian \n Enter Answer Here:")
if answer6 == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("The five good emperors are called the five good emperors as under their rule Rome went through years of great prosperity and overall piece throughout the empire. The five good emperors started with Nerva and ended with Marcus Aurelius. Nearly all of the emperors were adopted rather than recieving the throne through hereditary means. In Rome adoption was considered just as strong as familial bonds and as such adoptees were in line for the throne. Diocletian was a low-born slave who would go on to become the Roman Emperor and following his death the Roman Empire would be split into two distincitve parts.")
print("---")
#What is the Eastern Roman Empire referred to as in modern times?)
answer7 = input("7. What is the Eastern Roman Empire referred to as in modern times? \n a. Byzantine Empire \n b. Ottoman Empire \n c. Hellenic League \n d. Outremer Empire \n Enter Answer Here:")
if answer7 == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("While it was called the Eastern Roman Empire in it own time modern historians prefer to refer to it as the Byzantine Empire due to the fact that it didn't control Rome and its culture had become distinct than that of Rome by the time of its fall. Byzantium was the first capital of the Eastern Roman Empire but it was renamed following the Christianization of the Empire following Emperor Constantines rule.")
print("---")
#What was the capital of the Byzantine Empire called?
answer8 = input("8. What was the capital of the Eastern Roman Empire? \n a. Athens \n b. Constantinople \n c. Thessaloniki \n d. Rhodes \n Enter Answer Here:")
if answer8 == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("Byzantium was renamed to Constantinople after Emperor Constantine when he decided to move the capital there. Constantine considered Constantinople to be at an important strategic location at the center of the Bosphorus at wanted to covert the city into his Nova Roma (New Rome).")
print("---")
#Where is Constantinople today?
answer9 = input("9. Where is Constantinople today? \n a. Troy \n b. Venice \n c. Jerusalem \n d. Istanbul \n Enter Answer Here:")
if answer9 == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("After the Turkish War for independence the new Turkish capital was moved to Istanbul. Istanbul had long been a part of the Ottoman Empire following the Byzantines fall and was an important town in the empire. The name was officially changed to Istanbul in 1930. Istanbul comes from the term that Greek speakers had referred to the city since its fall to the Ottomans.")
print("---")
#When did Rome fall?
answer10 = input("10. What year did the Western Roman Empire fall? \n a. 196 AD \n b. 52 BC \n c. 476 AD \n d. 1000 AD \n Enter Answer Here:")
if answer10 == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("After many years of attacks from warlords such as Atilla the Hun, Rome finally fell when Odoacer deposed child emperor Romulus Augustus and established his kingdom. It was undeniable that after nearly 500 years the Western Roman Empire had fallen.")
print("---")
#What year did the Eastern Roman Empire fall?
answer11 = input("11. What year did the Eastern Roman Empire fall? \n a. 1453 AD \n b. 1822 AD \n c. 3 BC \n d. 476 AD \n Enter Answer Here:")
if answer11 == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("The Eastern Roman Empire finally ceased to exist following the capitals fall to the Ottomans in 1453 AD. The fall of Constantinpole is considered by many modern historians to be the end of the medieval era. The last Eastern Roman Emperor Constantine XI perished in the final siege of the city by leading the last of his soldiers to face the vastly superior enemy forces head on, becoming a legendary figure in late Greek history.")
print("---")
#Where is modern day rome located?
answer12 = input("12. Where is modern day Rome located? \n a. Andorra \n b. Italy \n c. Germany \n d. France \n Enter Answer Here:")
if answer12 == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("Rome is the Capital City of Italy and is one of the most visited tourist destinations in the world. The current population of Rome (2021) is around 4.2 Million.")
print("---")
#Summary
if score <= 5:
    print("Congratulations, you have a score of {}, the Roman Empire awards you the title of Plebian. Ave, True to Rome!" .format(score))
elif score <=11:
    print("Congratulations, you have a score of {}, the Roman Empire awards you the title of Senator. Ave, True to Rome!" .format(score))
elif score == 12:
    print("Congratulations, you have a score of {}, the Roman Empire awards you the title of Imperator. Ave, True to Rome!" .format(score))
    
