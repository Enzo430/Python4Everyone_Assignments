#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475";
a = text.find(" ")
b = text.find(".")
c = text[a+4:b+5]             #can also do c = text[a:]
d = float(c)
e = print(d)
