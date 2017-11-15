file_name = "number.txt"														
number =  "2;   5;    8;   34;   1;    7;   4;   11;   6;   97;  45;   23;   12;   5;    8;    5;    3;   12;  51;   3 \n"
number += "23;  3;    5;   6;    8;    9;   0;   1;    2;   32;  43;   21;   53;   32;   76;   45;   34;  23;  5;    9 \n"
number += "2;   3;    65;  87;   8;    5;   1;   1;    0;   76;  43;   21;   22;   45;   6;    4;    2;   7;   4;    7 \n"
number += "3;   45;   65;  72;   1;    0;   4;   77;   5;   3;   1;    6;    43;   36;   75;   32;   4;   2;   5;    2 \n"
number += "5;   2;    1;   3;    5;    7;   9;   0;    8;   7;   5;    3;    2;    1;    4;    6;    5;   3;   6;    6 \n"
number += "32;  43;   23;  45;   56;   58;  76;  45;   26;  92;  56;   86;   32;   75;   47;   24;   45;  23;  54;   7 \n"
number += "1;   2;    3;   4;    5;    6;   7;   8;    9;   0;   9;    8;    7;    6;    5;    4;    3;   2;   1;    3 \n"
number += "2;   43;   54;  63;   15;   4;   7;   8;    2;   5;   7;    9;    7;    35;   25;   5;    8;   8;   1;    2 \n" 
	
with open(file_name, 'w+') as file: 
	file.write(number)

def a_row(txt):
    txt = txt.split(';')
    txt = [float(i) for i in txt]
    return sum(txt)/20

def a_column(txt, num_col):
    average = 0
    for i in range(0, 8):
        buf = txt[i]
        buf = str(buf)
        buf = buf.split(";")
        for j in range(0, 20):
            if j == num_col:
                   average += float(buf[num_col])
    return round(average/8, 2)

with open(file_name, 'r') as file:
    lines = file.readlines()

    for i in range(0, 8):
    	lines[i] = lines[i].replace('\n', ';| %.2f \n' %a_row(lines[i]))
    	if i == 7:
    		for j in range(0, 108):
    			lines[7] += "-"
    			if j == 107:
    				lines[7] += "|\n"

    for i in range(0, 20):
        lines[7] +=  str(a_column(lines, i)) + " "

    for i in range(0, 8):
        lines[i] = lines[i].replace(';|', '|')

with open(file_name, 'w') as file:
    for line in lines:
        file.write(line)