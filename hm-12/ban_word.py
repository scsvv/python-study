class BanWarningWord(Exception):
    """
    Exception, raised when banned word used.
    It has optional message attribute for the
    convenient problem describing.
    """
    message: str = 'Please, don\'t use banned word'

    def __init__(self, message=None):
        if message:
            self.message = message

    def __str__(self):
        return self.message


if __name__ == "__main__":
    try:
        baned_word = "cat"
        sentance: str = input("Enter your sentance: \n")
        sentance = sentance.split()
        
        if sentance.count(baned_word) != 0:
            raise BanWarningWord()
    except BanWarningWord as e:
        print(e)
        exit(-1)
    