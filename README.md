# Obfuscated for solving sudoku puzzles (8 lines of code)!

# How to use the script

1) Clone/Download script
2) Open your terminal
3) Go to cloned/downloaded script path
4) Create virtual environment
    *python -m venv venv*
5) Activate newly created virtual enviroment (depending on your OS)
    *source venv/bin/activate*  (Linux)    
    *venv\Scripts\activate . *   (Windows)
6) Install all requirements (it is just numpy btw)
    *pip install -r requirements.txt*
7) Enter your python shell
    *python*
8) import solving function
    *from obscure import solve*
9) import some sudoku sample (there are four of them)
    *from samples import sample1*
10) see how sudoku looks unsolved
    *print(sample1)*
11) solve and see solved sudoku
    *print(solve(sample1))*
