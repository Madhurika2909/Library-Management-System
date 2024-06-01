def GameRec():
    infile = open("game.dat","r")
    outfile = open("basket.dat","w")
    try:
        lines = infile.readlines()
        for line in lines:
            if line.startswith("Basket Ball"):
                outfile.write(line)
                outfile.write("\n")
    except EOFError:
        pass
    infile.close()
    outfile.close()

GameRec()
