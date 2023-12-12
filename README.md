# Final-Project
To do this project I had to learn the basics of object oriented programming in Python, such as how classes, inheritance, and constructors work. While I didn't complete the parts requiring it directly, I also learned some about abstract syntax trees.

My general plan was to build a lexer to take in a proof from the user and turn it into a list of tokens such that I could then build a parser to generate an AST reflecting the structure of the proof as classes of variables, binary and unary operations, axioms, formulae, and the conclusion. After this, I was going to brute force check whether or not the proof was valid. That is, given the axioms of the proof, generate a complete list of possible permutations through valid sentential logic manipulations and check whether any of these is identical to the following line in the proof. If so, then that step is valid; if not, then it is invalid. Following this process through to the conclusion, with valid steps all the way, would return that the proof is valid. 

Unfortunately there is not much direct information about proof validators online. The video cited below is intended as a tutorial for building a programming language, however I was able to follow along (with some adjustments) in order to use it for my lexer. When designing the parser itself I had some trouble coming up with a grammatical structure that would be relevant to proof checking, and in particular the negation operator (being the only unary operator) gave me some trouble. 

In general, this project motivated me to take more interest in programming and computer science. Whereas I previously felt programming was algorithmic, motivating a project through my interests as a math/philosophy major helped me realize how interesting planning and designing such a program can be. In the future, I may in fact taking more computer science classes which I had previously not planned on doing. While I wasn't able to complete my project in time, I will absolutely be working on it over the break. Hopefully in the future I can complete the sentential logic validation, and possibly extent it to either validate predicate logic proofs or automatically prove sentential logic statements.

# Citation
I used the first two videos of the following series to build the Lexer and a portion of the Parser:
https://www.youtube.com/watch?v=Eythq9848Fg&list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD
