# پیدا کردن کلمات کلیدی در متن داده شده به نام mysterios

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


print(f"All keywords: {key_list}")
print(f"keywords in the text: {decrypt_clue(text)}")
