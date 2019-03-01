import arcade

class VocabularyMap(arcade.Window):

    @property
    def vcm(self):
        return self.__vcm

    @property
    def vocab(self):
        return self.__vocab

    def __init__(self):
        self.__vcm = [
            arcade.key.A,
            arcade.key.B,
            arcade.key.C,
            arcade.key.D,
            arcade.key.E,
            arcade.key.F,
            arcade.key.G,
            arcade.key.H,
            arcade.key.I,
            arcade.key.J,
            arcade.key.K,
            arcade.key.L,
            arcade.key.M,
            arcade.key.N,
            arcade.key.O,
            arcade.key.P,
            arcade.key.Q,
            arcade.key.R,
            arcade.key.S,
            arcade.key.T,
            arcade.key.U,
            arcade.key.V,
            arcade.key.W,
            arcade.key.X,
            arcade.key.Y,
            arcade.key.Z
        ]

        self.__vocab = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    def get_vocab_of_key(self, key):
        vcm_key = self.vcm.index(key)
        if vcm_key < len(self.vocab):
            return self.vocab[vcm_key]
        else:
            return ""