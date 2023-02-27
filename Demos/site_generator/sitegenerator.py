import re

def main():
	#open the files containing the player text
	f1 = open("player1_template.txt","r")
	f2 = open("player2_template.txt","r")
	#open the file containing the template page
	f3 = open("page_template.txt","r")
	#read the files into memory
	playeronelines = f1.read()
	playertwolines = f2.read()
	pagetemplatelines = f3.read()
	#substitute the player text into the template
	pagetemplatelines = re.sub(r'<!--PLAYER_ONE-->',playeronelines,pagetemplatelines)
	pagetemplatelines = re.sub(r'<!--PLAYER_TWO-->',playertwolines,pagetemplatelines)
	#write out the changes to the finished page
	outfile=open("output_page.html", "w") 
	outfile.write(pagetemplatelines)
	outfile.close() 

if __name__ == "__main__":
	main()

