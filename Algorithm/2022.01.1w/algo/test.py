s=input()
smile=s.count(":-)")
sad=s.count(":-(")
if smile==0 and sad==0: print("none")
elif smile>sad: print("happy")
elif smile==sad: print("unsure")
elif smile<sad: print("sad")