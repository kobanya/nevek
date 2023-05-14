
import magyar
import random

telepulesek = random.sample(magyar.telepules, k=80)  # 55 nem ismétlődő magyar település listája
tordelt = magyar.tordel(telepulesek, 8)              # soronként 8 elemmel azonnal kiírva a terminálra

# a tördelt listát azonnal kiírja, nincs szükség PRINT parancsra



