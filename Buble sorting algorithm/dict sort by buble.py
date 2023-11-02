def bublik(datastore):
    medical = datastore["office"]["medical"]
    i = len(medical)
    
    for x in range(0 , i - 1):
        for j in range(0, i - x - 1):
            if medical[j]["sq-ft"] > medical[j + 1]["sq-ft"]:
                medical[j]["sq-ft"] , medical[j + 1]["sq-ft"] = medical[j + 1]["sq-ft"] , medical[j]["sq-ft"]

datastore = { "office": {
    "medical": [
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }
    ],
    "parking": {
      "location": "premium",
      "style": "covered",
      "price": 750
    }
  }
}

bublik(datastore)

for room in datastore["office"]["medical"]:
    print(room)
