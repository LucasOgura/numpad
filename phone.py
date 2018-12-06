from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def main():
    if request.method == 'POST':
        if request.form['numberInput']!='':
            numInput = request.form['numberInput']
            try:
                result = countTelephoneNums(int(numInput))
                return render_template('index.html',result=result)
            except:
                return render_template('index.html')
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

def countTelephoneNums(digits):
    # number of digits
    n = 1
    # lastDigits[i] = number of telephone numbers which end in digit i
    lastDigits = [1,0,0,0,0,0,0,0,0,0]

    while(n < digits):
        numCounts = [0,0,0,0,0,0,0,0,0,0]
        
        if n % 3 == 1:
            for i in range(len(numCounts)):
                tallMove(i, lastDigits[i], numCounts)
        else:
            for i in range(len(numCounts)):
                shortMove(i, lastDigits[i], numCounts)
        
        lastDigits = numCounts
        n += 1
    
    return sum(lastDigits)

def tallMove(start, count, digitCount):
    if start == 1:
        digitCount[8] += count
        digitCount[6] += count
    elif start == 2:
        digitCount[9] += count
        digitCount[7] += count
    elif start == 3:
        digitCount[4] += count
        digitCount[8] += count
    elif start == 4:
        digitCount[9] += count
        digitCount[3] += count
        digitCount[0] += count
    elif start == 5:
        return
    elif start == 6:
        digitCount[7] += count
        digitCount[1] += count
        digitCount[0] += count
    elif start == 7:
        digitCount[6] += count
        digitCount[2] += count
    elif start == 8:
        digitCount[3] += count
        digitCount[1] += count
    elif start == 9:
        digitCount[2] += count
        digitCount[4] += count
    elif start == 0:
        digitCount[6] += count
        digitCount[4] += count

def shortMove(start, count, digitCount):
    if start == 1:
        digitCount[5] += count
    elif start == 2:
        digitCount[4] += count
        digitCount[6] += count
    elif start == 3:
        digitCount[5] += count
    elif start == 4:
        digitCount[2] += count
        digitCount[8] += count
    elif start == 5:
        digitCount[1] += count
        digitCount[3] += count
        digitCount[7] += count
        digitCount[9] += count
    elif start == 6:
        digitCount[2] += count
        digitCount[8] += count
    elif start == 7:
        digitCount[0] += count
        digitCount[5] += count
    elif start == 8:
        digitCount[4] += count
        digitCount[6] += count
    elif start == 9:
        digitCount[0] += count
        digitCount[5] += count
    elif start == 0:
        digitCount[7] += count
        digitCount[9] += count