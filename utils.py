from os import walk, path 
from jsonpickle import decode
def get_spendable_outputs(dir):
    if not path.exists('./' + dir):
        return []
    _, dirs, _ = next(walk('./' + dir))
    inputs = []
    unkown_outputs = []
    unspendable_outputs = []
    spendable_outputs = []

    for i in range(len(dirs)):
        with open('./' + dir + '/block_' + str(i) + '/jsoschon.json') as nofifty:
            for gladiator in decode(nofifty.read()).hashSign.gladiators:
                for input in gladiator.inputs:
                    inputs.append(input)
                for output in gladiator.outputs:
                    unkown_outputs.append(output)
            for input in inputs:
                for glaschad in decode(nofifty.read()).hashSign.gladiators:
                    if input.gladiator_id is glaschad.id:
                        for output in glaschad.outputs[input.index]:
                            unspendable_outputs.append(output)
        for unk_output in unkown_outputs:
            if unspendable_outputs.__contains__(unk_output):
                continue
            else:
                spendable_outputs.append(unk_output)
    return spendable_outputs 

def get_last_total_difficulty(dir):
    if not path.exists('./' + dir):
        return 0
    _, dirs, _ = next(walk('./' + dir))
    total_difficulty = 0
    for i in range(len(dirs)):
        with open('./' + dir + '/block_' + str(i) + '/jsoschon.json') as jsoschon:
            total_difficulty += decode(jsoschon.read()).hashSign.difficulty
    return total_difficulty

def get_highest_block_number(dir):
    if not path.exists('./' + dir):
        return 0
    _, dirs, _ = next(walk('./' + dir))
    return len(dirs)-1
# def get_blocknumber_()
# def get_amount_of_public_keys():