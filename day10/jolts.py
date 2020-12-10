
# Graph structure
class Adapter:
    def __init__(self, parent, number):
        self.number = number
        self.parents = [parent]
        self.childs = []
        self.paths = 1


# Function needed for tree traversal
def get_parent_count(adapterObj):
    if not adapterObj:
        return 1
    else:
        paths = 0
        for parent in adapterObj.parents:
            paths += get_parent_count(parent)
        return paths

with open("adapters", "r") as f:
    adapters = [int(adapter) for adapter in f.readlines()]
    adapters = sorted(adapters)
    device = max(adapters) + 3
    adapters.append(device)

    ### PART ONE ###
    differences = {}
    differences[min(adapters)] = 1
    for key, adapter in enumerate(adapters):
        if(key == len(adapters) - 1):
            break
        difference = abs(adapter - adapters[key+1])
        if(difference in differences):
            differences[difference] += 1
        else:
            differences[difference] = 1

    print("Difference product: %s" % differences[1] * differences[3])

    ### PART TWO ###
    queue = []
    for key, adapter in enumerate(adapters):

        copied_queue = queue.copy()
        popped = False

        if(adapter <= 3):
            tmpAdapterObj = Adapter(None, adapter)
            queue.append(tmpAdapterObj)


        for qkey, adapterObj in enumerate(copied_queue):
            if popped:
                queue[-1].parents.append(adapterObj)
                adapterObj.childs.append(queue[-1])
                queue[-1].paths += adapterObj.paths
            elif adapterObj.number != adapter and adapter-adapterObj.number <= 3:
                tmpAdapterObj = Adapter(adapterObj, adapter)
                adapterObj.childs.append(tmpAdapterObj)
                if(len(adapterObj.childs) > 1):
                    tmpAdapterObj.paths = adapterObj.paths * len(adapterObj.parents)
                else:
                    tmpAdapterObj.paths = adapterObj.paths
                queue.append(tmpAdapterObj)
                popped = True
            elif(adapter - adapterObj.number > 3):
                queue.pop(0)
        del copied_queue
    

    for key, adapterObj in enumerate(queue):
        if(adapterObj.number == device):
            print("Count during path creation: %s" % adapterObj.paths)

    ### Only run this code to check correctness. Takes a long time to traverse the tree.
    # solutions = 0
    # for key, adapterObj in enumerate(queue):
    #     if(adapterObj.number != device):
    #         continue
    #     else:
    #         solutions += get_parent_count(adapterObj)
    # print("Tree-Traversal: %s" % solutions)

