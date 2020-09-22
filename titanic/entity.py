from dataclasses import dataclass


@dataclass
class Entity:
    # def __init__(self, context, fname, train, test, id, label):
    #     self._context = context  # _ 1개는 default 접근을 의미, __ 2개는 private 접근 의미
    #     self.fname = fname
    #     self.train = train
    #     self.test = test
    #     self.id = id
    #     self.label = label
    #     self._context = context

    context: str = '/Users/hong/Desktop/sbaproject/data/'
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''

# contest get, set을 만듭니다.

    @property
    def context(self) -> str:
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

# fname get, set을 만듭니다.

    @property
    def fname(self) -> str:
        return self.fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

# train get, set을 만듭니다.
    @property
    def train(self) -> str:
        return self.train

    @train.setter
    def train(self, train):
        self._train = train

# test get, set을 만듭니다.
    @property
    def test(self) -> str:
        return self.test

    @test.setter
    def test(self, test):
        self._test = test

# id get, set을 만듭니다.
    @property
    def id(self) -> str:
        return self.id

    @id.setter
    def id(self, id):
        self._id = id

# label get, set을 만듭니다.
    @property
    def label(self) -> str:
        return self.label

    @label.setter
    def label(self, label):
        self._label = label
