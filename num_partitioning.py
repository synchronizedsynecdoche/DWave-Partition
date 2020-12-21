from dwave.system import DWaveSampler, EmbeddingComposite
from neal import SimulatedAnnealingSampler
from pyqubo import Spin
from datetime import datetime
import pickle
#import numpy as np


USE_SIMULATOR = True
BACKUP = False

# Backup helper function
def backup(expName, topo, samples):

    if BACKUP:
        with open("data/"+expName + topo + str(datetime.now()), "wb") as f:
                
                pickle.dump(samples, f)

# Expects a space-seperated list of integers
arr = [int(x) for x in input(">>>").split()]

#np.random.randint(1,high=100,size=20)

print(f"Our set S is {arr}")

H = 0
for i in range(len(arr)):
    H += Spin(f'x_{i}') * arr[i]

H *= H 
model = H.compile()
bqm = model.to_bqm() # we need pyqubo>=1.0.0

if not USE_SIMULATOR:
    sampler = DWaveSampler()
    embedded = EmbeddingComposite(sampler)

    print("embedding and sampling...")
    sampleset = embedded.sample(bqm, num_reads=100)
    backup("num partitioning arr", "Chimera", arr)
    backup("num partitioning", "Chimera", sampleset)

else:
    simulator = SimulatedAnnealingSampler()
    sampleset = simulator.sample(bqm)
    decoded_samples = model.decode_sampleset(sampleset)
    

decoded_samples = model.decode_sampleset(sampleset)
best = min(decoded_samples, key=lambda x:x.energy)
# decision version of the partitioning problemm: does there exist a partition?
print(best.energy == 0)
# how "far away" are we?
print(best.energy)