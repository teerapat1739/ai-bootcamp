import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)

#  use session best practice
# print(tf.constant(2))
# define session
with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))

writer.close()

# session = tf.Session()
# print(session.run(x))
# session.close()
