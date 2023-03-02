from query import Query

class QuestionTemplate():
    def __init__(self):
        self.q_template_dict={
            0:self.get_Calculation_method,
            1:self.get_Example,
            2:self.get_Advantage,
            3:self.get_Shortcoming,
            4:self.get_Characteristic,
            5:self.get_More_Details,
            6:self.get_Include_Nodes,
            7:self.get_Reference_Resources,
            8:self.get_Alias,
            9:self.get_Front_Relation,
            10:self.get_Succeed_Relation,
            11:self.get_Relation,
            12:self.get_Content,
            13:self.get_Fuction,
        }
        # 连接数据库
        self.graph = Query()
    def get_question_answer(self,question,template):
        # 如果问题模板的格式不正确则结束
        assert len(str(template).strip().split("\t"))==2
        template_id,template_str=int(str(template).strip().split("\t")[0]),str(template).strip().split("\t")[1]
        self.template_id=template_id
        self.template_str2list=str(template_str).split()

        # 预处理问题
        question_word,question_flag=[],[]
        for one in question:
            word, flag = one.split("/")
            question_word.append(str(word).strip())
            question_flag.append(str(flag).strip())
        assert len(question_flag)==len(question_word)
        self.question_word=question_word
        self.question_flag=question_flag
        self.raw_question=question
        # 根据问题模板来做对应的处理，获取答案
        answer=self.q_template_dict[template_id]()
        return answer

    # 获取节点名字
    def get_name(self,type_str):
        name_count=self.question_flag.count(type_str)
        if name_count==1:
            ## 获取nm在原问题中的下标
            tag_index = self.question_flag.index(type_str)
            ## 获取名称
            name = self.question_word[tag_index]
            return name
        else:
            result_list=[]
            for i,flag in enumerate(self.question_flag):
                if flag==str(type_str):
                    result_list.append(self.question_word[i])
            return result_list

    # 0:nm 计算方式
    def get_Calculation_method(self):
        node_name=self.get_name('nm')
        cql = f"match (m) where m.name='{node_name}'and m.Attribute2Key='计算方式' return m.Attribute2Value"
        answer = self.graph.run(cql)[0]
        final_answer=node_name+"的计算方式为：\n"+str(answer)
        return final_answer
    # 1:nm 例子
    def get_Example(self):
        node_name = self.get_name('nm')
        cql = f"match (m) where m.name='{node_name}'and m.Attribute2Key='例子' return m.Attribute2Value"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的例子有：\n" + str(answer)
        return final_answer
    # 2:nm 优点
    def get_Advantage(self):
        node_name = self.get_name('nm')
        cql = f"match (m) where m.name='{node_name}'and m.Attribute1Key='优点' return m.Attribute1Value"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的优点如下：\n" + str(answer)
        return final_answer
    # 3:nm 缺点
    def get_Shortcoming(self):
        node_name = self.get_name('nm')
        cql = f"match (m) where m.name='{node_name}'and m.Attribute2Key='缺点' return m.Attribute2Value"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的缺点如下：\n" + str(answer)
        return final_answer
    # 4:nm 特点
    def get_Characteristic(self):
        node_name = self.get_name('nm')
        cql = f"match (m) where m.name='{node_name}'and m.Attribute1Key='特点' return m.Attribute1Value"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的特点如下：\n" + str(answer)
        return final_answer
    # 5:nnt 细节
    def get_More_Details(self):
        node_name = self.get_name('nm')
        cql = f"match (m) where m.name='{node_name}'and m.Attribute1Key='细节' return m.Attribute1Value"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的细节如下：\n" + str(answer)
        return final_answer
    # 6:nm 包含节点
    def get_Include_Nodes(self):
        node_name = self.get_name('nm')
        cql = f"match (n)-[:包含]->(m) where n.name='{node_name}' return m.name"
        answer = self.graph.run(cql)
        answer_set = set(answer)
        answer_list = list(answer_set)
        answer = "、".join(answer_list)
        final_answer = node_name + "包含了如下内容：\n" + str(answer)
        return final_answer
    # 7:nm 参考
    def get_Reference_Resources(self):
        node_name = self.get_name('nm')
        cql = f"match (n)-[:参考]->(m) where n.name='{node_name}' return m.name"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "参考了如下内容：\n" + str(answer)
        return final_answer
    # 8:nm 别名
    def get_Alias(self):
        node_name = self.get_name('nm')
        cql = f"match (n)-[:别名]->(m) where n.name='{node_name}' return m.name"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的别名是：\n" + str(answer)
        return final_answer
    # 9:nm 前置关系
    def get_Front_Relation(self):
        node_name = self.get_name('nm')
        cql = f"match (n)-[:前置]->(m) where n.name='{node_name}' return m.name"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的前置是：\n" + str(answer)
        return final_answer
    # 10:nm 后继关系
    def get_Succeed_Relation(self):
        node_name = self.get_name('nm')
        cql = f"match (n)-[:后继]->(m) where n.name='{node_name}' return m.name"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的后继是：\n" + str(answer)
        return final_answer
    # 11:nm 二者关系
    def get_Relation(self):
        node_name_list = self.get_name('nm')
        cql = f"match(n)-[r]->(m)where n.name='{node_name_list[0]}'and m.name='{node_name_list[1]}' return type(r)"
        answer = self.graph.run(cql)[0]
        final_answer = node_name_list[0] + "与" + node_name_list[1] + "的关系是：\n" + str(answer)
        return final_answer
    # 12:nm 内容
    def get_Content(self):
        node_name = self.get_name('nm')
        cql = f"match (m) where m.name='{node_name}' return m.Detail"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的内容是：\n" + str(answer)
        return final_answer
    # 13:nm 作用
    def get_Fuction(self):
        node_name = self.get_name('nm')
        cql = f"match (m) where m.name='{node_name}'and m.Attribute1Key='作用' return m.Attribute1Value"
        answer = self.graph.run(cql)[0]
        final_answer = node_name + "的作用是：\n" + str(answer)
        return final_answer