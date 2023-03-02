from py2neo import Graph

class Query():
    def __init__(self):
        self.graph=Graph("http://localhost:7474", username="neo4j",password="123456")

    # 查询
    def run(self,cql):
        result=[]
        find_rela = self.graph.run(cql)
        for i in find_rela:
            result.append(i.items()[0][1])
        return result