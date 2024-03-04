local ret = require("flag")

io.write("Input flag: ")
flag = io.read("*l")
if ret.check(flag, 'ThisIsAFlag') then
   print("Correct!")
else
   print("Wrong...")
end
