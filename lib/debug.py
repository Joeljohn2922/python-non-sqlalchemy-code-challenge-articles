#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:") 

Magazine.all = []
Article.all = []

author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
    
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")
    
Article(author_1, magazine_1, "How to wear a tutu with style")
Article(author_1, magazine_1, "How to be single and happy")
Article(author_1, magazine_1, "Dating life in NYC")
Article(author_1, magazine_2, "Carrara Marble is so 2020")
Article(author_2, magazine_2, "2023 Eccentric Design Trends")
    
    
ipdb.set_trace()
