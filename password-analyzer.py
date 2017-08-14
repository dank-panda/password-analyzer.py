#!/usr/bin/python
import sys

#Author: dank-panda
#version: 0.1 - initial script

#create a class so we can add some colors to the output
class colors:
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	end = '\033[0m'

#make sure we have the right args from the command line
if len(sys.argv) < 2:
    print colors.yellow +"Usage: python " + sys.argv[0] + " <passwords_file.txt>\n" + colors.end
    sys.exit()

passfile = sys.argv[1]
#set some vars, and zero them out so they can be used as counters
starts_upper = 0
starts_lower = 0
starts_number = 0
starts_special = 0
ends_letter = 0
ends_number = 0
ends_special = 0
length5 = 0
length6 = 0
length7 = 0
length8 = 0
length9 = 0
length10 = 0
length11 = 0
length12 = 0
#check for client names. Replace the placeholders with specifc names to search for.
contains_client = 0
clients = ('client','client1','client2')
num_words = 0

#check starting character
with open(passfile) as temp:
	for line in temp:
		num_words +=1
		if line[0].isupper():
			starts_upper +=1
		elif line[0].islower():
			starts_lower +=1
		elif line[0].isdigit():
			starts_number +=1
                else:
			starts_special +=1
temp.close()

#check ending character
with open(passfile) as temp2:
        for line in temp2:
		if line.strip()[-1:].isalpha():
                        ends_letter +=1
                elif line.strip()[-1:].isdigit():
                        ends_number +=1
		else:
			ends_special +=1
temp2.close()

#check word length
with open(passfile) as temp3:
        for line in temp3:
                if len(line) <= 5:
                        length5 +=1
                elif len(line) == 6:
                        length6 +=1
                elif len(line) == 7:
                        length7 +=1
                elif len(line) == 8:
                        length8 +=1
                elif len(line) == 9:
                        length9 +=1
                elif len(line) == 10:
                        length10 +=1
                elif len(line) == 11:
                        length11 +=1
                else:
                        length12 +=1
temp3.close()

#check for client names specified in the vars from the beginning of the script
with open(passfile) as temp4:
        for line in temp4:
		line = line.lower()
                if any(s in line for s in clients):
                        contains_client +=1
temp4.close

#calculating percentages
percent_starts_upper = starts_upper * 100 / num_words

if (percent_starts_upper >= 67):
	colorup = colors.green
elif (percent_starts_upper <= 33):
        colorup = colors.red
else:
	colorup = colors.yellow

percent_starts_lower = starts_lower * 100 / num_words

if (percent_starts_lower >= 67):
        colorlow = colors.green
elif (percent_starts_lower <= 33):
        colorlow = colors.red
else:
	colorlow = colors.yellow

percent_starts_number = starts_number * 100 / num_words

if (percent_starts_number >= 67):
        colornum = colors.green
elif (percent_starts_number <= 33):
        colornum = colors.red
else:
	colonum = colors.yellow

percent_starts_special = starts_special * 100 / num_words

if (percent_starts_special >= 67):
        colorspec = colors.green
elif (percent_starts_special <= 33):
        colorspec = colors.red
else:
	colorspec = colors.yellow

percent_ends_letter = ends_letter * 100 / num_words

if (percent_ends_letter >= 67):
        color_ends_letter = colors.green
elif (percent_ends_letter <= 33):
        color_ends_letter = colors.red
else:
        color_ends_letter = colors.yellow

percent_ends_number = ends_number * 100 / num_words

if (percent_ends_number >= 67):
        color_ends_num = colors.green
elif (percent_ends_number <= 33):
        color_ends_num = colors.red
else:
        color_ends_num = colors.yellow

percent_ends_special = ends_special * 100 / num_words

if (percent_ends_special >= 67):
        color_ends_spec = colors.green
elif (percent_ends_special <= 33):
        color_ends_spec = colors.red
else:
        color_ends_spec = colors.yellow

percent_length5 = length5 * 100 / num_words

if (percent_length5 >= 67):
        color_length5 = colors.green
elif (percent_length5 <= 33):
        color_length5 = colors.red
else:
        color_length5 = colors.yellow

percent_length6 = length6 * 100 / num_words

if (percent_length6 >= 67):
        color_length6 = colors.green
elif (percent_length6 <= 33):
        color_length6 = colors.red
else:
        color_length6 = colors.yellow

percent_length7 = length7 * 100 / num_words

if (percent_length7 >= 67):
        color_length7 = colors.green
elif (percent_length7 <= 33):
        color_length7 = colors.red
else:
        color_length7 = colors.yellow

percent_length8 = length8 * 100 / num_words

if (percent_length8 >= 67):
        color_length8 = colors.green
elif (percent_length8 <= 33):
        color_length8 = colors.red
else:
        color_length8 = colors.yellow

percent_length9 = length9 * 100 / num_words

if (percent_length9 >= 67):
        color_length9 = colors.green
elif (percent_length9 <= 33):
        color_length9 = colors.red
else:
        color_length9 = colors.yellow

percent_length10 = length10 * 100 / num_words

if (percent_length10 >= 67):
        color_length10 = colors.green
elif (percent_length10 <= 33):
        color_length10 = colors.red
else:
        color_length10 = colors.yellow

percent_length11 = length11 * 100 / num_words

if (percent_length11 >= 67):
        color_length11 = colors.green
elif (percent_length11 <= 33):
        color_length11 = colors.red
else:
        color_length11 = colors.yellow

percent_length12 = length12 * 100 / num_words

if (percent_length12 >= 67):
        color_length12 = colors.green
elif (percent_length12 <= 33):
        color_length12 = colors.red
else:
        color_length12 = colors.yellow

percent_client = contains_client * 100 / num_words

if (percent_client >= 67):
        color_client = colors.green
elif (percent_client <= 33):
        color_client = colors.red
else:
        color_client = colors.yellow

#writing the output of the calculations and colorizing
print "-" *60
print " Starting Characters"
print "-" *60
print colorup + "",starts_upper,"of the",num_words,"passwords start with an uppercase letter"
print "  [ ~",percent_starts_upper,"% ] \n" + colors.end

print colorlow + "",starts_lower,"of the",num_words,"passwords start with a lowercase letter"
print "  [ ~",percent_starts_lower,"% ] \n" +colors.end

print colornum + "",starts_number,"of the",num_words,"passwords start with a number"
print "  [ ~",percent_starts_number,"% ] \n" +colors.end

print colorspec + "",starts_special,"of the",num_words,"passwords start with a special character"
print "  [ ~",percent_starts_special,"% ] \n" +colors.end

print "-" *60
print " Ending Characters"
print "-" *60

print color_ends_letter + "",ends_letter,"of the",num_words,"passwords end with a letter"
print "  [ ~",percent_ends_letter,"% ] \n" +colors.end

print color_ends_num + "",ends_number,"of the",num_words,"passwords end with a number"
print "  [ ~",percent_ends_number,"% ] \n" +colors.end

print color_ends_spec + "",ends_special,"of the",num_words,"passwords end with a special character"
print "  [ ~",percent_ends_special,"% ] \n" +colors.end

print "-" *60
print " Word Length"
print "-" *60

print color_length5 + "",length5,"of the",num_words,"passwords have 5 or fewer letters"
print "  [ ~",percent_length5,"% ] \n" +colors.end

print color_length6 + "",length6,"of the",num_words,"passwords have 6 letters"
print "  [ ~",percent_length6,"% ] \n" +colors.end

print color_length7 + "",length7,"of the",num_words,"passwords have 7 letters"
print "  [ ~",percent_length7,"% ] \n" +colors.end

print color_length8 + "",length8,"of the",num_words,"passwords have 8 letters"
print "  [ ~",percent_length8,"% ] \n" +colors.end

print color_length9 + "",length9,"of the",num_words,"passwords have 9 letters"
print "  [ ~",percent_length9,"% ] \n" +colors.end

print color_length10 + "",length10,"of the",num_words,"passwords have 10 letters"
print "  [ ~",percent_length10,"% ] \n" +colors.end

print color_length11 + "",length11,"of the",num_words,"passwords have 11 letters"
print "  [ ~",percent_length11,"% ] \n" +colors.end

print color_length12 + "",length12,"of the",num_words,"passwords have 12 or more letters"
print "  [ ~",percent_length12,"% ] \n" +colors.end

print "-" *60
print " Client Name"
print "-" *60

print color_client + "",contains_client,"of the",num_words,"passwords have the client's name"
print "  [ ~",percent_client,"% ] \n" +colors.end
