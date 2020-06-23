import sage.all
from sage.rings.finite_rings.integer_mod import square_root_mod_prime, Mod
from Crypto.Util.number import long_to_bytes, inverse
import gmpy2

n = 27772857409875257529415990911214211975844307184430241451899407838750503024323367895540981606586709985980003435082116995888017731426634845808624796292507989171497629109450825818587383112280639037484593490692935998202437639626747133650990603333094513531505209954273004473567193235535061942991750932725808679249964667090723480397916715320876867803719301313440005075056481203859010490836599717523664197112053206745235908610484907715210436413015546671034478367679465233737115549451849810421017181842615880836253875862101545582922437858358265964489786463923280312860843031914516061327752183283528015684588796400861331354873
e = 16
ct = 11303174761894431146735697569489134747234975144162172162401674567273034831391936916397234068346115459134602443963604063679379285919302225719050193590179240191429612072131629779948379821039610415099784351073443218911356328815458050694493726951231241096695626477586428880220528001269746547018741237131741255022371957489462380305100634600499204435763201371188769446054925748151987175656677342779043435047048130599123081581036362712208692748034620245590448762406543804069935873123161582756799517226666835316588896306926659321054276507714414876684738121421124177324568084533020088172040422767194971217814466953837590498718
d = inverse(e, n-1)
pt = pow(ct, d, n)
print(pt)
ans = []
pt = square_root_mod_prime(Mod(pt, n), n)
ans.append(pt)
ans.append(n-pt)
ans1 = []
for a in ans:
    pt = square_root_mod_prime(Mod(a, n), n)
    ans1.append(pt)
    ans1.append(n-pt)
ans2 = []
for a in ans1:
    pt = square_root_mod_prime(Mod(a, n), n)
    ans2.append(pt)
    ans2.append(n-pt)
for a in ans2:
    print(long_to_bytes(a))