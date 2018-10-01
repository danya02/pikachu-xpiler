import sys
inp = open(sys.argv[1])
program = inp.read()
inp.close()
program = program.split('\n')
program = ['']+program
progcounter = 1

DEBUG=False


realprint=print
def print(*args, real=False, **kwargs):
    if DEBUG or real:
        realprint(*args, **kwargs)

print(f'Running {sys.argv[1]}...')
pipikachu = []
pikapikachu = []
while progcounter in range(len(program)):
    noadd=False
    command = program[progcounter]
    print(f'Command is: "{command}"')
    if command:
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
            operations = {'pi pika':'{s}.append({s}[-1]+{s}[-2])',
                    'pika pi':'{s}.append({s}[-1]+{s}[-2])',
                    'pi pikachu':'{s}.append({s}[-1]*{s}[-2])',
                    'pikachu':'{s}.append({s}[-2]/{s}[-1])',
                    'pika pikachu':'print("output of pika pikachu is:");print({s}.pop(),real=True)',
                    'pi pika':'print("output of pi pika is:");print(chr({s}.pop()),real=True)'}
            for i in operations:
                if command==i+' pi pikachu' or command==i+' pika pikachu':
                    exec(operatons[' '.join(command.split()[:2])].format(s=stack))
                    break
            else:
                exec('{s}.append(len(command.split())-2)'.format(s=stack))

    if not noadd:
        progcounter+=1
    if progcounter>len(program):
        exit()
