sequence1 = (input ("plak hier de 1ste sequentie"))
sequence2= (input ("plak hier de 2de sequentie"))
sequence1atgc = (sequence1.count(""))
sequence1gc = sequence1.count("G")+sequence1.count("C")
gc1percentage = sequence1gc/sequence1atgc*100
sequence2atgc = (sequence2.count(""))
sequence2gc = sequence2.count("G")+sequence2.count("C")
gc2percentage = sequence2gc/sequence2atgc*100
print ("zoveel nucleotiden 1ste sequentie:", sequence1atgc)
print ("gc percentage 1ste sequentie:", gc1percentage)
print ("zoveel nucleotiden 2de sequentie:", sequence2atgc)
print ("gc percentage 2de sequentie:", gc2percentage)

