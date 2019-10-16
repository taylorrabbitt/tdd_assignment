class Product():
        def __init__(self):
                pass
        
        def stringToNum(num):
                s = num[::-1]
                total = 0
                for i in range(len(s)):
                        if s[i] == '1':
                                total += 1*10**(i)
                        elif s[i] == '2':
                                total += 2*10**(i)
                        elif s[i] == '3':
                                total += 3*10**(i)
                        elif s[i] == '4':
                                total += 4*10**(i)
                        elif s[i] == '5':
                                total += 5*10**(i)
                        elif s[i] == '6':
                                total += 6*10**(i)
                        elif s[i] == '7':
                                total += 7*10**(i)
                        elif s[i] == '8':
                                total += 8*10**(i)
                        elif s[i] == '9':
                                total += 9*10**(i)
                return total
        
        def processNums(self, num1, num2):
                if type(num1) != str or type(num2) != str:
                        return 'Error'
                if num1 == '0' or num2 == '0':
                        return 0
                if num1 == '' and num2 == '':
                        return ''
                if num1 == '':
                        n2 = Product.stringToNum(num2)
                        return n2
                if num2 == '':
                        n1 = Product.stringToNum(num1)
                        return n1
                else:
                        sToNum1 = Product.stringToNum(num1)
                        sToNum2 = Product.stringToNum(num2)
                        return sToNum1 * sToNum2
                                
