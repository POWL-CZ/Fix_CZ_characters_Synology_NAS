import os

#enter your folder path here
path=''

c=0
for root, dirs, files in os.walk(path):
    for filename in files:
        c=c+1
i=1
for root, dirs, files in os.walk(path):
    for filename in files:
        new_filename=filename
        
        for character, correction in {"¼":"C", "²":"r", "º":"z", '∞':'y', '╪':'e', 'τ':'s','ƒ':'c','à':'u','σ':'n','╘':'d','μ':'s','£':'t','╡':'A','ª':'z','╥':'d'}.items():
            new_filename = new_filename.replace(character, correction)
       
        print(f'{i} of {c}: {os.path.join(root, new_filename)}')
        os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
            
        i+=1
