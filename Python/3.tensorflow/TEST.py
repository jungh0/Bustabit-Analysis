import tensorflow as tf

data = [38,34,70644,66622,122883,122074,117,114,149805,153227,921,903]

input_c = 6
hidden_c = 500
output_c = 2

#신경망 모델 구성
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# 첫번째 가중치의 차원은 [특성, 히든 레이어의 뉴런갯수]
W1 = tf.Variable(tf.random_uniform([input_c, hidden_c], -1., 1.))
# 두번째 가중치의 차원을 [첫번째 히든 레이어의 뉴런 갯수, 분류 갯수
W2 = tf.Variable(tf.random_uniform([hidden_c, output_c], -1., 1.))

# 편향을 각각 각 레이어의 아웃풋 갯수로 설정합니다.
b1 = tf.Variable(tf.zeros([hidden_c]))
b2 = tf.Variable(tf.zeros([output_c]))

# 신경망의 히든 레이어에 가중치 W1과 편향 b1을 적용합니다
L1 = tf.add(tf.matmul(X, W1), b1)
L1 = tf.nn.relu(L1)

# 최종적인 아웃풋을 계산합니다.
# 히든레이어에 두번째 가중치 W2와 편향 b2를 적용하여 3개의 출력값을 만들어냅니다.
model = tf.add(tf.matmul(L1, W2), b2)

#데이터 불러오기
saver = tf.train.Saver()
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
saver.restore(sess, './model/model')

#결과 확인
kill = ((data[0] - data[1]) + 40) / 80
gold = ((data[2] - data[3]) + 40000) / 80000
get = ((data[4] - data[5]) + 40000) / 80000
wad = ((data[6] - data[7]) + 40) / 80
demage = ((data[8] - data[9]) + 40000) / 80000
cs = ((data[10] - data[11]) + 400) / 800

x_data = [[kill,gold,get,wad,demage,cs]]

prediction = tf.argmax(model, 1)
print('입력값:',data)
print('결과:',sess.run(prediction, feed_dict={X: x_data}))
if(sess.run(prediction, feed_dict={X: x_data}) == 1):
	print('예측값: 승' )
else:
	print('예측값: 패' )
