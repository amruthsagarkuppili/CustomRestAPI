######################################
#                                    #
# @author Amruth Sagar Kuppili       #
#                                    #
######################################

import requests
from concurrent.futures import ThreadPoolExecutor
import json
class Sendrequest:

    def getResponse(self, url):
        return requests.get(url)

    # Merge all the requests, remove duplicates and sort according to criteria
    def merge(self, responseList, sortby, direction):
        mergedList = []
        statuscode = 0
        isreverse = False
        if(direction == 'desc'):
            isreverse = True
        for resp in responseList:
            print(resp)
            resp_json = resp.json()
            statuscode = resp.status_code
            mergedList += resp_json['posts']
        merged = {single['id'] : single for single in mergedList}
        finalList = [value for key, value in merged.items()]
        finalList.sort(key = lambda x:x[sortby], reverse=isreverse) #Sorting process
        print(type(finalList))
        finalresp = json.dumps(finalList, indent=4)
        return finalresp, statuscode




    # Pull the data from given API
    def hitLink(self, tags, sortby, direction):
        link = "https://api.hatchways.io/assessment/blog/posts?tag="
        tagList = tags.split(",")
        urlList = [link+x for x in tagList]
        with ThreadPoolExecutor(max_workers=10) as executor: # Threads for parallel request processing
            response_list = list(executor.map(self.getResponse, urlList))
        merged, statuscode = self.merge(response_list, sortby, direction)
        return merged, statuscode