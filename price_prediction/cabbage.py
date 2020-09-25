import tensorflow as tf
import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_handler import FileReader

class Cabbage:

    # year, avgTemp, minTemp, maxTemp, rainFall, avgPrice
    # 멤버 변수
    year: int = 0
    avgTemp: float = 0.0
    minTemp: float = 0.0
    maxTemp: float = 0.0
    rainFall: float = 0.0
    avgPrice: int = 0

    # 생성자
    def __init__(self):
        self.fileReader = FileReader()
        self.context = '/users/hong/desktop/sbaproject/cabbage/data/'
        self.X = tf.compat.v1.placeholder(tf.float32, shape=[None, 4])
        self.Y = tf.compat.v1.placeholder(tf.float32, shape=[None, 1])
        self.W = tf.Variable(tf.random.normal([4, 1]), name='weight')
        self.b = tf.Variable(tf.random.normal([1]), name='bias')
        self.H = tf.matmul(self.X, self.W) + self.b
        self.saver = tf.compat.v1.train.Saver()

    def new_model(self, payload) -> object:
        this = self.fileReader
        this.context = self.context
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    def create_tf(self, payload):
        xy = np.array(payload, dtype=np.float32)
        x_data = xy[:, 1:-1]  # feature
        y_data = xy[:, [-1]]  # price
        cost = tf.reduce_mean(tf.square(self.H - self.Y))
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(
            learning_rate=0.00005)
        train = optimizer.minimize(cost)
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())
        for step in range(10000):
            cost_, hypo_, train_ = sess.run([cost, self.H, train], feed_dict={
                                            self.X: x_data, self.Y: y_data})

            # if step % 500 == 0:
            #   print(f'step: {step}, cost: {cost_}')
            #   print(f'배추가격 : {hypo_[0]}')
        self.saver.save(sess, self.context + 'saved_model.ckpt')
        print('저장완료')

    def service(self):
        with tf.compat.v1.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())
            self.saver.restore(sess, self.context + 'saved_model.ckpt')
            data = [[self.avgTemp, self.minTemp, self.maxTemp, self.rainFall], ]
            arr = np.array(data, dtype=np.float32)
            dict = sess.run(tf.matmul(self.X, self.W) +
                            self.b, {self.X: arr[0:4]})
            # print(dict[0])
        return int(dict[0])


if __name__ == '__main__':
    m = Cabbage()
    dframe = m.new_model('price_data.csv')
    m.create_tf(dframe)
    m.service()
