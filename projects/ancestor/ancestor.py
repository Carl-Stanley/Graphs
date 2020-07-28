from collections import defaultdict
def earliest_ancestor(ancestors, starting_node):
    mapping = defaultdict(list)
    for link in ancestors:
        mapping[link[1]].append(link[0])

    thestack = []
    visited = set()
    thepath = []
    thestack.append([starting_node])
    while len(thestack) > 0:
        mainpath = thestack.pop()
        print(mainpath)
        mainnode = mainpath[-1]
        if mainnode not in visited:
            visited.add(mainnode)
            if neighbors := mapping[mainnode]:
                for neighbor in neighbors:
                    thestack.append(mainpath + [neighbor])
            elif len(mainpath) > 1:
                thepath.append(mainpath)
    if thepath:
        longest = max(sorted(thepath, key=lambda item:
                             item[-1]), key=lambda item: len(item))
        return longest[-1]
    return -1

ancestors_List = [(4, 8), (2, 9), (6, 8), (10, 12), (14, 15), (7, 2), (9, 8), (6, 5)]

earliest_ancestor(ancestors_List, 8)