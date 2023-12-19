import gmpy2
from Crypto.Util.number import *
flag = b"flag{It's-the_true-flag--have0a0try}"
assert len(flag) == 35
p, q = [getPrime(2048) for _ in "__"]
n = p*q
e = 0x10001
c = gmpy2.powmod(bytes_to_long(flag), e, n)
print(p)
print(c)
#24724324630507415330944861660078769085865178656494256140070836181271808964994457686409910764936630391300708451701526900994412268365698217113884698394658886249353179639767806926527103624836198494439742123128823109527320850165486500517304731554371680236789357527395416607541627295126502440202040826686102479225702795427693781581584928770373613126894936500089282093366117940069743670997994742595407158340397268147325612840109162997306902492023078425623839297511182053658542877738887677835528624045235391227122453939459585542485427063193993069301141720316104612551340923656979591045138487394366671477460626997125944456537
#81726634457025933493485206743769779940269570742900097485184878251355346022424868238578456135549425397616225402340585844371803593460556984024650309769461570748608318998542995021677448070083577602122495119674168772126999587975753451714761206268469646378774469842742753714654782795976585695567702829751240527011964009714784316678393727006332207045485304544485628746947783872981967877128192751687730445580364207229995126556660589242620373959816980361430171285397680063298000429198178424728683657487734034703263623509295077911943130220139613373523732737828236310866574678131151172480202862095107391869397466301529173654914865326850340543189993299736020997346984009760817883599354638938782621088626258967731017172747884313446701451048617209715956657005452651668757201082647749261481761387146958933131536848257329609310146791884071145122527298023332570138748193415685656349344912741688078202084961365743372638231527944088800705310107658991346327312875378209817061037497839274161928125465052019641706945640985522678131079917401217928932835026405209353040125582943607319903056318780124035791783141766737798271974835992564468028719897769291587514372189061000705413521016770477724787526444729816448971088666396735980599723517100152873305846615
