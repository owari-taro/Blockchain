name: public(string[24])

@public
def __init__():
    self.name = "Satoshi Nakamoto"
@public
def change_name(new_name: string[24]):
    self.name = new_name
@public
def say_hello() -> string[64]:
    return concat( self.name,self.name)