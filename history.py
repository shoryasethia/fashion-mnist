from matplotlib import pyplot as plt

def plot_all_histories(histories):
    plt.figure(figsize=(12, 12))
    
    for i, history in enumerate(histories, start=1):
        # Plot training loss
        plt.plot(history.history['loss'], label=f'Model {i} Training Loss')
        # Plot validation loss
        plt.plot(history.history['val_loss'], label=f'Model {i} Validation Loss')
    
    plt.title('Model Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
