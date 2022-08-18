import shutil

maxAmount = 5000

for i in range(maxAmount):
    shutil.copy2('src/output/stuffyBunny/Unrevealed.json', 'src/output/stuffyBunny/{}.json'.format(i))