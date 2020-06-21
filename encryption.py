import math
def encryption(s):
    result =" "
    text = s.replace(" ","")
    k = math.floor(math.sqrt(len(text)))
    text_array = [text[i:i+k] for i in range(0,len(text),3)]
    result = "\n".join(text_array)
    print(result)
    return result


encryption("have a nice day")