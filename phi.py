# import scispacy
# import spacy
# import scrubadub
# import nltk
# nlp = spacy.load("en_ner_bc5cdr_md")
# import nltk
# # nltk.download('punkt')
# scrubber = scrubadub.Scrubber()
# scrubber.remove_detector('url')
# scrubber.remove_detector('ssn')
# import re

# def clean_text(text):
#   text_s = scrubber.clean(text)
#   text_s
#   text_n = text_s.replace("\n"," ")
#   text_d = text_n.replace("{{NAME}}","")
#   text_e = text_d.replace("{{EMAIL}}","")
#   text_p = text_e.replace("{{PHONE}}","")
#   text_p
#   s = "Jane Doe 12/15/2017 - 8:35 pm - SDFTRD $550.95 2004/12/28 abcd@gmail.com abhinav.jha@intechhub.com 9766318407 1-212-555-1212 208.83.243.70 https://www.geeksforgeeks.org/python-ways-to-remove-numeric-digits-from-given-string/"
#   new_s = re.sub('\d+\/\d+\/\d+', '', text_p) 
#   new_t = re.sub('\S*@\S*\s?','',new_s)
#   new_i = re.sub(r'((1-\d{3}-\d{3}-\d{4})|(\(\d{3}\) \d{3}-\d{4})|(\d{3}-\d{3}-\d{4}))', '', new_t)
#   new_q = re.sub('(\d{3}\d{3}\d{4})', "", new_i)
#   new_r = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',"",new_q)
#   print(new_r)
#   return new_r

# text = """
# I am Leo.
# My dad name is Chakra.
# My uncle name is Ram.
# My brother name is Selva.
# I live in Boston USA.
# My DOB is 29/01/1941.
# I work in Pandrdental and their website is https://www.pandrdental.com/.
# My number is (609) 783-9004.
# My friend Donald Trump is suffering from Lung Cancer,Flu,Coronavirus,Cavities,Gingivitis,Periodontal,Polio.
# He has website name https://www.eprmm.io/
# He lives in Sydney,Australia.
# His number is 1-212-555-1212
# His date of birth is 12/15/2017
# He is fan of Manchester United and Messi.
# """
# clean_text(text)