import json as js
loadedData =js.loads(open("newmapping.json").read())
outputData=js.loads(open("D://task1//output//EC2.json").read())
servicesNames=[]
finalArray=[]
finalDict = {}
for serviceData in outputData:
    dic = {}
    servicesList=str(serviceData.keys())
    servicesList = servicesList.split("::")
    name=servicesList[1]
    serviceMap = loadedData["ServiceMap"]
    #print(serviceMap)
    serviceTypes=serviceMap[name]
    serviceType=servicesList[2].split("'")
    for serviceMap in serviceTypes:
        finalDict[name]=serviceMap
        d=serviceTypes[serviceMap]
        for ty in d:
            if ty == serviceType[0]:
                finalDict[serviceType[0]]=d[ty]
    for c in serviceData:
        r=serviceData[c]
        v=loadedData['Mappings']
        vv=v[name]
        b=r['InstanceType']
        q=vv['InstanceType']
        finalDict[b]=q[b]
print(finalDict)

