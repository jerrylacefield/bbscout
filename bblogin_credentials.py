class Account:
    def __init__(self, ln):
        self.loginname = ln

    def setLoginName(self, ln):
        self.loginname = ln

    def getLoginName(self):
        return self.loginname
