

class Chamber:
    def __init__(self, name):
        self.name = "THIKL21720"
        self.state_controller = StateController()



class StateController:
    def __init__(self):
        self.dc = DataCollection()
        self.dp = DataPreprocessing()
        self.mi = ModelInference()
        self.m_state = self.dc

    def setState(self, state):
        print('loading state', state.__repr__())
        self.m_bRunBegin = False
        self.m_state = state

    def stateUpdate(self):
        self.m_state.stateBegin()
        self.m_bRunBegin = True




class State:
    def stateBegin(self):
        pass
    def stateEnd(self):
        pass
    def stateUpdate(self):
        pass


class DataCollection(State):

    def stateBegin(self):
        print("start DataCollection")

    def stateEnd(self):
        print("end DataCollection")

    def stateUpdate(self):
        print("update DataCollection")


class DataPreprocessing(State):
    def stateBegin(self):
        print("start DataPreprocessing")

    def stateEnd(self):
        print("end DataPreprocessing")

    def stateUpdate(self):
        print("update DataPreprocessing")

class ModelInference(State):
    def stateBegin(self):
        print("start ModelInference")

    def stateEnd(self):
        print("end ModelInference")

    def stateUpdate(self):
        print("update ModelInference")

class ResultUploading(State):
    def stateBegin(self):
        print("start ResultUploading")

    def stateEnd(self):
        print("end ResultUploading")

    def stateUpdate(self):
        print("update ResultUploading")
















