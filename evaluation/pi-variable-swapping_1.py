##PI pattern on line 20
def benchmark_graph_train(self):
    for batch_size in [16, 32, 64]:
      with tf.Graph().as_default():
        np_images, np_labels = random_batch(batch_size)
        dataset = tf.data.Dataset.from_tensors((np_images, np_labels)).repeat()
        images, labels = tf.data.make_one_shot_iterator(
            dataset).get_next()

        model = resnet50.ResNet50(data_format())
        logits = model(images, training=True)
        loss = tf.compat.v1.losses.softmax_cross_entropy(
            logits=logits, onehot_labels=labels)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0)
        train_op = optimizer.minimize(loss)

        init = tf.global_variables_initializer()
        with tf.Session() as sess:
          sess.run(init)
          (num_burn, num_iters) = (5, 10)
          for _ in range(num_burn):
            sess.run(train_op)
          start = time.time()
          for _ in range(num_iters):
            sess.run(train_op)
          self._report('train', start, num_iters, batch_size)