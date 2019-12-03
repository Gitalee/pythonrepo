import json as js
loadedData =js.loads(open("newmapping.json").read())
outputData=js.loads(open("D://task1//output//Ec2withEBS.json").read())
servicesNames=[]
finalArray=[]
finalDict = {}
for serviceData in outputData:
    dic = {}
    finalDict = {}
    for singleService in serviceData:
        servicesList = singleService.split("::")
        serviceType=servicesList[1]
        serviceMap = loadedData["ServiceMap"]
        #print(serviceMap)
        splitedType=servicesList[2].split("'")
        subType=splitedType[0]
        mapOfService = serviceMap[serviceType]
        propMap = loadedData['Mappings']
        if serviceType == 'EC2':
            specPropMap = propMap['EC2']
            if subType=='Instance':
                for main in mapOfService:
                    finalDict[serviceType]=main
                    for subMap in mapOfService[main]:
                        if subType == subMap:
                            finalDict[subType]=mapOfService[main][subMap]
                mapOfInstanceType=specPropMap['Instance']['InstanceType']
                for instanceType in mapOfInstanceType:
                    if instanceType==serviceData[singleService]['InstanceType']:
                        finalDict[instanceType]=mapOfInstanceType[instanceType]
                        finalArray.append(finalDict)
            elif subType=='Volume':
                for main in mapOfService:
                    finalDict[serviceType]=main
                    for subMap in mapOfService[main]:
                        if subType == subMap:
                            finalDict[subType]=mapOfService[main][subMap]
                            finalArray.append(finalDict)
print(finalArray)

