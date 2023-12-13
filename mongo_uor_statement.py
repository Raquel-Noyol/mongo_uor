import pymongo

#host= "localhost"
#port="27017"
#time_out= 1000
#mongo_url="mongodb://"+host +":" + port + "/"

datos=[
        {
            "subject":{
                "summary": "This task is to test Multiple issues extracted from Python",
                "creator": "Benjamin Noyola",
                "key": "AGAI-17"
            },
            "Predicate":{
                "description": "This task is to test multiple calls using Jira api",
            },
            "object":    {
                "summary": "This task is to test Multiple issues extracted from Python",
                "created": "2023-11-17T21:31:18.418-0700",
                "creator": "Benjamin Noyola",
                "key": "AGAI-17"
            }
        },
        {
            "subject":{
                "summary": "This task is to test Multiples issues extracted from Python",
                "creator": "Benjamin Noyola",
                "key": "AGAI-18"
            },
            "Predicate":{
                "description": "This task is to test multipless calls using Jira api",
            },
            "object":    {
                "summary": "This task is to test Multiples issues extracted from Python",
                "created": "2023-12-17T21:31:18.418-0700",
                "creator": "Benjamin Noyola",
                "key": "AGAI-18"
            }
        }
]


"""
try:
    client = pymongo.MongoClient("mongodb+srv://benjamin_noyola:349NoBe1984@uorstatement.cwpypfd.mongodb.net/")

    client.server_info()
    print("Successful connection")
    
    #crear base de datos
    db=client["jira_mvp"]
    #crear coleccion
    col=db["uor_Statement"]

    #Insertar datos en coleccion
    col.insert_many(datos)

    #lista las bases de datos
    print (client.list_database_names())
    print (db["uor_Statement"])
    print (col.count_documents({}))
    
    #buscar docuemneto
    doc=col.find_one({"Predicate":{
        "description": "This task is to test multiple calls using Jira api"}})
    print(doc)
    client.close()

except pymongo.errors.ServerSelectionTimeoutError as error:
    print("Time exceeded"+error)
except pymongo.errors.ConnectionFailure as error:
    print("Failed to connect to mongodb"+error)

"""

client = pymongo.MongoClient("mongodb+srv://raquelnoyola3103:raquel03@cluster0.cjezdom.mongodb.net/")

#client=pymongo.MongoClient("mongodb+srv://raquelnoyola3103:SVlmi3k9d1zFvwtrvVl04wCTt7hzRCiTXmRwNTrgXMUSXgKbFA35F0kfR8w8LOQI@https://us-east-2.aws.data.mongodb-api.com/app/data-gssch/endpoint/data/v1")
client.server_info()
print("Successful connection")
    
#crear base de datos
db=client["uor_statements"]
#crear coleccion
col=db["uor_Statements_2"]
"""
#Insertar datos en coleccion
col.insert_many(datos)

    #lista las bases de datos
print (client.list_database_names())
print (db["uor_Statements"])
print (col.count_documents({}))
    
#buscar docuemneto
doc=col.find_one({"Predicate":{
    "description": "This task is to test multiple calls using Jira api"}})
print(doc)
client.close()

"""

"""
#api_key raquel = srE8LgNrCs9uoIhNcd0JfYutjQkuLqt1mzXOQw0nKjnw0TRL8pXrbLOktwhl3oU9


import requests
import json
# url = "https://us-east-1.aws.data.mongodb-api.com/app/data-hpgok/endpoint/data/v1/action/findOne"


### findOne
url="https://us-east-2.aws.data.mongodb-api.com/app/data-gssch/endpoint/data/v1/action/findOne"
payload = json.dumps({
    "collection": "uor_Statement",
    "database": "uor_statements",
    "dataSource": "Cluster0",
    "projection": {"_id":"656e8482855a9e4e798d0ab1"}

    
    })
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'srE8LgNrCs9uoIhNcd0JfYutjQkuLqt1mzXOQw0nKjnw0TRL8pXrbLOktwhl3oU9',
  'Accept': 'application/ejson'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

"""
"""
## find multiple
url="https://us-east-2.aws.data.mongodb-api.com/app/data-gssch/endpoint/data/v1/action/find"
payload = json.dumps({
    "collection": "uor_Statement",
    "database": "uor_statements",
    "dataSource": "Cluster0",
    #"projection": {"object":{"key":"AGAI-130"}
    #            }
    #})

    "filter": {
      "object": "key"
    },
    "sort": { "completedAt": 1 },
    "limit": 3
  })

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'srE8LgNrCs9uoIhNcd0JfYutjQkuLqt1mzXOQw0nKjnw0TRL8pXrbLOktwhl3oU9',
  'Accept': 'application/ejson'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

"""
"""
### insertOne
import requests
import json
url="https://us-east-2.aws.data.mongodb-api.com/app/data-gssch/endpoint/data/v1/action/insertOne"
payload = json.dumps({
    "collection": "uor_Statement",
    "database": "uor_statements",
    "dataSource": "Cluster0",
    "document": {
            "subject":{
                "summary": "This task is to test Multiple issues extracted from Python",
                "creator": "Benjamin Noyola",
                "key": "AGAI-17"
            },
            "Predicate":{
                "description": "This task is to test multiple calls using Jira api",
            },
            "object":    {
                "summary": "This task is to test Multiple issues extracted from Python",
                "created": "2023-11-17T21:31:18.418-0700",
                "creator": "Benjamin Noyola",
                "key": "AGAI-17"
            }
        },

    
    })
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'srE8LgNrCs9uoIhNcd0JfYutjQkuLqt1mzXOQw0nKjnw0TRL8pXrbLOktwhl3oU9',
  'Accept': 'application/ejson'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
"""
"""
###insertMany
import requests
import json
url="https://us-east-2.aws.data.mongodb-api.com/app/data-gssch/endpoint/data/v1/action/insertMany"
payload = json.dumps({
    "collection": "uor_Statement",
    "database": "uor_statements",
    "dataSource": "Cluster0",
    "documents": [{
            "subject":{
                "summary": "This task is to test Multiple issues extracted from Python",
                "creator": "Benjamin Noyola",
                "key": "AGAI-22"
            },
            "Predicate":{
                "description": "This task is to test multiple calls using Jira api",
            },
            "object":    {
                "summary": "This task is to test Multiple issues extracted from Python",
                "created": "2023-11-17T21:31:18.418-0700",
                "creator": "Benjamin Noyola",
                "key": "AGAI-22"
            }
        },
        {
            "subject":{
                "summary": "This task is to test Multiples issues extracted from Python",
                "creator": "Benjamin Noyola",
                "key": "AGAI-21"
            },
            "Predicate":{
                "description": "This task is to test multipless calls using Jira api",
            },
            "object":    {
                "summary": "This task is to test Multiples issues extracted from Python",
                "created": "2023-12-17T21:31:18.418-0700",
                "creator": "Benjamin Noyola",
                "key": "AGAI-21"
            }
        }
        ]
    
    })
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'srE8LgNrCs9uoIhNcd0JfYutjQkuLqt1mzXOQw0nKjnw0TRL8pXrbLOktwhl3oU9',
  'Accept': 'application/ejson'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
"""