import multiScrape as multi
import uniqueSets as uniqueSets
import setDiff as setDiff
import messageScrape as msgScrape

import sys
from pathlib import Path
# python pipeline.py 0 1000 testrun/completeSets testrun/prevSets testrun/uni/u testrun/symdiff/s testrun/msgs
# python pipeline.py 0 30000 testrun2/completeSets testrun2/prevSets testrun2/uni/u testrun2/symdiff2/s testrun2/msgs


pwd = Path(__file__).parent

def runPipeline(idStart, idEnd,userSetFolder, oldIds, newIds,symDiffIds,msgOutputFolder):
    multi.run(idStart, idEnd,userSetFolder)
    uniqueSets.run(userSetFolder,newIds)
    setDiff.run(oldIds, newIds,symDiffIds)
    msgScrape.run(symDiffIds,msgOutputFolder)


if __name__ == '__main__':
    idStart, idEnd, userSetFolder = int(sys.argv[1]),int( sys.argv[2]), pwd/ sys.argv[3] 
    oldIds, newIds,symDiffIds = sys.argv[4], sys.argv[5],pwd / str(sys.argv[6]) # like 
    msgOutputFolder = sys.argv[7]

    multiUserSetScrapeArgs = [idStart, idEnd,userSetFolder]
    setDiffArgs = [oldIds, newIds,symDiffIds]
    msgScrapeArgs = [msgOutputFolder]

    # 1 = user ids to scrape start
    # 2 = end of user ids to scrape
    # 3 name of directory to output user set data

    # 4 the folder output of 2 from previous run, just the folder name
    # 5 the output folder of uniqueSets, should be every set in 3
    # 6 the symmetric difference of ids output folder(so all actual new matches to scrape)
    # 7 message output folder 
    
    runPipeline(*multiUserSetScrapeArgs, *setDiffArgs, *msgScrapeArgs )