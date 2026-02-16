import cmd
import shlex


class nullshell(cmd.Cmd):
    intro = "Welcome to My Custom Shell. Type help or ? to list commands.\n"
    prompt = "(my-shell) "

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

    def do_exit(self, arg):
        print("Goodbye, friend!")
        return True # Returning True exits the cmdloop

    do_EOF = do_exit

if __name__ == "__main__":
    nullshell().cmdloop()