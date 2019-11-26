import tensorflow as tf
import numpy as np
from numpy import genfromtxt
import numpy

x_data = genfromtxt('./data/train_data.csv', delimiter=',')
#print(x_data)

y_data = genfromtxt('./data/train_result.csv', delimiter=',')
#print(y_data)

#########
# 신경망 모델 구성
######
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)


W1 = tf.Variable(tf.random_uniform([9, 10], 0., 1.))
b1 = tf.Variable(tf.zeros([10]))
L1 = tf.add(tf.matmul(X, W1), b1)
L1 = tf.nn.relu(L1)

W2 = tf.Variable(tf.random_uniform([10, 20], 0., 1.))
b2 = tf.Variable(tf.zeros([20]))
L2 = tf.add(tf.matmul(L1, W2), b2)
L2 = tf.nn.relu(L2)

W2 = tf.Variable(tf.random_uniform([20, 20], 0., 1.))
b2 = tf.Variable(tf.zeros([20]))
L3 = tf.add(tf.matmul(L2, W2), b2)
L3 = tf.nn.relu(L3)

W2 = tf.Variable(tf.random_uniform([20, 10], 0., 1.))
b2 = tf.Variable(tf.zeros([10]))
L4 = tf.add(tf.matmul(L3, W2), b2)
L4 = tf.nn.relu(L4)


W3 = tf.Variable(tf.random_uniform([10, 2], 0., 1.))
b3 = tf.Variable(tf.zeros([2]))
model = tf.add(tf.matmul(L4, W3), b3)


# 텐서플로우에서 기본적으로 제공되는 크로스 엔트로피 함수를 이용해
# 복잡한 수식을 사용하지 않고도 최적화를 위한 비용 함수를 다음처럼 간단하게 적용할 수 있습니다.
cost = tf.reduce_mean(
	tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=model))

optimizer = tf.train.AdamOptimizer(learning_rate=0.001)
train_op = optimizer.minimize(cost)


#########
# 신경망 모델 학습
######
saver = tf.train.Saver()
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
#print("!!!!!!!=================================")
saver.restore(sess, './model/model')
for step in range(1000000):
	#print("#####@@@@@!!!!!!!=================================")
	sess.run(train_op, feed_dict={X: x_data, Y: y_data})
	#print("2#####@@@@@!!!!!!!=================================")
	if ((step + 1) % 100 == 0):
		print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))
		#saver.save(sess, './model/model')

print(sess.run(cost, feed_dict={X: x_data, Y: y_data}))
saver.save(sess, './model/model')
#print("@@@@@!!!!!!!=================================")
#########
# 결과 확인
######
x_data2 = genfromtxt('./data/train_data.csv', delimiter=',')
y_data2 = genfromtxt('./data/train_result.csv', delimiter=',')

prediction = tf.argmax(model, 1)
target = tf.argmax(Y, 1)
#print('예측값:', sess.run(prediction, feed_dict={X: x_data2}))
#print('실제값:', sess.run(target, feed_dict={Y: y_data2}))

is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data2, Y: y_data2}))
###
x_data2 = genfromtxt('./data/test_data.csv', delimiter=',')
y_data2 = genfromtxt('./data/test_result.csv', delimiter=',')

prediction = tf.argmax(model, 1)
target = tf.argmax(Y, 1)

print('예측값:', sess.run(prediction, feed_dict={X: x_data2}))
print('실제값:', sess.run(target, feed_dict={Y: y_data2}))

csv_prediction = sess.run(prediction, feed_dict={X: x_data2})
numpy.savetxt("test_predict.csv", csv_prediction, delimiter=",")
csv_prediction = sess.run(target, feed_dict={Y: y_data2})
numpy.savetxt("test_real.csv", csv_prediction, delimiter=",")

is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data2, Y: y_data2}))