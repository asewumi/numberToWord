'''
    This is python module that convert number into it corresponding word format
'''

PLACE_VALUE = ['', 'thousand', 'million', 'billion', 'trillion']

NUMBER_WORD = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
               'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
               'eighteen', 'nineteen', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy',
               'eighty', 'ninty'
              ]

class CharacterLengthException(Exception):
    pass

class Convert(object):

    def __init__(self, number):
        ''' Collecting the number input and testing the input'''
        if not isinstance(number , int):
            raise TypeError('An integer must be passed %s passed'%(type(number)))
        if len(str(number)) > 15:
            raise CharacterLengthException("Number character can only be 15 character or less")
        self.number = number
        self.word = ''

    def convert_to_word(self):
        ''' This convert the whole number to word '''
        number = int(self.number)
        digit_len = len(str(self.number))
        word_format = []
        digit_group = []
        if digit_len > 3:
            # if digit is > 3 split them in schuncks of 3
            digit_group = self.group_number()
            digit_group_len = len(digit_group)
            counter = 0
            while digit_group_len > 0:
                #for each digit group perform hundred tens and units conversion
                number_chunk = digit_group[counter]
                number_word = self.hundred_tens_units(number_chunk)
                if number_word != '':
                    main_place = PLACE_VALUE[counter]
                    number_word += ' '+  main_place
                word_format.append(number_word)
                #word_format.append( main_place)
                counter += 1
                digit_group_len -= 1
            self.word = ' '.join(word_format[::-1])
            #print(word_format[::-1])
        else:
            self.word = self.hundred_tens_units(number)

        return self.word

    def hundred_tens_units(self, number_chunk):
        ''' hundred tens and units conversion '''
        divisor = 100
        self.word = ""
        dividen = int(number_chunk)
        COMMON_INDEX = 2
        step = 0
        while divisor > 0:
            quotent = dividen // divisor
            remainder = dividen % divisor
            step += 1
            if step == 1:
                if remainder == 0:
                    if quotent > 0:
                        self.word += NUMBER_WORD[quotent] + ' hundred '
                    return self.word
                else:
                    if quotent > 0:
                        self.word += NUMBER_WORD[quotent] + ' hundred and '
                    dividen = remainder
            elif step == 2:
                if remainder == 0:
                    if quotent > 0:
                        if quotent == 1:
                            quotent = int(str(quotent) + str(remainder))
                            self.word += NUMBER_WORD[quotent]
                        else:
                            quotent = int(str(COMMON_INDEX) + str(quotent - COMMON_INDEX))
                            self.word += NUMBER_WORD[quotent]
                    return self.word
                else:
                    if quotent > 0:
                        if quotent == 1:
                            quotent = int(str(quotent) + str(remainder))
                            self.word += NUMBER_WORD[quotent]
                            return self.word
                        else:
                            quotent = int(str(COMMON_INDEX) + str(quotent - COMMON_INDEX))
                        self.word += NUMBER_WORD[quotent] + '-'
                        dividen = remainder
            elif step == 3:
                if remainder == 0:
                    if quotent > 0:
                        self.word += NUMBER_WORD[quotent]
            else:
                pass
            divisor /= 10     
        return self.word

    def group_number(self):
        ''' this function group into chunck of threes from right to left '''
        digit_group = []
        while self.number > 0:
            remainder = self.number % 1000
            digit_group.append(remainder)
            self.number /= 1000
        return digit_group





if __name__ == '__main__':
    value = 123423456
    result = Convert(value)
    print(result.convert_to_word())
