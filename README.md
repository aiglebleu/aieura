----|----1----|----2----|----3----|----4----|----5----|----6----|----7----|----8
# aieura
AiEura is a dummy AI chatbot designed to learn from input from users over time.
The bot currently uses a simple text file to store responses and recall them
from memory. While the bot simply parrots responses it knows from file, it has
been given the capibility to choose responses to phrases similar or close to the
user input. This makes AiEura's responses more fluid than other AI chatbots.

Ai Eura is a python3 implimentation and has the following features:
   - AiEura can learn from user input over time, and will store these learned
     responses in a database managed by the bot in a single, easy to read .txt
     file.
   - AiEura has a supplied dictionary of English words externally. The bot will
     compare indiviual words supplied in converation to this dictionary. If a
     word is not included in the dictionary, it may be mispelled, which will help
     prevent pollution of AiEura's storage heavy database file. If a correctly
     spelled word is not included in the dictionary, the user has the option of
     adding that word to the dictionary. To add a word to the dictionary the user
     will be propmted.
   - AiEura also includes a second dictionary of banned or undesireable words
     which it will check. Any sentence including these words will be disregarded
     as input.
   - AiEura has the potential to learn any natural lanugage provided that the
     proper text support is available.
   - On startup AiEura will list the number of words in both dictionaries, and
     the number of total responses available in the database.
   - The newest version of AiEura includes a combonation database merger and
     sorter that users may run to combine two database files, while removing
     duplicate responses and sorting the contents.

Commands:
   - [input] - input is any sentence of which each word in that sentence is a
     valid word that is included in AiEura's dictionary, and not included in the
     banned word dictionary.
   - ! - Instead of input, the character '!' may be supplied by the user instead,
     which will restart the program.
   - In both cases when the add word to dictionary prompt is given, the user will
     need to resubmit their original input to have AiEura respond.
       - Y - Y, Yes or any variation thereof is input for the add word to 
         dictionary propmt. Selecting yes will add the prompted word to AiEura's 
         dictionary.
       - N - N, No or any variation thereof is input for the dictionary prompt
         that will decline adding the prompted word to AiEura's dictionary.
         
Version Information:
   - 1.0.1
       + Added support for MacOS, Linux, Unix, and Windows
       * Small efficiency optimizations
   - No Version Number
   - Always Updates
       * English Dictionary
       * Banned Dictionary
       * data.txt
