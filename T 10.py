from time import perf_counter
import string

text = """
"ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocal
passraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdn
onlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealed
staticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinal
lythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveCl
earIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectio
nsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypee
rasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobs
ervermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousp
rogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...

quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartifi
cialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgor
ithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervi
sedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetwo
rksgenerativeadversar...

blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2Pnet
workscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcon
tractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFid
ecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOs
decentralizedautonomousorganizati...
"""
key_list = ["and", "is", 'in', 'def', 'as', 'yield', 'assert', 'break', 'class', 'continue', 'except', 'finally', 'for',
            'from', 'global', 'import', 'nonlocal', 'pass', 'raise', 'return', 'try', 'while', 'with', 'or', 'del',
            'elif', 'else', 'if', 'not', 'True', 'False', 'None', 'async', 'await', 'lambda']


def decrypt_clue(text):
    list = []
    for i in key_list:
        if i in text:
            list.append(i)
    return list


answer1 = decrypt_clue(text)

puzzle = ['ali', 1233, 0, "", [], {}, 'False', '0', 'None', None, -1, [1, 2, 3], {'key': 'value'}, True, ' ', '[]',
          '[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}',
          '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}', 'True',
          'ali', '1234', 1, 0.1, -0.1]


def solve_puzzle(puzzle):
    list = []
    for i in puzzle:
        if i:
            list.append('True')
        elif i == None:
            list.append('None')
        else:
            list.append('False')
    return list


answer2 = solve_puzzle(puzzle)


def calculate_magic_numbers(start, end):
    x = 0.5
    return x * (end - start) + start


start = int(input("start: "))
end = int(input("end: "))
answer3_1 = str(calculate_magic_numbers(start, end))


def exam_numbers():
    list_question = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011',
                     '1100', '1101', '1110', '1111']
    list_answer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    finish_list = []
    start_time = perf_counter()
    for i in range(16):
        print(f"{list_question[i]}: ", end='')
        answer = input()
        if answer in list_answer[i]:
            finish_list.append('True')
        else:
            finish_list.append('False')
        end_time = perf_counter()
        if end_time - start_time >= 20:
            break
    return finish_list


answer3_2 = exam_numbers()


def try_passport(password):
    confirmation = [False, False, False, False]
    for i in password:
        if len(password) == 8:
            confirmation[3] = True
        if i in string.ascii_uppercase:
            confirmation[0] = True
        if i in string.ascii_lowercase:
            confirmation[1] = True
        if i in string.punctuation:
            confirmation[2] = True
    if False not in confirmation:
        return True
    else:
        return False


def check_pass():
    username = input("Enter your username: ").split(" ")
    password = input("Enter your password: ").split(" ")
    correct_password = []
    k = 0
    for i in password:
        if try_passport(i):
            correct_password.append(username[k])
            k += 1
        else:
            k += 1
    return correct_password


answer3_3 = check_pass()
answer3 = [answer3_1, answer3_2, answer3_3]


def unlock_vault(answer1, answer2, answer3, answer4="lataragi"):
    final_answer1 = str(answer1[0][0])
    final_answer2 = str(answer2[0][0])
    final_answer3 = str(answer3_1[0][0] + answer3_2[0][0] + answer3_3[0][0])
    final_answer4_1 = str(answer4[0])
    vault = final_answer1 + final_answer2 + final_answer3 + final_answer4_1
    print(vault)


unlock_vault(answer1, answer2, answer3)
