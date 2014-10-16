#author guojingyu
#date      Oct 15, 2014

class RegistParamsInComplete(Exception):
    message = "User Register Parameter Incomplete : parameter '%(param)s' not found !"
    def __init__(self,**kwargs):
        super(RegistParamsInComplete,self).__init__(self.message%kwargs)
        self.msg = self.message%kwargs

class UsernameAlreadyUsed(Exception):
    message = "Register failed :username '%(username)s' already used "
    def __init__(self,**kwargs):
        super(UsernameAlreadyUsed,self).__init__(self.message%kwargs)
        self.msg = self.message%kwargs
        
class RegisterEmailALreadyUsed(Exception):
    message = "Register failed : email '%(email)s' already used "
    def __init__(self,**kwargs):
        super(RegisterEmailALreadyUsed,self).__init__(self.message%kwargs)
        self.msg = self.message%kwargs

class LoginParamsInComplete(Exception):
    message = "User Login Parameter Incomplete : parameter '%(param)s' not found "
    def __init__(self,**kwargs):
        super(LoginParamsInComplete,self).__init__(self.message%kwargs)
        self.msg = self.message%kwargs
        
class UsernamePasswordNotMatch(Exception):
    message = "Username Password not Match"
    def __init__(self):
        super(UsernamePasswordNotMatch,self).__init__(self.message)
        self.msg = self.message

class UserNotExist(Exception):
    message = "Login with invalid user : '%(user)s' "
    def __init__(self,**kwargs):
        super(UserNotExist,self).__init__(self.message%kwargs)
        self.msg = self.message%kwargs

'''
if __name__ == "__main__":
    
    a = LoginParamsInComplete(param="guojy@163.com")
    print a.msg
'''               


