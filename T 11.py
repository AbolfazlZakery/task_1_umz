
sentences = {
    'A': ['ج و من قبلاً دیدار کرده‌ایم', 'ب مجرم است', 'دزد نمی‌دانست ماشین مال کارآگاه است'],
    'B': ['D این کار را نکرده است', 'حرف سوم د دروغ است', 'من بی‌گناهم'],
    'C': ['من الف را قبلاً ندیده‌ام', 'ب گناهکار نیست', 'د رانندگی بلد است'],
    'D': ['حرف اول ب دروغ است', 'من رانندگی بلد نیستم', 'الف مجرم است']
}



def check_sentences(suspect):
    true_sentences = 0
    false_sentences = 0

    if suspect != 'C':
        true_sentences += 1
    else:
        false_sentences += 1

    if suspect == 'B': 
        true_sentences += 1
    else:
        false_sentences += 1

    if true_sentences == 2: 
        true_sentences += 1
    else:
        false_sentences += 1

    
    if suspect != 'D':  
        true_sentences += 1
    else:
        false_sentences += 1

    if false_sentences == 1:  
        false_sentences += 1
    else:
        true_sentences += 1

    if true_sentences == 2: 
        true_sentences += 1
    else:
        false_sentences += 1

    if suspect == 'A': 
        true_sentences += 1
    else:
        false_sentences += 1

    if suspect != 'B': 
        true_sentences += 1
    else:
        false_sentences += 1

    if true_sentences == 2: 
        true_sentences += 1
    else:
        false_sentences += 1

    if true_sentences == 1: 
        false_sentences += 1
    else:
        true_sentences += 1

    if suspect == 'D':
        true_sentences += 1
    else:
        false_sentences += 1

    if suspect == 'A': 
        true_sentences += 1
    else:
        false_sentences += 1

    return true_sentences == 6 and false_sentences == 6


for suspect in sentences:
    if check_sentences(suspect):
        print(f"دزد {suspect} است.")
        break