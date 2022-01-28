class ToYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
age=int(input("enter your age"))
if age<18:
    raise ToYoungException("please wait for some years to grow up")
