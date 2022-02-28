INVALID = -1
Vertices = list[int]
Relations = list[tuple[(int, int)]]
LinearOrders = list[int]

class Poset():

    def __init__(self, relations: Relations):
        # Vertex V with no relations is inputted as (V, -1)
        self.vertices = self._getVertices(relations)
        self.relations = self._getRelations(relations)
    
    def _getVertices(self, relations: Relations) -> Vertices:
        vertices = []
        for relation in relations:
            if relation[0] not in vertices and relation[0] != INVALID:
                vertices.append(relation[0])

            if relation[1] not in vertices and relation[1] != INVALID:
                vertices.append(relation[1]) 
        
        return sorted(vertices)

    def _getRelations(self, relations: Relations) -> Vertices:
        for relation in relations:
            if relation[1] == INVALID:
                relations.pop(relation)
        
        return sorted(relations)
    
    def transitiveReduce(self) -> None:
        # transitive reduction
        pass

    def generateLinearExtensions(self) -> LinearOrders:
        # generate linear extensions fast
        pass

class LinearOrder(Poset):

    def convertToPoset(self) -> Poset:
        return