import random
import dominate
from dominate.tags import *
from dominate.util import raw

prompts = []

numPrompts = 4

names = ["names","of","recipients"]

with open('generated_prompts.txt','r') as gp:
    for line in gp:
        if '=' not in line:
            prompts.append(line)

promptChoices = []

def isIn(array,item):
    check = False
    for a in array:
        if a == item:
            check = True
    return check

for i in range(len(names) * numPrompts):
    x = random.randint(0,100)
    while isIn(promptChoices,x):
        x = random.randint(0,100)
    promptChoices.append(x)
    print(prompts[promptChoices[i]])


for n in range(len(names)):
    for i in range(numPrompts):
        doc = dominate.document(title=(names[n] + `i`))

        with doc.head:
            td(raw('<style> h1 {font-family : monospace; font-size : 16pt;} </style>'))

        with doc:
            with div():
                attr(cls='body')
                h1(prompts[promptChoices[(n * numPrompts) + i]])

        htmlFile = open(names[n] + `i` + ".html", "w")
        htmlFile.write(doc.render())
        htmlFile.close()

        print(names[n] + `i` + " successfully created.\n")
