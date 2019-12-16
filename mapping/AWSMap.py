#pip install pyyaml

import json as js
import yaml

loadedData =js.loads(open("newmapping.json").read())
outputData=js.loads(open("C://Users//personal//Desktop//pythonrepo//task1//output//2ec2withebs.json").read())
servicesNames=[]
finalArray=[]
finalGcpArray=[]
count=0
for serviceData in outputData:
    dic = {}
    finalDict = {}
    finalGcpDict = {}

    for singleService in serviceData:
        servicesList = singleService.split("::")
        serviceType=servicesList[1]
        properties = loadedData["Properties"]
        #print(serviceMap)
        splitedType=servicesList[2].split("'")
        subType=splitedType[0]
        mappings = loadedData['Mappings']

        serviceProperties = serviceData[singleService]
        propBlankDict = {}
        prop={}
        for property in serviceProperties:
            if property in properties:
                if property in mappings:
                    propBlankDict[properties[property]] = mappings[property][serviceProperties[property]]
                else:propBlankDict[properties[property]]=serviceProperties[property]#####does not have corresponding gcp values
        Type =""
        services=loadedData['Services']
        subservices=loadedData['Subservices']
        Type+=services[serviceType]+".v1."+subservices[subType]
        finalGcpDict['name']=Type+str(count)
        count=count+1
        finalGcpDict['type']=Type
        finalGcpDict['properties']=propBlankDict
        finalGcpArray.append(finalGcpDict)

#print (finalGcpArray)
tempFileName = "gcpVolume.yaml"
FinalTempName = "configurationfinalfile.yaml"
d = {'resources':[]}

with open(tempFileName, 'r') as stream:

        docs = yaml.load_all(stream, Loader=yaml.FullLoader)
        dictionary = yaml.safe_load(stream)
        print(type(dictionary))
        for i in finalGcpArray:
            resourcesList=list(dictionary['resources'])[0]
            z=i['properties']
            zz=resourcesList['properties'].update(z)
            i['properties']=resourcesList['properties']
            resourcesList.update(i)
            dic.append(resourcesList)
            break
        d['resources'] = dic
        print(d)
        x={'resources': [{'name': 'compute.v1.disk2', 'type': 'compute.v1.disk', 'properties': {'zone': 'us-east-1a', 'machineType': 'm1-micro', 'disks': [{'deviceName': 'boot', 'type': 'PERSISTENT', 'boot': True, 'initializeParams': {'sourceImage': 'projects/debian-cloud/global/images/family/debian-9'}}], 'networkInterfaces': [{'network': 'global/networks/default'}], 'sizeGb': '5'}}, {'name': 'compute.v1.disk2', 'type': 'compute.v1.disk', 'properties': {'zone': 'us-east-1a', 'machineType': 'm1-micro', 'disks': [{'deviceName': 'boot', 'type': 'PERSISTENT', 'boot': True, 'initializeParams': {'sourceImage': 'projects/debian-cloud/global/images/family/debian-9'}}], 'networkInterfaces': [{'network': 'global/networks/default'}], 'sizeGb': '5'}}, {'name': 'compute.v1.disk2', 'type': 'compute.v1.disk', 'properties': {'zone': 'us-east-1a', 'machineType': 'm1-micro', 'disks': [{'deviceName': 'boot', 'type': 'PERSISTENT', 'boot': True, 'initializeParams': {'sourceImage': 'projects/debian-cloud/global/images/family/debian-9'}}], 'networkInterfaces': [{'network': 'global/networks/default'}], 'sizeGb': '5'}}]}
        print (type(d))
        print (type(x))

with open(r'configurationfinalfile.yaml', 'w') as file:
    print (d)
    dd=d.copy()
    if x==d:
        print("hi")
    documents = yaml.dump(dd, file)
    print (documents)
