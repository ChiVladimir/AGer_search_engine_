from tqdm import tqdm

Vowels = "аеиоуыеюя"

def procesString(string):
    tmp = string
    tmp.replace("  ", " ")
    tmp = tmp.split()
    
    return [tmp[i] for i in range(0, len(tmp), 2)]

PERFECTIVE_GERUND = [["в", "вши", "вшись"],
                     ["ив", "ивши", "ившись", "ыв", "ывши", "ывшись"]]
ADJECTIVE = procesString("ее (ee)   ие (ie)   ые (ye)   ое (oe)   ими (imi)   ыми (ymi)   ей (eì)   ий (iì)   ый (yì)   ой (oì)   ем (em)   им (im)   ым (ym)   ом (om)   его (ego)   ого (ogo)   ему (emu)   ому (omu)   их (ikh)   ых (ykh)   ую (uiu)   юю (iuiu)   ая (aia)   яя (iaia)   ою (oiu)   ею (eiu)")
PARTICIPLE = [ procesString("ем (em)   нн (nn)   вш (vsh)   ющ (iushch)   щ (shch)") ,
               procesString("ивш (ivsh)   ывш (yvsh)   ующ (uiushch)") ]
REFLEXIVE =procesString("ся (sia)   сь (s')")
VERB = [ procesString("ла (la)   на (na)   ете (ete)   йте (ìte)   ли (li)   й (ì)   л (l)   ем (em)   н (n)   ло (lo)   но (no)   ет (et)   ют (iut)   ны (ny)   ть (t')   ешь (esh')   нно (nno)") ,
        procesString("ила (ila)   ыла (yla)   ена (ena)   ейте (eìte)   уйте (uìte)   ите (ite)   или (ili)   ыли (yli)   ей (eì)   уй (uì)   ил (il)   ыл (yl)   им (im)   ым (ym)   ен (en)   ило (ilo)   ыло (ylo)   ено (eno)   ят (iat)   ует (uet)   уют (uiut)   ит (it)   ыт (yt)   ены (eny)   ить (it')   ыть (yt')   ишь (ish')   ую (uiu)   ю (iu)") ]
NOUN = procesString("а (a)   ев (ev)   ов (ov)   ие (ie)   ье ('e)   е (e)   иями (iiami)   ями (iami)   ами (ami)   еи (ei)   ии (ii)   и (i)   ией (ieì)   ей (eì)   ой (oì)   ий (iì)   й (ì)   иям (iiam)   ям (iam)   ием (iem)   ем (em)   ам (am)   ом (om)   о (o)   у (u)   ах (akh)   иях (iiakh)   ях (iakh)   ы (y)   ь (')   ию (iiu)   ью ('iu)   ю (iu)   ия (iia)   ья ('ia)   я (ia)")
SUPERLATIVE = procesString("ейш (eìsh)   ейше (eìshe)")
DERIVATIONAL = procesString("ост (ost)   ость (ost')")

def findeRV_R1_R2(word):
    ptr = 0
    ans = {"RV": len(word), "R1": len(word) + 1, "R2": len(word) + 1}
    
    for i in range(ptr, len(word)):
        if word[i] in Vowels:
            ptr += 1
            ans["RV"] = ptr
            break
        ptr += 1
    
    for i in range(ptr, len(word)):
        if word[i] not in Vowels:
            ptr += 1
            ans["R1"] = ptr
            break
        ptr += 1
    
    for i in range(ptr, len(word)):
        if word[i] in Vowels:
            ptr += 1
            break
        ptr += 1
        
    for i in range(ptr, len(word)):
        if word[i] not in Vowels:
            ptr += 1
            ans["R2"] = ptr
            break
        ptr += 1
        
    
    return ans

        
def StemSTEP1(word, RV_R1_R2):
    maxW = ""
    
    for i in PERFECTIVE_GERUND[0]:
        if(word.find("а" + i, RV_R1_R2["RV"]) != -1 or
           word.find("я" + i, RV_R1_R2["RV"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
                
    for i in PERFECTIVE_GERUND[1]:
        if(word.find(i, RV_R1_R2["RV"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
                
    if(maxW != ""):
        return word[:-len(maxW)]
    
    maxW = ""
    for i in REFLEXIVE:
        if(word.find(i, RV_R1_R2["RV"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
    
    if(maxW != ""):
        word = word[:-len(maxW)]
    
    maxW = ""
    for i in ADJECTIVE:
        if(word.find(i, RV_R1_R2["RV"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
    
    for i in PARTICIPLE[0]:
        for j in ADJECTIVE:
            if(word.find("а" + i + j, RV_R1_R2["RV"]) != -1 or
               word.find("я" + i + j, RV_R1_R2["RV"]) != -1):
                if(len(i + j) > len(maxW)):
                    maxW = i + j
                
    for i in PARTICIPLE[1]:
        for j in ADJECTIVE:
            if(word.find(i + j, RV_R1_R2["RV"]) != -1):
                if(len(i + j) > len(maxW)):
                    maxW = i + j
    
    if(maxW != ""):
        return word[:-len(maxW)]
    
    maxW = ""
    
    for i in VERB[0]:
        if(word.find("а" + i, RV_R1_R2["RV"]) != -1 or
           word.find("я" + i, RV_R1_R2["RV"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
                
    for i in VERB[1]:
        if(word.find(i, RV_R1_R2["RV"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
                
    if(maxW != ""):
        return word[:-len(maxW)]
    
    maxW = ""
    for i in NOUN:
        if(word.find(i, RV_R1_R2["RV"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
    
    if(maxW != ""):
        return word[:-len(maxW)]
    
    return word


def StemSTEP2(word):
    if(word[-1] == 'и'):
        return word[:-1]
    return word
    


def StemSTEP3(word, RV_R1_R2):
    
    maxW = ""
    for i in DERIVATIONAL:
        if(word.find(i, RV_R1_R2["RV"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
    
    if(maxW != ""):
        return word[:-len(maxW)]
    return word
    

def StemSTEP4(word, RV_R1_R2):
    
    maxW = ""
    for i in SUPERLATIVE:
        if(word.find(i, RV_R1_R2["R2"]) != -1):
            if(len(i) > len(maxW)):
                maxW = i
    
    if(maxW != ""):
        word = word[:-len(maxW)]
    
    if(word.find("нн", RV_R1_R2["RV"]) != -1):
        i = word.find("нн", RV_R1_R2["RV"])
        word = word[:i]
    
    if(word[-1] == "ь"):
        word = word[:-1]
    return word


def Stem(word):
    
    if(len(word) < 2):
        return word
    
    RV_R1_R2 = findeRV_R1_R2(word)
    
    word = StemSTEP1(word, RV_R1_R2)
    word = StemSTEP2(word)
    word = StemSTEP3(word, RV_R1_R2)
    word = StemSTEP4(word, RV_R1_R2)
    return word
    
    
    
    
