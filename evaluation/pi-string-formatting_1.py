def test_ModelCheckpoint(self):
    if h5py is None:
      return  # Skip test if models cannot be saved.

    layers = [
        keras.layers.Dense(NUM_HIDDEN, input_dim=INPUT_DIM, activation='relu'),
        keras.layers.Dense(NUM_CLASSES, activation='softmax')
    ]
    model = testing_utils.get_model_from_layers(layers, input_shape=(10,))
    model.compile(
        loss='categorical_crossentropy', optimizer='rmsprop', metrics=['acc'])

    temp_dir = self.get_temp_dir()
    self.addCleanup(shutil.rmtree, temp_dir, ignore_errors=True)

    filepath = os.path.join(temp_dir, 'checkpoint.h5')
    (x_train, y_train), (x_test, y_test) = testing_utils.get_test_data(
        train_samples=TRAIN_SAMPLES,
        test_samples=TEST_SAMPLES,
        input_shape=(INPUT_DIM,),
        num_classes=NUM_CLASSES)
    y_test = np_utils.to_categorical(y_test)
    y_train = np_utils.to_categorical(y_train)
    # case 1
    monitor = 'val_loss'
    save_best_only = False
    mode = 'auto'

    model = keras.models.Sequential()
    model.add(
        keras.layers.Dense(
            NUM_HIDDEN, input_dim=INPUT_DIM, activation='relu'))
    model.add(keras.layers.Dense(NUM_CLASSES, activation='softmax'))
    model.compile(
        loss='categorical_crossentropy', optimizer='rmsprop', metrics=['acc'])

    cbks = [
        keras.callbacks.ModelCheckpoint(
            filepath,
            monitor=monitor,
            save_best_only=save_best_only,
            mode=mode)
    ]
    model.fit(
        x_train,
        y_train,
        batch_size=BATCH_SIZE,
        validation_data=(x_test, y_test),
        callbacks=cbks,
        epochs=1,
        verbose=0)
    assert os.path.exists(filepath)
    os.remove(filepath)

    # case 2
    mode = 'min'
    cbks = [
        keras.callbacks.ModelCheckpoint(
            filepath,
            monitor=monitor,
            save_best_only=save_best_only,
            mode=mode)
    ]
    model.fit(
        x_train,
        y_train,
        batch_size=BATCH_SIZE,
        validation_data=(x_test, y_test),
        callbacks=cbks,
        epochs=1,
        verbose=0)
    assert os.path.exists(filepath)
    os.remove(filepath)

    # case 3
    mode = 'max'
    monitor = 'val_acc'
    cbks = [
        keras.callbacks.ModelCheckpoint(
            filepath,
            monitor=monitor,
            save_best_only=save_best_only,
            mode=mode)
    ]
    model.fit(
        x_train,
        y_train,
        batch_size=BATCH_SIZE,
        validation_data=(x_test, y_test),
        callbacks=cbks,
        epochs=1,
        verbose=0)
    assert os.path.exists(filepath)
    os.remove(filepath)

    # case 4
    save_best_only = True
    cbks = [
        keras.callbacks.ModelCheckpoint(
            filepath,
            monitor=monitor,
            save_best_only=save_best_only,
            mode=mode)
    ]
    model.fit(
        x_train,
        y_train,
        batch_size=BATCH_SIZE,
        validation_data=(x_test, y_test),
        callbacks=cbks,
        epochs=1,
        verbose=0)
    assert os.path.exists(filepath)
    os.remove(filepath)

    # Case: metric not available.
    cbks = [
        keras.callbacks.ModelCheckpoint(
            filepath,
            monitor='unknown',
            save_best_only=True)
    ]
    model.fit(
        x_train,
        y_train,
        batch_size=BATCH_SIZE,
        validation_data=(x_test, y_test),
        callbacks=cbks,
        epochs=1,
        verbose=0)
    # File won't be written.
    assert not os.path.exists(filepath)

    # case 5
    save_best_only = False
    period = 2
    mode = 'auto'

    filepath = os.path.join(temp_dir, 'checkpoint.{epoch:02d}.h5')
    cbks = [
        keras.callbacks.ModelCheckpoint(
            filepath,
            monitor=monitor,
            save_best_only=save_best_only,
            mode=mode,
            period=period)
    ]
    model.fit(
        x_train,
        y_train,
        batch_size=BATCH_SIZE,
        validation_data=(x_test, y_test),
        callbacks=cbks,
        epochs=4,
        verbose=1)
    assert os.path.exists(filepath.format(epoch=2))
    assert os.path.exists(filepath.format(epoch=4))
    os.remove(filepath.format(epoch=2))
    os.remove(filepath.format(epoch=4))
    assert not os.path.exists(filepath.format(epoch=1))
    assert not os.path.exists(filepath.format(epoch=3))

    # Invalid use: this will raise a warning but not an Exception.
    keras.callbacks.ModelCheckpoint(
        filepath,
        monitor=monitor,
        save_best_only=save_best_only,
        mode='unknown')

    # Case 6: `ModelCheckpoint` with a combination of `save_freq` and `period`.
    # Though `period` is deprecated, we're testing it for
    # backward-compatibility.
    filepath = os.path.join(temp_dir, 'checkpoint.epoch{epoch:02d}.h5')
    cbks = [
        keras.callbacks.ModelCheckpoint(
            filepath, monitor=monitor, mode=mode, save_freq='epoch', period=5)
    ]
    assert not os.path.exists(filepath.format(epoch=0))
    assert not os.path.exists(filepath.format(epoch=5))
    model.fit(
        x_train,
        y_train,
        batch_size=2,
        validation_data=(x_test, y_test),
        callbacks=cbks,
        epochs=10,
        verbose=1)
    assert not os.path.exists(filepath.format(epoch=1))
    assert not os.path.exists(filepath.format(epoch=2))
    assert not os.path.exists(filepath.format(epoch=3))
    assert not os.path.exists(filepath.format(epoch=4))
    assert os.path.exists(filepath.format(epoch=5))
    assert not os.path.exists(filepath.format(epoch=6))
    assert os.path.exists(filepath.format(epoch=10))
    os.remove(filepath.format(epoch=5))
    os.remove(filepath.format(epoch=10))

    # Case 7: `ModelCheckpoint` with an integer `save_freq`
    filepath = os.path.join(temp_dir, 'checkpoint.epoch{epoch:02d}.h5')
    cbks = [
        keras.callbacks.ModelCheckpoint(
            filepath,
            monitor=monitor,
            save_best_only=save_best_only,
            mode=mode,
            save_freq=15,
            period=100)  # The period should be ignored (this test tests this).
    ]
    assert not os.path.exists(filepath.format(epoch=3))
    model.fit(
        x_train,
        y_train,
        batch_size=2,
        validation_data=(x_test, y_test),
        callbacks=cbks,
        epochs=10,
        verbose=1)
    assert not os.path.exists(filepath.format(epoch=1))
    assert not os.path.exists(filepath.format(epoch=2))
    assert os.path.exists(filepath.format(epoch=3))
    assert not os.path.exists(filepath.format(epoch=4))
    assert not os.path.exists(filepath.format(epoch=5))
    assert os.path.exists(filepath.format(epoch=6))
    assert not os.path.exists(filepath.format(epoch=7))
    assert not os.path.exists(filepath.format(epoch=8))
    assert os.path.exists(filepath.format(epoch=9))
    os.remove(filepath.format(epoch=3))
    os.remove(filepath.format(epoch=6))
    os.remove(filepath.format(epoch=9))

    # Case 8: `ModelCheckpoint` with valid and invalid save_freq argument.
    with self.assertRaisesRegexp(ValueError, 'Unrecognized save_freq'):
      keras.callbacks.ModelCheckpoint(
          filepath,
          monitor=monitor,
          save_best_only=save_best_only,
          mode=mode,
          save_freq='invalid_save_freq')
    # The following should not raise ValueError.
    keras.callbacks.ModelCheckpoint(
        filepath,
        monitor=monitor,
        save_best_only=save_best_only,
        mode=mode,
        save_freq='epoch')
    keras.callbacks.ModelCheckpoint(
        filepath,
        monitor=monitor,
        save_best_only=save_best_only,
        mode=mode,
        save_freq=3)