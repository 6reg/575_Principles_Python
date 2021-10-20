import webbrowser # make available to this program all the code from the python standard library module called "webbrowser"
import json # import standard library module "json"
from urllib.request import urlopen # import only the urlopen function from standard library module urllib.request

print("Let's find an old website.")
site = input("Type a website URL: ") # prints question, reads input and saves to program variable called "site"
era = input("Type a year, month, and day, like 201050613: ") # print another question, read input and save to variable "era"
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era) # construct a sting variable "url" with user inputted variables
response = urlopen(url) # connect to webserver with urlopen function with user inputted url as argument
contents = response.read() # get response data and assign to variable "contents"
text = contents.decode("utf-8") # decode contents to a text string in json format and assign to variable "text"
data = json.loads(text) # convert text to python data structure "data" variable
try: # try to run next four lines, if any fail, run except line
    old_site = data["archived_snapshots"]["closest"]["url"] # if there's a match for site and date, extract value from three-level python dictionary
    print("Found this copy: ", old_site) # print found url
    print("It should appear in your browser now.")
    webbrowser.open(old_site) # function call with old_site var
except: # if try fails ..
    print("Couldn't find", site)
