INVALID = -1

class Poset:

    def __init__(self, relations: list[tuple[(int, int)]]):
        # Vertex V with no relations is inputted as (V, -1)
        self.vertices = self._getVertices(relations)
        self.relations = self._getRelations(relations)
    
    def _getVertices(self, relations: list[tuple[(int, int)]]) -> list[int]:
        vertices = []
        for relation in relations:
            if relation[0] not in vertices and relation[0] != INVALID:
                vertices.append(relation[0])

            if relation[1] not in vertices and relation[1] != INVALID:
                vertices.append(relation[1]) 
        
        return sorted(vertices)

    def _getRelations(self, relations: list[tuple[(int, int)]]) -> list[tuple[(int, int)]]:
        for relation in relations:
            if relation[1] == INVALID:
                relations.pop(relation)
        
        return sorted(relations)

    # transitive reduction?
    # get linear orders -> list[int]?

# class HammockPoset?