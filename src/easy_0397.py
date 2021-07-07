'''
Ezra S. Brooker
Date Created: 2021-07-05

https://www.reddit.com/r/dailyprogrammer/comments/oe9qnb/20210705_challenge_397_easy_roman_numeral/

For the purpose of today's challenge, a Roman numeral is a non-empty string of the characters 
M, D, C, L, X, V, and I, each of which has the value 1000, 500, 100, 50, 10, 5, and 1. The 
characters are arranged in descending order, and the total value of the numeral is the sum of
the values of its characters. For example, the numeral MDCCXXVIIII has the value 
1000 + 500 + 2x100 + 2x10 + 5 + 4x1 = 1729.

This challenge uses only additive notation for roman numerals. There's also subtractive notation, 
where 9 would be written as IX. You don't need to handle subtractive notation (but you can if you 
want to, as an optional bonus).

Given two Roman numerals, return whether the first one is less than the second one:

numcompare("I", "I") => false
numcompare("I", "II") => true
numcompare("II", "I") => false
numcompare("V", "IIII") => false
numcompare("MDCLXV", "MDCLXVI") => true
numcompare("MM", "MDCCCCLXXXXVIIII") => false
You only need to correctly handle the case where there are at most 1 each of D, L, and V, and at 
most 4 each of C, X, and I. You don't need to validate the input, but you can if you want. Any 
behavior for invalid inputs like numcompare("V", "IIIIIIIIII") is fine - true, false, or error.

Try to complete the challenge without actually determining the numerical values of the inputs.

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")


class RomanNumeral:

    _roman  = [ "N", "I", "V", "X", "L", "C", "D", "M"   ]
    _arabic = [  0,   1,   5,   10,  50,  100, 500, 1000 ]
    _maxnum = 3

    def __init__(self, numeral=None, modern=None, form="additive"):
        self._errmsg = f"{numeral} is not a valid numeral in {form} notation"
        if form == "additive": self._maxnum+=1
        self.numeral = numeral
        self.modern  = modern
        self.form    = form
        self._convert()

    def _convert(self):

        if self.modern is None:
            numeral = self.numeral
            sgn = 1
            if "-" in numeral:
                sgn = -1
                numeral = numeral.replace("-","")

            if self.form != "irregular-additive" and \
               (numeral.count("I") > self._maxnum or \
                numeral.count("X") > self._maxnum or \
                numeral.count("C") > self._maxnum): return

            self.modern = [ self._arabic[self._roman.index(k)] for k in numeral[::-1] ]
            if self.form=='subtractive': 
                self.modern = self.modern[0] + sum(v if v >= self.modern[i] else -v for i,v in enumerate(self.modern[1:]))
            else:
                self.modern = self.modern[0] + sum(v for v in self.modern[1:])    

            self.modern *= sgn

        elif self.numeral is None:
            if self.modern == 0: 
                self.numeral = "N"
                return

            self.numeral = ""
            modern = str(self.modern)
            if modern[0] == "-":
                self.numeral = "-"
                modern = modern[1:]

            ones = int(modern[-1])
            tens, huns, thns = 0, 0, 0
            if len(modern) > 1: tens = int(modern[-2])
            if len(modern) > 2: huns = int(modern[-3])
            if len(modern) > 3: thns = int(modern[:-3])

            # Add thousands
            self.numeral += thns*"M"

            if self.form=="subtractive":

                # Add hundreds
                if huns == 9: self.numeral += f"{(huns//9)*'CM'}"
                if 4 < huns < 9: self.numeral += f"{(huns//5)*'D'}"
                if huns == 4: self.numeral += f"{(huns//4)*'CD'}"
                if 0 < (huns-5)%5 < 4: self.numeral += f"{((huns-5)%5)*'C'}"

                # Add tens
                if tens == 9: self.numeral += f"{(tens//9)*'XC'}"
                if 4 < tens < 9: self.numeral += f"{(tens//5)*'L'}"
                if tens == 4: self.numeral += f"{(tens//4)*'XL'}"
                if 0 < (tens-5)%5 < 4: self.numeral += f"{((tens-5)%5)*'X'}"

                # Add ones
                if ones == 9: self.numeral += f"{(ones//9)*'IX'}"
                if 4 < ones < 9: self.numeral += f"{(ones//5)*'V'}"
                if ones == 4: self.numeral += f"{(ones//4)*'IV'}"
                if 0 < (ones-5)%5 < 4: self.numeral += f"{((ones-5)%5)*'I'}"

            else:
                self.numeral += f"{(huns//5)*'D'}{((huns-5)%5)*'C'}"   # Add hundreds
                self.numeral += f"{(tens//5)*'L'}{((tens-5)%5)*'X'}"   # Add tens
                self.numeral += f"{(ones//5)*'V'}{((ones-5)%5)*'I'}"   # Add ones


    def _validate_operation(self,other):
        if self.modern is None: return False, f"{self._errmsg}"
        if other.modern is None: return False, f"{other._errmsg}"
        if self.form != other.form: return False, f"{self.form} and {other.form} are not the same notations!"
        return True, ""

    def _validate_equality(self,other):
        if self.modern is None: return False, f"{self._errmsg}"
        if other.modern is None: return False, f"{other._errmsg}"
        return True, ""


    def __str__(self):
        return f"({self.numeral}, {self.modern})"

    def __pos__(self):
        return RomanNumeral(modern= abs(self.modern), form=self.form)

    def __neg__(self):
        return RomanNumeral(modern= -self.modern, form=self.form)

    def __abs__(self):
        return RomanNumeral(modern= abs(self.modern), form=self.form)

    def __add__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern + other.modern,form=self.form)

    def __sub__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern - other.modern,form=self.form)

    def __mul__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern * other.modern,form=self.form)

    def __floordiv__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern // other.modern,form=self.form)

    def __div__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern / other.modern,form=self.form)

    def __mod__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern % other.modern,form=self.form)

    def __pow__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern ** other.modern,form=self.form)

    def __iadd__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern + other.modern,form=self.form)

    def __isub__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern - other.modern,form=self.form)

    def __imul__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern * other.modern,form=self.form)

    def __ifloordiv__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern // other.modern,form=self.form)

    def __idiv__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern / other.modern,form=self.form)

    def __imod__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern % other.modern,form=self.form)

    def __ipow__(self,other):
        valid, msg = self._validate_operation(other)
        if not valid: return msg
        return RomanNumeral(modern=self.modern ** other.modern,form=self.form)

    def __eq__(self,other):
        valid, msg = self._validate_equality(other)
        if not valid: return msg
        return self.modern == other.modern

    def __ne__(self,other):
        valid, msg = self._validate_equality(other)
        if not valid: return msg
        return self.modern != other.modern

    def __ge__(self,other):
        valid, msg = self._validate_equality(other)
        if not valid: return msg
        return self.modern >= other.modern

    def __gt__(self,other):
        valid, msg = self._validate_equality(other)
        if not valid: return msg
        return self.modern > other.modern

    def __le__(self,other):
        valid, msg = self._validate_equality(other)
        if not valid: return msg
        return self.modern <= other.modern

    def __lt__(self,other):
        valid, msg = self._validate_equality(other)
        if not valid: return msg
        return self.modern < other.modern


def rDailyProggerTest(form="additive"):
    rm_1   = RomanNumeral("-I",               form=form)
    rm     = RomanNumeral("I",                form=form)
    rm0    = RomanNumeral("N",                form=form)
    rm1    = RomanNumeral("I",                form=form)
    rm2    = RomanNumeral("II",               form=form)
    rm4    = RomanNumeral("IIII",             form=form)
    rm5    = RomanNumeral("V",                form=form)
    rm7    = RomanNumeral("IIIIIII",          form=form)
    rm1665 = RomanNumeral("MDCLXV",           form=form)
    rm1666 = RomanNumeral("MDCLXVI",          form=form)
    rm2000 = RomanNumeral("MM",               form=form)
    rm1999 = RomanNumeral("MDCCCCLXXXXVIIII", form=form)
    print(f"\n r/DailyProgrammer Tests ({form} notation)")
    print(f" {rm1} < {rm1} : {rm1<rm1}")
    print(f" {rm1} < {rm2} : {rm1<rm2}")
    print(f" {rm2} < {rm1} : {rm2<rm1}")
    print(f" {rm5} < {rm4} : {rm5<rm4}")
    print(f" {rm5} < {rm7} : {rm5<rm7}")
    print(f" {rm1665} < {rm1666} : {rm1665<rm1666}")
    print(f" {rm2000} < {rm1999} : {rm2000<rm1999}\n")
    print(f"\n Extra Tests ({form} notation)")
    print(f" {rm1} = {rm1} : {rm1==rm1}")
    print(f" {rm5} != {rm4} : {rm5!=rm4}")
    print(f" {rm2000} + {rm5} : {rm2000+rm5}")
    print(f" {rm4} - {rm4} : {rm4-rm4}")
    print(f" {rm4} - {rm5} : {rm4-rm5}")
    print(f" {rm5} - {rm1} : {rm5-rm1}")
    print(f" {rm5} % {rm5} : {rm5%rm5}")
    print(f" {rm5} % {rm4} : {rm5%rm4}")
    print(f" {rm5} + {rm1} - {rm2} : {rm5+rm1-rm2}")
    print(f" {rm5} + {rm1} - {rm4} : {rm5+rm1-rm4}")
    print(f" {rm1999} * {rm4} : {rm1999*rm4}\n")
    print(f" neg({rm1}) : {-rm1}")
    print(f" pos({rm1}) : {+rm1}")
    print(f" abs({rm1}) : {abs(rm1)}")
    print(f" neg({rm_1}) : {-rm_1}")
    print(f" pos({rm_1}) : {+rm_1}")
    print(f" abs({rm_1}) : {abs(rm_1)}")
    print(f" neg(neg({rm_1})) : {--rm_1}")
    print(f" neg(neg(neg({rm_1}))) : {---rm_1}\n")
    for i in range(10):
        print(f"{i}: {rm}")
        rm+=rm1


if __name__ == '__main__':

    rDailyProggerTest(form="additive")
    rDailyProggerTest(form="subtractive")
    rDailyProggerTest(form="irregular-additive")
