import tensorflow as tf

def create_f_k_model():
    """Create MLP model for f_k function"""
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

def create_g_model():
    """Create RNN model for g function"""
    model = tf.keras.Sequential([
        tf.keras.layers.SimpleRNN(32, activation='tanh', input_shape=(None, 2)),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model
