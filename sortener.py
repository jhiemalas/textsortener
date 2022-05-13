
""" This is my first project in python """
""" created by: Jhiem Alas """
""" date created: January 11, 2022 """
""" modified May 5, 2022 | version 2.0 """
""" THIS PROGRAM LET YOU SORT TEXT CONTENT OF YOUR TEXT FILE ALPHABETHICALLY """



import string






print("\n\n\n")
print("        SSSSSS    HHHHH    RRRRRR    TTTTTTT   EEEEEEE   NN    N   EEEEEEE   RRRRRR")
print("       SS        H     H   R     R      T      EE        N N   N   EE        R     R")
print("         SSSS    H     H   RRRRRR       T      EEEEEEE   N  N  N   EEEEEEE   RRRRRR")
print("            SS   H     H   R    R       T      EE        N   N N   EE        R    R")
print("       SSSSSS     HHHHH    R     R      T      EEEEEEE   N    NN   EEEEEEE   R     R")
print("\n\n\n")
print("      \"THIS PROGRAM LETS YOU SORT THE CONTENT OF YOUR TEXT FILE IN ALPHABETICAL ORDER\" ")

print("\n  \"rememeber to turn off/disable Windows Defender or AntiVirus Software to run this program\"   ")


print("\n\nA file must in text formatt (ex: text.txt)")
files = input('put the name (optinal: location ) of the file you want to sort.\nhere:> ')
print("\n\n")
newfiles = input('put the name (optional: location) of the new file you want to create\nhere:> ')
print("\n\n\n")
# text_to_find = input('what do want to find ')





def making_list(file):
	dalist = []
	reading = open(file, "r+")
	for song in reading:
		dalist.append((song))
	reading.close()
	return dalist


listing = making_list(files)

def counter(lst):
	total = []
	for i in lst:
		if i[0] not in list(string.ascii_lowercase + string.ascii_uppercase):
			continue
		else:
			total.append(i)
	return total


to_sort = counter(listing)




def sorting_to_text(input_list):
	foutput = ""
	sortedlist = sorted(input_list)
	for ele in sortedlist:
		foutput += ele
	return foutput
		

plain_text = sorting_to_text(to_sort)



def make_sorted_new_file(nfile_name, text_plain):
	with open(nfile_name, "w") as nfile:
		nfile.write(text_plain)
		nfile.close()


make_sorted_new_file(newfiles, plain_text)



print("#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~# DONE #~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#")
print()
print("   total content of a file:", len(to_sort),"items") 
print()
print('   Your new sorted text file named (path) "%s" was successfully created.' % (newfiles))
print("   Look out on your directory to see your file.")
print("\n\n\n\n\n")