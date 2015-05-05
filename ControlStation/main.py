from PS3InputMethod import PS3InputMethod

# Declare the inputMethod
im = PS3InputMethod("/dev/input/js0")

# Enter the listening loop
im.doListenLoop()
