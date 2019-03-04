
import textwrap
import random

#orignila text found https://www.quora.com/How-would-you-describe-a-sunset

originaltext = """
The glowing sun, a crisp circle in the bloody sky, illuminated a quivering path across the water.
It bathed the ocean's meek waves and the wispy clouds in a burning red.
As the sun dipped below the horizon, the fleeting colors of the red dusk began to fade away.
The charcoal-black rocks circled around small pools of water, shimmering confidently before dark fell upon them.
The sun fell asleep, shielded behind three sloping, blue mountains, each smaller but tougher
than the one before. The trees were strong, black soldiers, standing in an unmoving row. """

for line in originaltext:
      line = line.strip()
      words = line.split(" ")
      new_line = " ".join(line)



newnames = [originaltext.replace('sun', 'fire') for name in originaltext]


indentedtext = (textwrap.fill(originaltext, initial_indent= '    '))

test = [originaltext.swapcase(), len(originaltext)]

#print(test)

text1 = ' '.join(reversed(originaltext))
text2 = ":".join(text1)
print text2.swapcase()
print (newnames)
print len(originaltext)



#indentedtext2 = (textwrap.fill(newnames, initial_indent= '    '))

#print (indentedtext2)
