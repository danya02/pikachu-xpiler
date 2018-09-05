import sys
print(f'Running {sys.argv[1]}...')
inp = open(sys.argv[1])
program = inp.read()
inp.close()
program = program.split('\n')
program = ['']+program
progcounter = 1

pipikachu = []
pikapikachu = []
while 1:
    noadd=False
    command = program[progcounter]
    if command=='pi pika':
        print('Top of PiPikachu inserted into PikaPikachu!')
        pikapikachu.append(pipikachu[-1])
    elif command=='pika pi':
        print('Top of PikaPikachu inserted into PiPikachu!')
        pipikachu.append(pikapikachu[-1])
    elif command=='pikachu pikachu':
        print('Comparing stacks for equal...')
        if pipikachu[-1]==pikapikachu[-1]:
            progcounter = len(program[progcounter+1].split())
            print(f'Tops are equal, jumping to line {progcounter}!')
            noadd=True
    elif command=='pika pika':
        print('Comparing stacks for unequal...')
        if pipikachu[-1]!=pikapikachu[-1]:
            progcounter = len(program[progcounter+1].split())
            print(f'Tops are unequal, jumping to line {progcounter}!')
            noadd=True
    else:
        stack = ''.join(command.split()[-2:])
        if command.startswith('pi pika '):
            print(f'Adding together two values on {stack}!')

            exec('{s}.append({s}[-1]+{s}[-2])'.format(s=stack))
        elif command.startswith('pika pi '):
            print(f'Subtracting two values on {stack}!')
            exec('{s}.append({s}[-1]-{s}[-2])'.format(s=stack))
        elif command.startswith('pi pikachu '):
            print(f'Multiplying two values on {stack}!')
            exec('{s}.append({s}[-1]*{s}[-2])'.format(s=stack))
        elif command.startswith('pikachu '):
            print(f'Dividing two values on {stack}!')
            exec('{s}.append({s}[-2]/{s}[-1])'.format(s=stack))
        elif command.startswith('pika pikachu '):
            print(f'Printing top of {stack}!')
            exec('print({s}.pop())'.format(s=stack))
        elif command.startswith('pi pika '):
            print(f'Printing chr of top of {stack}!')
            exec('print(chr({s}.pop()))'.format(s=stack))
        else:
            print(f'Pushing {len(command)-2} to {stack}!')
            exec('{s}.append(len(command)-2)'.format(s=stack))

    if not noadd:
        progcounter+=1
    if progcounter>len(program):
        exit()
