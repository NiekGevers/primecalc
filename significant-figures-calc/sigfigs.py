
class SigFigs():

    def count(self, number):
        """
        Counts number of sig figs for a given number

        INPUTS: number
        OUTPUTS: number of sig figs of input
        """
        # converting E to e, otherwise breaks code
        number = str(number).lower()
        # deleting neg. sign, not important for sig figs
        if '-' in number:
            number = number.replace("-", "")
        numb_list = list(number)

        if '.' in numb_list and 'e' not in numb_list:
            decimal_location = numb_list.index('.')
            numb_list[decimal_location] = '0'
            return self.__calc_with_decimals(numb_list, decimal_location)
        elif '.' not in numb_list:
            return self.__calc_without_decimals(numb_list)
        elif 'e' in numb_list:
            # exponential notation
            return numb_list.index('e')-1
            # -1 for decimal place
        else:
            print("Something broke")

    def __calc_with_decimals(self, numb_list, decimal_location):
        """
        Helper function for determining number of sig figs
        the case when the input has a decimal

        INPUTS: numb_list (python list of number)
                decimal_location (integer of location in numb_list
        OUTPUTS: number of sig figs in input
        """
        for index, digit in enumerate(numb_list):
            if digit != '0':
                first_non_zero_location = index
                # 1st NZ found, no need to keep iterating
                break
        if first_non_zero_location < decimal_location:
            # 1st NZ before decimal, all digits after are signficant
            # number of digits after 1st NZ, excluding the decimal point.
            return len(numb_list)-first_non_zero_location-1

        if first_non_zero_location > decimal_location:
            # anything after the 1st NZ is significant
            return len(numb_list) - first_non_zero_location

    def __calc_without_decimals(self, numb_list):
        """
        Helper function for determining number of sig figs
            the case when the input has a decimal
        INPUTS: numb_list (python list of number)
        OUTPUTS: number of sig figs in input
        """
        for index, digit in enumerate(numb_list):
            if digit != '0':
                first_non_zero_location = index
                # 1st NZ found, no need to keep iterating
                break

        for index, digit in reversed(list(enumerate(numb_list))):
            if digit != '0':
                last_non_zero_location = index
                break

        # calculate number of digits between non zeros, inclusive
        return last_non_zero_location - first_non_zero_location + 1

    def __calc(self, number1, number2, operation):
        """
        Performs mathematical operation and retains sig figs
        INPUTS: number1,number2 (input numbers)
                operation (str of operator to be performed)
        OUTPUTS: calculated answer to correct sig figs
        """
        if operation == "*" or operation == "/":
            return self.__multiplicative_calc(number1, number2, operation)
        elif operation == "+" or operation == "-":
            return self.__additive_calc(number1, number2, operation)
        else:
            print("Uh oh, check your operator parameter and try again")

    def multiply(self, number1, number2):
        """
        Determines multiplication operations
        while conserving sig figs
        """
        return self.__multiplicative_calc(number1, number2, "*")

    def divide(self, number1, number2):
        """
        Determines division operations
        while conserving sig figs
        """
        return self.__multiplicative_calc(number1, number2, "/")

    def __multiplicative_calc(self, number1, number2, operation):
        """
        Determines multiplication and division operations
        while conserving sig figs

        Because the operation is multiplying/dividing,
        sig fig rules state that the answer should have the sig figs
        of the smallest input. EX: 6.154 * 3.14 = 19.3

        INPUTS: number1,number2 (numbers in operation)
                operation ("*" or "/")
        OUTPUTS: answer to calculation with correct sig figs
        """
        # return value with smallest sig figs
        sf1, sf2 = self.count(number1), self.count(number2)
        sigfig = min(sf1, sf2)
        evaluation = eval(number1+operation+number2)
        exp_string = "%.*e" % (sigfig-1, evaluation)
        answer = exp_string
        # VVVV doesn't quite work yet, trying to convert exp to decimal form
        # if "." in exp_string :
        #     exp_string = exp_string.replace(".","")
        # front_str,back_str = exp_string.split('e')
        # exponent = int(back_str)
        # if exponent == 0:
        #     # no exponent, can truncate
        #     return front_str
        # elif exponent > 0:
        #     if exponent > len(front_str):
        #         # +1 for decimal place
        #         answer = front_str+(exponent-len(front_str)+1)*"0"
        #     elif exponent < len(front_str):
        #         # have to add decimal back in
        #         answer = front_str[:1+exponent]+"."+front_str[1+exponent:]
        #     elif exponent == len(front_str):
        #         answer = front_str + "."
        # elif exponent < 0:
        #     answer =  "0." + (abs(exponent)-1)*"0" + front_str

        return answer

    def add(self, number1, number2):
        """
        Determines addtion operations
        while conserving sig figs
        """
        return self.__additive_calc(number1, number2, "+")

    def subtract(self, number1, number2):
        """
        Determines subtraction operations
        while conserving sig figs
        """
        return self.__additive_calc(number1, number2, "-")

    def __additive_calc(self, number1, number2, operation):
        """
        Determines addition and subtraction operations
        while conserving sig figs

        Because the oepration is adding/subtracting, sig fig rules
        state that the answer should retain the fewest deciaml places
        between inputs. Ex: 1.00 + 1.0 = 2.0

        INPUTS: number1,number2 (numbers in operation)
                operation ("*" or "/")
        OUTPUTS: answer to calculation with correct sig figs
        """
        number1, number2 = str(number1).lower(), str(number2).lower()
        numb1, numb2 = number1, number2
        # return value with fewest decimal places
        if "e" in number1:
            numb1, _ = number1.split("e")
        if "e" in number2:
            numb2, _ = number2.split("e")
        if ("." in number1) and ("." in number2):
            temp1, temp2 = numb1.split("."), numb2.split(".")
            dec1, dec2 = len(temp1[-1]), len(temp2[-1])
            min_dec = min(dec1, dec2)
        else:
            min_dec = 0
        # if this ^^ isn't met, then at least one number doesn't have a decimal
        evaluation = eval(number1+operation+number2)
        return "%.*f" % (min_dec, evaluation)
        # return value with fewest decimal places

    def round(self, number, sigfigs):
        """
        Round input number to given number of sig figs

        INPUTS: number
                sigfigs
        OUTPUTS: number with correct sig figs
        """
        multiple = "1." + (int(sigfigs)-1)*"0"
        sf1, sf2 = self.count(number), self.count(multiple)
        if sf1 < sf2:
            evaluation = eval(number+"*"+multiple)
            exp_string = "%.*e" % (sf2-1, evaluation)
            answer = exp_string
            return answer
        else:
            return self.__multiplicative_calc(number, multiple, "*")
        # minus one to account for decimal place
