import cmd
import shlex


class function():
    def do_hello(self, arg):
        if arg:
            print(f"Hello, {arg}")
        else:
            print("Hello, stranger!")
    
    def do_adding(self, arg):
        try:
            a, b = map(int, shlex.split(arg))
            print(f"Result: {a + b}")
        except ValueError:
            print("you cannot add letters")
    
    def do_is(self, arg):
        try:
            args =  shlex.split(arg)
            if not args:
                return
            
            val = int(args[0])

            if val % 2 !=0:
                print(f"{val}, is odd")
            else:
                 print(f"{val}, is even")
        except ValueError:
            print("unknown")

    def do_echo(self, arg):
        try:
            args =  shlex.split(arg)
            if not args:
               return
            
            cal = str(args[0]).lower()
            if cal == "text":
             print(f"{cal}")
            else: 
                print(f"You typed: {cal}")
        except UnicodeWarning:
            print("non text character")

class input(cmd.Cmd):
    intro = "Welcome to My Custom Shell. Type help or ? to list commands.\n"
    prompt = "(my-shell) "

    def __init__(self):
        super().__init__()
        self.commands = function()  

    def default(self, line):
        parts = shlex.split(line)
        if not parts:
            return
        

        cmd_reader = parts[0]
        arg_string = " ".join(parts[1:])

        method = f"do_{cmd_reader}"
        command = getattr(self.commands, method, None)

        if command and callable(command):
            return command(arg_string)
        else:
            print(f"Unknown Commands: {line}")

    def do_exit(self, arg):
        print("Goodbye, friend!")
        return True

           
if __name__ == "__main__":       
 input().cmdloop()
        