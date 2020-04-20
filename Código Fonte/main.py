#palavras reservadas
reserved_words = ['while', 'for', 'do', 'return', 'break', 'continue', 'switch', 'case']

#operadores
operators = ['+', '-', '/', '*', '^']

#atribuidores
assigners = ['=', '+=', '-=', '/=', '*=']

#valida int
def isInt(value):
  try:
    int(value)
    return True
  except:
    return False

#valida float
def isFloat(value):
  try:
    float(value)
    return True
  except:
    return False

def content_file_print(content):
    print('')
    print("File Contente: ")
    print('>>>\n{}'.format(content))
    print('>>>\n')

def print_lexemas(lexema):
    print("Lexemas:")
    print(lexema)

def print_code_help(code):
    print("code help:\n{}\n".format(code))

def add_espace_final_instruct(code):
    #add espace to ;  
    code = code.replace(";", " ;")
    return code

def replace_to_break_line(code):
    #replace \n to espace
    code = code.replace("\n", " ")
    return code

def replace_to_tabulation(code):    
    #replace \t to espace
    code = code.replace("\t", " ")
    return code

def lexemas(code):
    #split code
    list_lexema = code.split()
    
    #matrix of lexema
    matriz = []

    #para cada palavra examina seu tipo
    for word in list_lexema:        
        if word in reserved_words:
            matriz.append([word, word])
        elif word in operators:
            matriz.append([word, word])
        elif word in assigners:
            matriz.append([word, word])
        elif word == ';':
            matriz.append([word, '$'])        
        elif isInt(word) or isFloat(word):
            matriz.append([word, 'num'])
        else:
            matriz.append([word, 'id'])    
    return matriz

def analise_lexema(code):
    #functions tratament
    code = add_espace_final_instruct(code)
    code = replace_to_break_line(code)
    code = replace_to_tabulation(code)
    
    #print codigo auxiliar
    print_code_help(code)

    #funtion get lexemas 
    lexema = lexemas(code)

    #print lexemas
    print_lexemas(lexema)


#function main
if 'main' == 'main':
    #open file cod.txt
    arquivo = open('cod.txt', 'r')

    #read file
    code = arquivo.read()

    #type cast
    code = str( code )

    #function print content file
    content_file_print(code)

    #function analise lexema
    analise_lexema(code)

    #close file
    arquivo.close()