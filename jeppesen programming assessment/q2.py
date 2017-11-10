# QUESTION 2

# Write a function which takes a tree root node as input
# and writes out the number of each leaf node.
# (Each node holds one number and a list of child nodes.)
# (The exact data structure of the tree can be chosen freely.)


#tree data
dataTree = {
            2: (
                {
                    3: (
                        {
                            8
                        },
                        {
                            5
                        }
                    )
                },
                {
                    7
                },
                {
                    9: {
                        4: (
                        {
                            6
                        },
                        {
                            1
                        }
                    )
                    }
                }
            )
        }


import re

def findLeaf(data):
    for x in data.items():      # put nodes w no children into set[]
        return re.findall(r'\[([^]]*)\]',str(data))  # re to cleanup data
      
print findLeaf(dataTree)
