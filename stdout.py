import sys
import io

def example_function(parameter):
    if(parameter % 5 == 0 and parameter % 3 == 0):
        variable = "FizzBuzz"
    elif(parameter % 5 == 0):
        variable = "Buzz"
    elif(parameter % 3 == 0):
        variable = "Fizz"
    else:
        variable = parameter
    print("result: " + str(variable))

def console_output(parameter):
    # record the pointer to the original terminal, VERY IMPORTANT!!!
    stdout_terminal = sys.stdout
    try:
        # change the stdout/err to point to the io.StringIO() object
        sys.stdout = sys.stderr = io.StringIO()
        try:
            # Your code here
            command = '''{}'''.format(parameter)
            exec(command)
            # End code here
        except Exception as error_msg:
            # printing here will ONLY print if stdout_terminal is restored..
            # .. and stdout_capture is returned
            print(str(error_msg))

        # now call the io.StringIO() object's "getvalue()" function for the string
        stdout_capture = sys.stdout.getvalue()
        # return the stdout to the original terminal, then return the captured string
        sys.stdout = stdout_terminal
        return stdout_capture
    
    # if it fails, should always fall back to the original terminal for stdout
    except:
        sys.stdout = stdout_terminal
        print("Terminal returned fatal error")
        return # if fatal error, return nothing
        # do NOT try returning some partial stdout abomination

output = console_output("example_function(15)")
print("Captured stdout:")
print(output)

output = console_output("example_nonexistential_function(15)")
print("Captured stdout:")
print(output)
