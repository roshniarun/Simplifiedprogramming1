'''
Author: Thejas.R
		Roshni.A
Function: csv_dict_reader()
		  main()
Description : csv_dict_reader():
			  Reads value from country.csv file and writes it to the file given as input through command line
			  It also records the events in the log file
			  main():
			  Uses get_opt function to read values from command line argument

Parameters: csv_dict_reader():
			file_obj
			file1
			file2
			main():
			argv
'''
import csv
import sys, getopt
import datetime

logfile=''
outputfile=''

def csv_dict_reader(file_obj,file1,file2):

	#Read a CSV file using csv.DictReader
	i = datetime.datetime.now()
	l = open(file2,"w")
	f = open(file1,"w")
	l.write("%s The text file inputted through command line was created \n"%i)
	j=1
	reader = csv.DictReader(file_obj,delimiter=',')
	for line in reader:
		x=(line["Country"])
		y=(line["Capital"])
		z=(line["Population"])
		f.write("The capital of %s is %s and its population is %s \n"%(x,y,z))
		k = datetime.datetime.now()
		l.write("%s %d entry of country written to text file \n"%(k,j))
		j=j+1
	l.close()
	f.close()

def main(argv):
   global outputfile
   global logfile
   try:
      opts, args = getopt.getopt(argv,"f:l:",["ofile=","lfile="])
   except getopt.GetoptError:
      print ('test.py -f <inputfile> -l <logfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-f", "--ofile"):
         outputfile = arg
      elif opt in ("-l", "--lfile"):
         logfile = arg
      else:
      	print ('test.py -f <inputfile> -l <logfile>')

if __name__ == "__main__":
	f_obj=''
	main(sys.argv[1:])
	
	try:
		f_obj = open("Country.csv", "r") 
	except IOError:
		l = open(logfile,"w")
		m=datetime.datetime.now()
		l.write("%s Could not open csv file!"%m)
		l.close()
		
	with open("Country.csv", "r") as f_obj:
		f=outputfile 
		l=logfile          
		csv_dict_reader(f_obj,f,l)
