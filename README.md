# Caesar-s-encryption

This is one of my first Python projects, I wrote it just for the purpose of learning and practice.

As everyone knows Cesar's encryption is basically you change the actual letter of the text by one letter in front of or behind the original letter, in the case of this project he walks backwards in the alphabet.

Encrypted Text:

for example imagine the phrase "hello world" encrypted with this method would look something like "savip ropia"

Key:

The key is a sequence of numbers, where n is the key number in the first letter of the encrypted word, starting from that letter, n is the number of times you have to go back in the alphabet to find the actual letter. The project needs a key for each word in the sentence, they are stored in a list, ie lists within the list. For example the key to our encrypted "hello world" savip ropia is [[11, 22, 10, 23, 1], [21, 0, 24, 23, 23]]


In addition, both the encrypted phrase and keys must be written to the corresponding text files in the "resource" folder.
